import random
import pytz

from odoo import models, fields, api
from odoo.exceptions import ValidationError



class SaleOrder(models.Model):
    _inherit = "sale.order"

    test_field = fields.Char(string="Test",
                             default=lambda _: random.randint(0, 1_000_000),
                             compute="_compute_test_field",
                             states={'draft': [('readonly', False)]},
                             store=True)

    @api.constrains("test_field")
    def _check_test_field(self):
        if self.test_field:
            if len(self.test_field) > 50:
                raise ValidationError("Длина текста должна быть меньше 50 символов!" + str(len(self.test_field)))


    @api.depends("date_order", "amount_total")
    def _compute_test_field(self):
        user_tz = self.env.user.tz or self.env.context.get('tz')
        user_pytz = pytz.timezone(user_tz) if user_tz else pytz.utc
        for record in self:
            dt_tz = record.date_order.astimezone(
                user_pytz
            ).replace(tzinfo=None)
            record.test_field = f"{record.amount_total:,.2f} {dt_tz:%d/%m/%Y %H:%M:%S}"

