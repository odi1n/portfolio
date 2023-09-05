from typing import Any

from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML


def generate(
    templates: str,
    context: dict[str, Any],
    data: str,
) -> HttpResponse:
    html_string = render_to_string(templates, context)
    html = HTML(string=html_string)

    response = HttpResponse(content_type="application/pdf;")
    response["Content-Disposition"] = f"inline; filename={data}.pdf"
    response["Content-Transfer-Encoding"] = "utf8-to-binary"

    html.write_pdf(response)
    return response
