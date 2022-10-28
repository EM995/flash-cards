# cards/views.py

from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    CreateView,
    UpdateView,
    DeleteView,
)

from .models import Card, BOXES
from .forms import CardCheckForm

import random

# Displays a list of all cards
class CardListView(ListView):
    model = Card
    queryset = Card.objects.all().order_by('box', '-date_updated')
    
# A form for creating a card
class CardCreateView(CreateView):
    model = Card
    fields = ['question', 'answer', 'box']
    success_url = reverse_lazy('card-create')

# A form for updating a card
class CardUpdateView(CardCreateView, UpdateView):
    success_url = reverse_lazy('card-list')

# A little form for deleting a card
class CardDeleteView(DeleteView):
    model = Card
    success_url = reverse_lazy('card-list')


class BoxView(CardListView):
    template_name = "cards/box.html"
    form_class = CardCheckForm

    def get_queryset(self):
        return Card.objects.filter(box=self.kwargs['box_num'])

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['box_number'] = self.kwargs['box_num']
        context['last_box_number'] = (self.kwargs['box_num'] == BOXES[-1])
        if self.object_list:
            context['check_card'] = random.choice(self.object_list)
        return context
    
    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            card = get_object_or_404(Card, id=form.cleaned_data['card_id'])
            card.move(form.cleaned_data['solved'])
        return redirect(request.META.get('HTTP_REFERER'))
    