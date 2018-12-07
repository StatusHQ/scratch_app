from django.urls import path
from . import views

urlpatterns = [
	path('', views.index, name='index'),
	path('applications/', views.ApplicationsListView.as_view(), name='applications'),
	path('applications/<int:pk>', views.ApplicationDetailView.as_view(), name='application-detail'),
]