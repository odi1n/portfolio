from django.http import HttpResponse
from django.template.loader import render_to_string
from weasyprint import HTML
import tempfile
from django.views import View
from users.models import Social, Language, WorkPlace
from ..models import Portfolio, Work, Experience, Tech
from ..models.type import CategoryType
from ..service.generate_pdf import generate


class PortfolioView(View):
    template_name = "mytemplates.html"

    def get(self, request, *args, **kwargs):
        portfolio = Portfolio.objects.filter(id=kwargs.get('pk')).first()
        if portfolio is None:
            return HttpResponse("error number portfokio")

        work = Work.objects.filter(portfolio=portfolio).first()
        experiences = Experience.objects.filter(portfolio=portfolio)

        socials = Social.objects.filter(user=portfolio.user)
        languages = Language.objects.filter(user=portfolio.user)
        work_places = WorkPlace.objects.filter(user=portfolio.user)

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
            "socials": socials,
            "languages": languages,
            "work_places": work_places,

            "work": work,

            "techs": techs,

            "experiences": experiences,
        }

        return generate(templates=self.template_name, context=context)
