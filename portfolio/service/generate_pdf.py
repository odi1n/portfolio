from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.views import View


def generate(templates, context):
    # Обработка шаблона
    html_string = render_to_string('mytemplates.html', context)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Создание http ответа
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=Rezume.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response
