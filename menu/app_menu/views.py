from django.shortcuts import render
from app_menu.models import MenuCategory


def menu_view(request):
	categories = MenuCategory.objects.filter(level=0)

	data = {
		"title": 'main',
		"test_data": 'test',
		"categories": categories,
	}
	
	return render(request, "main.html", context=data)


def main_category(request, name_node):
	
	categories = MenuCategory.objects.filter(level=0) | MenuCategory.objects.get(slug=name_node).get_ancestors(ascending=True, include_self=True) | MenuCategory.objects.get(slug=name_node).get_children()
	print(categories)
	data = {
		"title": 'main',
		"test_data": 'test',
		"categories": categories,
	}
	
	return render(request, "main.html", context=data)

#
# def sub_category(request, main_slug, sub_slug):
# 	categories = MenuCategory.objects.all()
# 	data = {
# 		"title": 'main',
# 		"test_data": 'test',
# 		"categories": categories,
# 	}
#
# 	return render(request, "main.html", context=data)