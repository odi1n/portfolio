from django import template
from django.utils.timezone import now
import locale
locale.setlocale(locale.LC_ALL,'')

register = template.Library()


@register.filter()
def dict_join(qs):
    values = ''
    for index, value in enumerate(qs.values('text')):
        values += value['text']
        if index != qs.count() - 1:
            values += ' / '
    return values

@register.filter()
def work_place_tags(qs):
    if qs.date_end is  None:
        value = f'По текущий момент'
    elif qs.date_end is not None:
        value = qs.date_end.strftime("%d %B %Y")
    return f'{qs.text} - {qs.whom}. {qs.date_start.strftime("%d %B %Y")} - {value}'