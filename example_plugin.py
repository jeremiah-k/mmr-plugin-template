from mmrelay.plugins.base_plugin import BasePlugin
from mmrelay.meshtastic_utils import connect_meshtastic
from mmrelay.matrix_utils import bot_command


class Plugin(BasePlugin):
    plugin_name = "example_plugin"  # Define plugin_name as a class variable

    @property
    def description(self):
        """Get the plugin description for help text."""
        return (
            "Example plugin demonstrating basic Meshtastic and Matrix message handling"
        )

    async def handle_meshtastic_message(
        self, packet, formatted_message, longname, meshnet_name
    ):
        """
        Asynchronously processes incoming Meshtastic packets, handling only text messages and verifying channel enablement.

        Returns:
            bool: True if the message was handled by this plugin, False otherwise.
        """
        # Check if the packet is a TEXT_MESSAGE_APP packet
        if (
            "decoded" in packet
            and "portnum" in packet["decoded"]
            and packet["decoded"]["portnum"] == "TEXT_MESSAGE_APP"
        ):
            self.logger.debug("Debug logging on Meshtastic TEXT_MESSAGE_APP message")

            # Example of how to get the Meshtastic client
            meshtastic_client = connect_meshtastic()

            # Example of checking if a message is a direct message
            toId = packet.get("to")
            is_direct_message = False  # Default to False
            if meshtastic_client and meshtastic_client.myInfo:
                myId = meshtastic_client.myInfo.my_node_num
                is_direct_message = toId == myId

            # Example of checking if the channel is enabled for this plugin
            channel = packet.get("channel", 0)
            if not self.is_channel_enabled(
                channel, is_direct_message=is_direct_message
            ):
                return False

            # Add your plugin logic here
            # For example, you could check for specific text patterns, commands, etc.

            # Return True to indicate the message was processed
            return True

        return False

    async def handle_room_message(self, room, event, full_message):
        """
        Asynchronously handles Matrix room messages, responding to commands directed at this plugin.

        Returns:
            bool: True if a command was processed and a response sent; False otherwise.
        """
        self.logger.debug("Debug logging on Matrix message")

        # Example of checking if a message is a command for this plugin
        if bot_command(self.plugin_name, event):
            # The send_matrix_message method handles client initialization checks and logs an error if needed
            await self.send_matrix_message(
                room_id=room.room_id,
                message="This is a response from the example plugin",
            )
            return True

        return False
