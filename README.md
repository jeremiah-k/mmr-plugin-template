# mmr-plugin-template

## MMRelay Plugin Template

Fork this repo and create a new one with the name of your plugin, rename `example_plugin.py` to the name of your plugin and go from there.

For more information on the basics of creating plugins see the [MMRelay Plugin Development Guide](https://github.com/geoffwhittington/meshtastic-matrix-relay/wiki/Plugin-Development-Guide).

## Important Notes

### Matrix Client Usage

Always use the `send_matrix_message()` method from `BasePlugin`. Never call `connect_matrix()` directly in your plugins, as this will reinitialize the client and cause unnecessary credential reloading.

```python
# Preferred method: Use send_matrix_message from BasePlugin.
# This method automatically handles checking if the matrix client is initialized and logs an error if it's not available.
await self.send_matrix_message(room_id=room.room_id, message="Your message here")
```

### Plugin Name Initialization

Define `plugin_name` as a class variable in your plugin class. This is the recommended way to identify your plugin:

```python
class Plugin(BasePlugin):
    plugin_name = "your_plugin_name"  # Define plugin_name as a class variable

    # No need to override __init__() unless you need custom initialization

    async def handle_meshtastic_message(self, packet, formatted_message, longname, meshnet_name):
        # Your implementation here
        pass
```

## Code Quality Tools

This template includes [Trunk](https://trunk.io) for code quality and formatting. Trunk helps maintain clean, consistent code by automatically checking for issues and applying fixes.

### Using Trunk

The Trunk binary is included in this repository at `.trunk/trunk`. To check and fix your code:

```bash
.trunk/trunk check --fix --all
```

This will:
- Format your Python code with Black
- Check for linting issues with Ruff and other tools
- Apply automatic fixes where possible
- Ensure your code follows best practices

Trunk is completely optional but recommended for maintaining high code quality. The configuration is already set up in the `.trunk` directory, so you can start using it immediately without any additional setup.
