import tempfile

from django.http import HttpResponse
from django.template.loader import render_to_string

from weasyprint import HTML


def generate(templates, context, data: str):
    # Обработка шаблона
    html_string = render_to_string("mytemplates.html", context)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Создание http ответа
    response = HttpResponse(content_type="application/pdf;")
    response["Content-Disposition"] = f"inline; filename={data}.pdf"
    response["Content-Transfer-Encoding"] = "binary"
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, "rb")
        response.write(output.read())
    return response
