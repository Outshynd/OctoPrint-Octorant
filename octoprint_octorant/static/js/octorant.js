/*
 * View model for OctoPrint-OctoRant
 *
 * Author: Benjamin Chanudet
 * License: MIT
 */
$(function() {
    function OctorantViewModel(parameters) {
        var self = this;
        self.settings = parameters[1];

        self.events = null;
        self.progress = null;
        self.prusa_user_action = null;

        self.onBeforeBinding = () => {
            self.events = self.settings.settings.plugins.octorant.events;
            self.progress = self.settings.settings.plugins.octorant.progress;
            self.prusa_user_action = self.settings.settings.plugins.octorant.prusa_user_action;

            console.log(self);
        }
    }

    // view model class, parameters for constructor, container to bind to
    OCTOPRINT_VIEWMODELS.push({
        construct: OctorantViewModel,
        dependencies: [ "loginStateViewModel", "settingsViewModel" ],
        elements: ["div#settings_plugin_octorant"]
    });
});
