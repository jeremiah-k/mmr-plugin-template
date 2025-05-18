# mmr-plugin-template
## MMRelay Plugin Template

Fork this repo and create a new one with the name of your plugin, rename `example_plugin.py` to the name of your plugin and go from there.

For more information on the basics creating plugins see the [MMRelay Plugin Development Guide](https://github.com/geoffwhittington/meshtastic-matrix-relay/wiki/Plugin-Development-Guide).

## Important Notes

### Matrix Client Usage

Always use the global `matrix_client` from `matrix_utils` or the `send_matrix_message()` method from `BasePlugin`. Never call `connect_matrix()` directly in your plugins, as this will reinitialize the client and cause unnecessary credential reloading.

```python
# Import the global matrix_client
from mmrelay.matrix_utils import matrix_client

# Check if matrix_client is initialized before using it
if matrix_client is None:
    self.logger.error("Matrix client is not initialized. Cannot send message.")
    return False

# Preferred method: Use send_matrix_message from BasePlugin
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
This is completely optional, but I recommend making use of [trunk.io](https://trunk.io)'s code quality tools. They are free for open source projects and are a great way to help keep your code clean and maintainable as you go.

This repo has already been initialized with [Code Quality Tools](https://docs.trunk.io/code-quality) and the configuration files are located in the `.trunk` folder in this repository.

To use this functionality you will need to install [VS Code](https://code.visualstudio.com/) (or [VS Codium](https://vscodium.com/)) and the [Code Quality Tools CLI](https://docs.trunk.io/code-quality/setup-and-installation/initialize-trunk).

The rest is handled automatically in code editor as you work.
