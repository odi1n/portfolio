import transliterate
from django.http import HttpResponse
from django.views import View
from django.contrib.auth.models import AnonymousUser
from django.views.decorators.clickjacking import xframe_options_exempt

from ..models import Portfolio, Work, Experience
from ..models.type import CategoryType
from ..service.generate_pdf import generate


class PortfolioView(View):
    template_name = "mytemplates.html"

    @xframe_options_exempt
    def get(self, request, *args, **kwargs):
        if request.user == AnonymousUser():
            return HttpResponse("Error user auth")

        if request.user.is_staff:
            portfolio = Portfolio.objects.filter(id=kwargs.get("pk")).first()
        else:
            portfolio = Portfolio.objects.filter(
                id=kwargs.get("pk"), user=request.user
            ).first()
        if portfolio is None:
            return HttpResponse("Error number portfolio")

        work = Work.objects.filter(portfolio=portfolio).first()
        experiences = Experience.objects.filter(portfolio=portfolio)

        categories = [
            CategoryType.PROJRAMS_LANGUAGE,
            CategoryType.FRAMEWORK,
            CategoryType.LIBRARIES,
            CategoryType.DBMS,
            CategoryType.CLOUD_SERVICE,
            CategoryType.OTHER,
            CategoryType.DEVELOPMENT_TOOL,
            CategoryType.APP_TYPE,
        ]
        techs = []
        for category in categories:
            portfolio_data = Portfolio.objects.filter(
                tech__category=category, user=portfolio.user, id=portfolio.id
            ).order_by("tech")
            if portfolio_data.count() > 0:
                techs.append(
                    {
                        "label": category.label,
                        "params": portfolio_data.values_list("tech__text", flat=True),
                    }
                )

        return generate(
            templates=self.template_name,
            context={
                "portfolio": portfolio,
                "work": work,
                "techs": techs,
                "experiences": experiences,
            },
            data=transliterate.translit(
                f"Резюме - {portfolio.user.get_name}. {portfolio.get_stack_display()}",
                reversed=True,
            ),
        )