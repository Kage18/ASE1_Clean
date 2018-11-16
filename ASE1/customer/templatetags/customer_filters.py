from django import template

register = template.Library()

@register.filter
def get_qty(stock):
    try:
        stock = int(stock)
    except ValueError:
        raise ValueError('Stock should be an integer!')
    if stock <= 10:
        return list(range(stock))
    else:
        return list(range(10))
