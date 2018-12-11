from django.shortcuts import render, get_object_or_404
from applications.models import Application 
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from applications.models import Application 
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.mixins import LoginRequiredMixin

class UserApplicationsListView(LoginRequiredMixin, generic.ListView):
	'''Generic class-based view listing user applications'''
	model = Application 
	context_object_name = 'applications_list'
	template_name = 'applications/user_applications.html'
	paginate_by = 10

	def get_queryset(self):
		return Application.objects.filter(owner=self.request.user).order_by('status')

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

# Create your views here.
def index(request):
	'''View function for home page of site'''

	if not request.user.is_authenticated:
		return render(request, 'index.html')
	else:
		# Generate counts of applications
		num_apps = Application.objects.filter(owner=request.user).count()

		# Get number of applications with each status
		num_inprogress = Application.objects.filter(status__exact='p', owner=request.user).count()
		num_applied = Application.objects.filter(status__exact='a', owner=request.user).count()
		num_interviewing = Application.objects.filter(status__exact='i', owner=request.user).count()
		num_offered = Application.objects.filter(status__exact='o', owner=request.user).count()
		num_denied = Application.objects.filter(status__exact='d', owner=request.user).count()
		num_removed = Application.objects.filter(status__exact='r', owner=request.user).count()

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


class ApplicationCreate(LoginRequiredMixin, CreateView):
	model = Application
	fields = ['company', 'position', 'date_applied', 'deadline', 'status']

	def form_valid(self, form):
		form.instance.owner = self.request.user
		return super().form_valid(form)

class ApplicationUpdate(UpdateView):
	model = Application 
	fields = '__all__'

class ApplicationDelete(DeleteView):
	model = Application
	success_url = reverse_lazy('applications')