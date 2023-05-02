from django.shortcuts import render
from app_menu.models import MenuCategory


def menu(request):
	menus = MenuCategory.objects.filter(level=0)
	return render(request, "main.html", context={'menus': menus})


def menu_view(request, name_menu):
	print(name_menu)
	categories = MenuCategory.objects.get(slug=name_menu).get_children()
	return render(request, "menu_view.html", context={'categories': categories})


def sub_menu_view(request, name_node):
	print(MenuCategory.objects.get(slug=name_node).id)
	categories = MenuCategory.objects.get(slug=name_node).get_ancestors(ascending=True, include_self=True) | MenuCategory.objects.get(slug=name_node).get_children()
	return render(request, "menu_view.html", context={'categories': categories})
