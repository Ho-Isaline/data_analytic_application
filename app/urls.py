from django.urls import path,re_path
from django.views.decorators.csrf import csrf_exempt
from . import views


urlpatterns = [
	path('index', views.index, name='index'),
 	path('read_comic', views.read_comic, name='read_comic'),
	path('next_chap', views.read_next_chapter, name='next_chapter')

]