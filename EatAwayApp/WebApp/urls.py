from django.urls import path
from . import views

urlpatterns = [
	path('WebApp/', views.EatAppView, name="EatAppView"),
	path('add/', views.addEatAppView, name="addEatAppView"),
	path('MergeWithKiwi/', views.MergeWithKiwi, name="MergeWithKiwi"),
    path('delete/<int:i>/', views.deleteEatAppView, name="deleteEatAppView"),

]
