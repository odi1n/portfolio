from django.db import models
from .custom_user import CustomUser
from .social_type import SocialType

class Social(models.Model):
    user = models.ForeignKey(CustomUser,
                             verbose_name="Пользователь",
                             on_delete=models.CASCADE)
    social_type = models.ForeignKey(SocialType,
                                    verbose_name="Тип соц.",
                                    on_delete=models.CASCADE)
    values = models.CharField(verbose_name="Значение",
                              max_length=255)
