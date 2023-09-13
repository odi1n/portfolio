from typing import Any

from django import template

register = template.Library()


@register.filter()
def dict_join(qs: Any) -> str:
    values = ""
    for index, value in enumerate(qs.values("text")):
        values += value["text"]
        if index != qs.count() - 1:
            values += " / "
    return values
