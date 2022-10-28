# cards/templatetags/cards_tags.py

from django import template

from cards.models import Card, BOXES


register = template.Library()


@register.inclusion_tag("cards/box_links.html")
def boxes_as_links():
    boxes = []
    for box_num in BOXES:
        card_count = Card.objects.filter(box=box_num).count()
        boxes.append({
            'card_count': card_count,
            'number': box_num
        })
        
    return {'boxes': boxes}