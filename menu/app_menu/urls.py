from django.urls import path
from app_menu.views import menu_view, main_category

urlpatterns = [
    path("", menu_view, name="menu_view"),
    path("<slug:name_node>/", main_category, name="main"),
    # path("<slug:main_slug>/<slug:sub_slug>/", sub_category, name="sub")
]