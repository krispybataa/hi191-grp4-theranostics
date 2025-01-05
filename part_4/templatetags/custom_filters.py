from django import template

register = template.Library()

@register.filter
def split(value, arg):
    """
    Split a string into a list based on a delimiter
    Usage: {{ value|split:"," }}
    """
    return value.split(arg)

@register.filter
def getattr(obj, attr):
    """
    Get an attribute of an object dynamically
    Usage: {{ object|getattr:"attribute_name" }}
    """
    try:
        return obj.getattr(attr)
    except AttributeError:
        return None
