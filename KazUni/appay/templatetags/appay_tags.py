from django import template
from ..models import typeofoperations, typeofpays, organizations, bankcards, countrypartyes

register = template.Library()

@register.simple_tag
def get_items_from_db(field_name):
    models = {
        'typeofoperations': typeofoperations,
        'typeofpays': typeofpays,
        'organizations': organizations,
        'bankcards': bankcards,
        'countrypartyes': countrypartyes,
    }

    model = models.get(field_name)
    if model:
        data = model.objects.all().values('id', 'name')
        return {'data': data}
    else:
        return {'error': f'Model {field_name} not found'}

@register.filter(name='getattr')
def get_attribute(obj, attr):
    return getattr(obj, attr, None)