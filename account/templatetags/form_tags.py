from django import template

register = template.Library()





@register.simple_tag
def add_class(field, css):
    return field.as_widget(attrs={"class": str(css)})