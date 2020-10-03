from openerp import fields, models, api, _, exceptions


class AddressedAction(models.Model):
    _name = 'addressed.action'
    _description = 'Addressed Action'

    @api.onchange('external_id')
    @api.multi
    def _get_action_name(self):
        for rec in self:
            if rec.external_id:
                try:
                    rec.name = self.env.ref(
                        rec.external_id.module + '.' + rec.external_id.name
                    ).name
                except Exception:
                    return

    name = fields.Char(string='Name', compute='_get_action_name', store=False)
    external_id = fields.Many2one('ir.model.data', string='External ID', required=True)

    @api.multi
    def charge_action(self):
        if len(self) == 1:
            try:
                action = self.env.ref(self.external_id.module + '.' + self.external_id.name)
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


class IRModelData(models.Model):
    _inherit = 'ir.model.data'

    @api.model
    def name_search(self, name, args=None, operator='ilike', limit=100):
        if self.env.context.get('addressed_action_view', False) == True:
            expr = list()
            rec_name = name
            if '.' in name:
                complete_name = name.split('.')
                module, rec_name = complete_name[0:2]
                expr += [('module', '=ilike', module)]
            expr += [('name', 'ilike', rec_name), ('model', '=', 'ir.actions.act_window')]
            recs = self.search(expr)
            res = [(rec.id, rec.module + '.' + rec.name) for rec in recs]
        else:
            res = super(IRModelData, self).name_search(name, args=args,
                    operator=operator, limit=limit)
        return res

    @api.multi
    def name_get(self):
        if self.env.context.get('addressed_action_view', False) == True:
            res = [(rec.id, rec.module + '.' + rec.name) for rec in self]
        else:
            res = super(IRModelData, self).name_get()
        return res
