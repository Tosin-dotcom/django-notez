from django.urls import path

from .views import home_view, story_view, note_view, create_view, delete_view, edit_view


urlpatterns = [
    path("", home_view),
    path("<str:user>/notes/", story_view),
    path("<str:user>/notes/create/", create_view),
    path("<str:user>/notes/<str:app>/", note_view),
    path("<str:user>/notes/<str:app>/delete/", delete_view),
    path("<str:user>/notes/<str:word>/edit/", edit_view),
]
