from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from .models import ProfileSection

# Create your views here.

# Main page for the Professional Profile
def index(request):
	'''View function for home page of professional profile'''

	section_list = ProfileSection.objects.order_by('section_order')
	context = {
		'sections': section_list,
	}

	return render(request, 'prof_profile/index.html', context)

# 
# Individual pages for sections of professional profile
def prof_section(request, section_id):
	return HttpResponse("Hello, you are at section %s in your professional profile." % section_id)
# 
# Page to edit a section
def prof_edit(request, section_id):
	'''View function for home page of professional profile'''
	return HttpResponse("Hello, you are here to edit section %s of your professional profile." % section_id)
# 
# Page to add a new section
def prof_create(request):
	'''View function for home page of professional profile'''
	return HttpResponse("Hello, you creating a new section for your professional profile.")