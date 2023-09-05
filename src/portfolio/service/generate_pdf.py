from typing import Any

from django.http import HttpResponse
from django.template.loader import render_to_string
from django.views.decorators.clickjacking import xframe_options_exempt
from weasyprint import HTML


def generate(
    templates: str,
    context: dict[str, Any],
    data: str,
) -> HttpResponse:
    # Обработка шаблона
    html_string = render_to_string(templates, context)
    html = HTML(string=html_string)

    # Создание http ответа
    response = HttpResponse(content_type="application/pdf;")
    response["Content-Disposition"] = f"inline; filename={data}.pdf"
    response["Content-Transfer-Encoding"] = "utf8-to-binary"

    result = html.write_pdf(response)
    return response
