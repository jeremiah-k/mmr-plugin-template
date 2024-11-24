from plugins.base_plugin import BasePlugin

class Plugin(BasePlugin):
    plugin_name = "example_plugin"

    async def handle_meshtastic_message(self, packet, formatted_message, longname, meshnet_name):
        # Check if the packet is a TEXT_MESSAGE_APP packet
        if "decoded" in packet and "portnum" in packet["decoded"]:
            if packet["decoded"]["portnum"] == "TEXT_MESSAGE_APP":
                self.logger.debug("Debug logging on Meshtastic TEXT_MESSAGE_APP message")

    async def handle_room_message(self, room, event, full_message):
        self.logger.debug("Debug logging on Matrix message")
