import transliterate
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import AnonymousUser
from django.views.decorators.clickjacking import xframe_options_exempt

from users.models import Social, Language, WorkPlace
from ..models import Portfolio, Work, Experience
from ..models.type import CategoryType
from ..service.generate_pdf import generate


class PortfolioView(View):
    template_name = "mytemplates.html"

    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        if request.user == AnonymousUser():
            return HttpResponse("error user auth")

        portfolio = Portfolio.objects.filter(id=kwargs.get('pk'),
                                             user=request.user).first()
        if portfolio is None:
            return HttpResponse("error number portfolio")

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
            portf = Portfolio.objects.filter(tech__category=category,
                                             user=portfolio.user).order_by('tech')
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

        return generate(templates=self.template_name,
                        context=context,
                        data=transliterate.translit(
                            f'Резюме - {portfolio.user.first_name} {portfolio.user.last_name}. {portfolio.get_stack_display()}',
                            reversed=True))
