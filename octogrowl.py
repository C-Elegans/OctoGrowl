from __future__ import absolute_import
import octoprint.plugin
import gntp.notifier
class OctoGrowl(octoprint.plugin.StartupPlugin):
    growl = None
    def on_after_startup(self):
        growl = gntp.notifier.GrowlNotifier(
            applicationName = "OctoGrowl",
            notifications = ["New Updates","New Messages"],
            defaultNotifications = ["New Messages"],
            hostname = "10.0.1.16", # Defaults to localhost
            password = "abcd" # Defaults to a blank password
        )
        growl.register()
        self._logger.info("Hello!")
        growl.notify(title = "Startup")
        
__plugin_name__ = "Hello World"
__plugin_version__ = "1.0"
__plugin_description__ = "A quick \"Hello World\" example plugin for OctoPrint"
__plugin_implementations__ = [OctoGrowl()]
