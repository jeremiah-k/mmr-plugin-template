# MMRelay Plugin Template

Fork this repo and create a new one with the name of your plugin. Rename `example_plugin.py` to match your plugin name and customize from there.

For a full walkthrough, see the [MMRelay Plugin Development Guide](https://github.com/jeremiah-k/meshtastic-matrix-relay/wiki/Plugin-Development-Guide).

## Quick Start

After forking and customizing, users can activate your plugin by pinning to a commit:

```yaml
community-plugins:
  your_plugin_name:
    active: true
    repository: https://github.com/YourUsername/your-plugin-repo.git
    commit: 0123456789abcdef0123456789abcdef01234567
```

## Key Patterns

### Sending Meshtastic Messages

Use `self.send_message()` from `BasePlugin`. It handles queuing and rate limiting automatically:

```python
success = self.send_message(
    text="Your message here",
    channel=channel,
    destination_id=packet.get("fromId") if is_direct_message else None,
)
```

### Sending Matrix Messages

Use `self.send_matrix_message()` from `BasePlugin`. Pass `reply_to_event_id` to thread responses:

```python
await self.send_matrix_message(
    room.room_id,
    "Your message here",
    reply_to_event_id=event.event_id,
)
```

### Checking Commands

Use `bot_command()` with `self.get_require_bot_mention()` to respect the user's configuration:

```python
if bot_command("your_command", event, require_mention=self.get_require_bot_mention()):
    # handle the command
```

### Channel and DM Handling

Check whether to respond on a given channel:

```python
is_direct_message = self.is_direct_message(packet)
channel = packet.get("channel", 0)

if not self.is_channel_enabled(channel, is_direct_message=is_direct_message):
    return False
```

### Response Delay

Respect the configured response delay before sending mesh responses:

```python
import asyncio

await asyncio.sleep(self.get_response_delay())
```

## Code Quality

This template includes [Trunk](https://trunk.io) for code quality and formatting:

```bash
.trunk/trunk check --fix --all
```

Trunk is completely optional but recommended. The configuration is in `.trunk/` and works out of the box.

## Publishing

See [Step 6 of the Plugin Development Guide](https://github.com/jeremiah-k/meshtastic-matrix-relay/wiki/Plugin-Development-Guide#step-6-publishing-and-versioning) for the recommended versioning and release workflow.
