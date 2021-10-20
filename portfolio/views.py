from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.views import View
from .models import Portfolio, Work, Experience, Tech
from users.models import Social, Language, WorkPlace
from .models.type import CategoryType


def generate(templates, context):
    # Обработка шаблона
    html_string = render_to_string('mytemplates.html', context)
    html = HTML(string=html_string)
    result = html.write_pdf()

    # Создание http ответа
    response = HttpResponse(content_type='application/pdf;')
    response['Content-Disposition'] = 'inline; filename=list_people.pdf'
    response['Content-Transfer-Encoding'] = 'binary'
    with tempfile.NamedTemporaryFile(delete=True) as output:
        output.write(result)
        output.flush()
        output = open(output.name, 'rb')
        response.write(output.read())
    return response


class PortfolioView(View):
    template_name = "mytemplates.html"

    def get(self, request, *args, **kwargs):
        portfolio = Portfolio.objects.filter(id=kwargs.get('pk'),
                                             user=request.user).first()
        work = Work.objects.filter(portfolio=portfolio).first()
        experiences = Experience.objects.filter(portfolio=portfolio)

        socials = Social.objects.filter(user=request.user)
        languages = Language.objects.filter(user=request.user)
        work_places = WorkPlace.objects.filter(user=request.user)

        categorys = [CategoryType.PROJRAMS_LANGUAGE, CategoryType.FRAMEWORK,
                     CategoryType.LIBRARIES, CategoryType.DBMS, CategoryType.CLOUD_SERVICE,
                     CategoryType.OTHER, CategoryType.DEVELOPMENT_TOOL, CategoryType.APP_TYPE]
        techs = []
        for category in categorys:
            portf = Portfolio.objects.filter(tech__category=category)
            if portf.count() > 0:
                techs.append({
                    "label": category.label,
                    "params": portf.values_list('tech__text', flat=True)
                })

        context = {
            "portfolio": portfolio,
            "work": work,
            "experiences": experiences,
            "techs": techs,

            "socials": socials,
            "languages": languages,
            "work_places": work_places,
        }

        return generate(templates=self.template_name, context=context)
