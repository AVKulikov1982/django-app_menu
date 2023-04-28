from django.urls import path
from app_menu.views import menu, menu_view, sub_menu_view

urlpatterns = [
    path("", menu, name="menu"),
    path("<slug:name_menu>/", menu_view, name="menu_view"),
    path("<slug:name_menu>/<slug:name_node>/", sub_menu_view, name="sub_menu"),
]