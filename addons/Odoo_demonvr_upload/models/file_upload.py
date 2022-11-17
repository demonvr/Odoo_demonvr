from odoo import models, fields, api


class FileUpload(models.Model):
    _name = 'file.upload'
    _description = 'Upload File'

    name = fields.Char(string='File Name')
    file = fields.Binary(string='File', required=True)
    url = fields.Char(string='URL', compute="_compute_get_url")

    def action_upload_file(self):
        return True

    def _compute_get_url(self):
        base_url = self.env['ir.config_parameter'].get_param('web.base.url')
        self.url = f"{base_url}/web/content?model=file.upload&field=file&filename_field=name&id={self.id}"
