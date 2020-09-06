
odoo.define('addressed_action.DebugManager', ['web.DebugManager'], function (require) {
    "use strict";
    var DebugManager = require('web.DebugManager');

    DebugManager.include({
        addressed_action_view: function(){
            this.do_action('addressed_action.action_addressed_action');
        }
    });
});
