from odoo import fields, models, api, _, exceptions


class AddressedAction(models.Model):
    _name = 'addressed.action'

    name = fields.Char(string='Name')
    external_id = fields.Char(string='External ID', required=True)

    @api.multi
    def charge_action(self):
        if len(self) == 1:
            try:
                action = self.env.ref(self.external_id)
            except ValueError:
                raise exceptions.Warning(_('External ID not found in the system'))
            actions = [
                'ir.actions.act_window', 'ir.actions.act_url',
                'ir.actions.server', 'ir.actions.report',
                'ir.actions.client', 'ir.cron'
            ]
            if action._name in actions:
                return action.read()[0]
            else:
                raise exceptions.Warning(
                    _('Verify the model of the external id')
                )
