# -*- coding: utf-8 -*-
# © 2016 OpenSynergy Indonesia
# License AGPL-3.0 or later (http://www.gnu.org/licenses/agpl.html).

from openerp import models, fields, api
from openerp.addons.purchase.purchase import purchase_order


class PurchaseRequest(models.Model):
    _inherit = 'purchase.request'

    def _default_order_type(self):
        return self.env['purchase.order.type'].search([], limit=1)

    order_type = fields.Many2one(comodel_name='purchase.order.type',
                                 readonly=False,
                                 states=purchase_order.READONLY_STATES,
                                 string='Type',
                                 ondelete='restrict',
                                 default=_default_order_type)

