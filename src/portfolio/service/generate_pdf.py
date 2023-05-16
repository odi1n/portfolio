from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML


def generate(
    templates,
    context,
    data: str,
):
    # Обработка шаблона
    html_string = render_to_string(templates, context)
    html = HTML(string=html_string)

    # Создание http ответа
    response = HttpResponse(content_type="application/pdf;")
    response["Content-Disposition"] = f"inline; filename={data}.pdf"
    response["Content-Transfer-Encoding"] = "binary"

    result = html.write_pdf(response)
    return result
