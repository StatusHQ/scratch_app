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
	path('myapplications/', views.UserApplicationsListView.as_view(), name='my_applications'),
	#path('myapplications/company', views.UserApplicationsListViewCompany.as_view(), name='my_applications_company'),
	#path('myapplications/position', views.UserApplicationsListViewPosition.as_view(), name='my_applications_position'),
	#path('myapplications/date', views.UserApplicationsListViewDate.as_view(), name='my_applications_date'),
	path('applications/<int:pk>/change_status/', views.ChangeStatus.as_view(), name='change_status'),
	path('myapplications/past/', views.PastUserApplications.as_view(), name='past_applications'),
	path('applications/past/', views.AllPastApplications.as_view(), name='all_past_applications'),
]