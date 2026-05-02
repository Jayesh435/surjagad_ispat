from django import template

register = template.Library()


@register.filter
def split(value, delimiter=','):
    """Split a string by delimiter."""
    return value.split(delimiter)


@register.filter
def divisibleby(value, arg):
    """Check if value is 0 after mod (zero-indexed even rows)."""
    try:
        return int(value) % int(arg) == 0
    except (ValueError, ZeroDivisionError):
        return False
