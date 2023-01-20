from odoo import http
from odoo.http import request


class DemoWebsiteSnippetController(http.Controller):
    @http.route(
        ["/snippet_test_ali/legumes"],
        type="json",
        auth="public",
        website=True,
        methods=["POST", "GET"],
        csrf=False,
    )

    def hello_world(self):
        return {"test": "pomme!"}
