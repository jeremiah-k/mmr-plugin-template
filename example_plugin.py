import asyncio

from mmrelay.matrix_utils import bot_command
from mmrelay.plugins.base_plugin import BasePlugin


class Plugin(BasePlugin):
    plugin_name = "example_plugin"

    @property
    def description(self):
        return "Example plugin demonstrating basic Meshtastic and Matrix message handling"

    async def handle_meshtastic_message(
        self, packet, formatted_message, longname, meshnet_name
    ):
        if "decoded" not in packet or "text" not in packet["decoded"]:
            return False

        message_text = packet["decoded"]["text"].strip()
        channel = packet.get("channel", 0)
        is_direct_message = self.is_direct_message(packet)

        if not self.is_channel_enabled(channel, is_direct_message=is_direct_message):
            return False

        if message_text.lower() == "!example":
            await asyncio.sleep(self.get_response_delay())

            success = self.send_message(
                text="Hello from the example plugin!",
                channel=channel,
                destination_id=packet.get("fromId") if is_direct_message else None,
            )

            if success:
                self.logger.info("Response sent successfully")
                return True
            else:
                self.logger.error("Failed to send response")

        return False

    async def handle_room_message(self, room, event, full_message):
        if not bot_command(
            "example", event, require_mention=self.get_require_bot_mention()
        ):
            return False

        await self.send_matrix_message(
            room.room_id,
            "This is a response from the example plugin",
            reply_to_event_id=event.event_id,
        )
        return True
