from django.shortcuts import render, get_object_or_404
from applications.models import Application 
from django.views import generic

# Create your views here.
def index(request):
	'''View function for home page of site'''

	# Generate counts of applications
	num_apps = Application.objects.all().count()

	# Get number of applications with each status
	num_inprogress = Application.objects.filter(status__exact='p').count()
	num_applied = Application.objects.filter(status__exact='a').count()
	num_interviewing = Application.objects.filter(status__exact='i').count()
	num_offered = Application.objects.filter(status__exact='o').count()
	num_denied = Application.objects.filter(status__exact='d').count()
	num_removed = Application.objects.filter(status__exact='r').count()

	context = {
		'num_apps': num_apps,
		'num_inprogress': num_inprogress,
		'num_applied': num_applied,
		'num_interviewing': num_interviewing,
		'num_offered': num_offered,
		'num_denied': num_denied,
		'num_removed': num_removed,
	}

	return render(request, 'index.html', context=context)

class ApplicationsListView(generic.ListView):
	model = Application
	context_object_name = 'applications_list'	# own name for list as template variable
	'''
	def get_queryset(self):
		return Application.objects.filter(status__icontains='0')[:5] # Get 5 applications with status 'offered' NEED TO TEST
	'''
	template_name = 'applications/applications_list.html'  # Specify your own template name/location

class ApplicationDetailView(generic.DetailView):
	model = Application