from django.shortcuts import render
from app_menu.models import Menu, MenuCategory


def menu(request):
	menus = Menu.objects.all()
	return render(request, "main.html", context={'menus': menus})


def menu_view(request, name_menu):
	menu = Menu.objects.get(slug=name_menu)
	categories = MenuCategory.objects.filter(menu=menu).filter(level=0)
	return render(request, "menu_view.html", context={'categories': categories, 'name_menu': name_menu})


def sub_menu_view(request, name_menu, name_node):
	menu = Menu.objects.get(slug=name_menu)
	categories = MenuCategory.objects.get(menu=menu, slug=name_node).get_ancestors(ascending=True, include_self=True) | MenuCategory.objects.get(menu=menu, slug=name_node).get_children()
	return render(request, "menu_view.html", context={'categories': categories})
