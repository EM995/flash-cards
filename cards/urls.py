
from django.urls import path
# Remove: from django.views.generic import TemplateView

from . import views

urlpatterns = [
    path(
        "",
        views.CardListView.as_view(),
        name='card-list'
    ),
    path(
        "new",
        views.CardCreateView.as_view(),
        name='card-create'
    ),
    path(
        "edit/<int:pk>",
        views.CardUpdateView.as_view(),
        name='card-update'
    ),
    path(
        "remove/<int:pk>",
        views.CardDeleteView.as_view(),
        name='card-delete'
    ),
    path(
        "box/<int:box_num>",
        views.BoxView.as_view(),
        name='box'
    ),
]