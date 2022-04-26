import markdown
from django import template
from django.utils.safestring import mark_safe


register = template.Library()

#掲示物番後を表示するため引き算が必要だけど、addしかなくてテンプレートフィルターを作成
@register.filter
def sub(value, arg):
    return value - arg

@register.filter
def mark(value):
    extensions = ["nl2br", "fenced_code"]
    return mark_safe(markdown.markdown(value, extensions=extensions))