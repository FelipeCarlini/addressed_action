openerp.addressed_action = function(instance) {
    instance.web.ViewManagerAction.include({
    on_debug_changed: function (evt) {
        var self = this,
            $sel = $(evt.currentTarget),
            $option = $sel.find('option:selected'),
            val = $sel.val(),
            current_view = this.views[this.active_view].controller;
            switch (val) {
                case 'addressed_action_view':
                    this.do_action('addressed_action.action_addressed_action');
                break;
            }
            this._super.apply(this, arguments);
        },
    });

};
