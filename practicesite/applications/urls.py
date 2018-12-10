from django.urls import path
from . import views
from django.conf.urls import url

urlpatterns = [
	path('', views.index, name='index'),
	path('applications/', views.ApplicationsListView.as_view(), name='applications'),
	path('applications/<int:pk>', views.ApplicationDetailView.as_view(), name='application-detail'),
	path('applications/create/', views.ApplicationCreate.as_view(), name='application_create'),
	path('applications/<int:pk>/update/', views.ApplicationUpdate.as_view(), name='application_update'),
	path('applications/<int:pk>/delete/', views.ApplicationDelete.as_view(), name='application_delete'),
	path('applications/signup/', views.signup, name='signup'),
]