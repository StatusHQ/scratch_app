from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

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
    section = get_object_or_404(ProfileSection, pk=section_id)

    context = {
    	'section': section,
    }

    return render(request, 'prof_profile/prof_section.html', context)
# 
# 
# Page to edit a section
def prof_section_edit(request, section_id):
	'''View function for home page of professional profile'''
	section = get_object_or_404(ProfileSection, pk=section_id)
	try:
		section.profileentry_set.create(entry_name=request.POST['experience'])
	except (ValueError, section.DoesNotExist):
		return render(request, 'prof_profile/prof_section.html', {
			'section' : section,
			'error_message' : "Section Does not exist.",
		})
	else:
		section.save()
		return HttpResponseRedirect(reverse('prof_profile:prof_section', args=(section.id,)))


# 
# 
# Page to add a new section
def prof_create(request):
	'''View function for home page of professional profile'''
	return HttpResponse("Hello, you creating a new section for your professional profile.")