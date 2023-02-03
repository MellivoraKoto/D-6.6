from django import template


register = template.Library()
black_list = ['доцент', 'пасть', 'редиска', 'тырить', 'фуфло']

@register.filter(name='censor')
def censor(value, arg):
    for i in value.split():
        if i.lower() in black_list:
            value = value.replace(i, arg)
    return value

