from __future__ import absolute_import
import octoprint.plugin

class OctoGrowl(octoprint.plugin.StartupPlugin):
    def on_after_startup(self):
        self._logger.info("Hello!")
        
__plugin_name__ = "Hello World"
__plugin_version__ = "1.0"
__plugin_description__ = "A quick \"Hello World\" example plugin for OctoPrint"
__plugin_implementations__ = [OctoGrowl()]
