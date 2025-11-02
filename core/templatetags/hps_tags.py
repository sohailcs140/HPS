from django import template
register = template.Library()


@register.filter
def getProperName(value:str)->str:
    return value.replace("_"," ").capitalize()