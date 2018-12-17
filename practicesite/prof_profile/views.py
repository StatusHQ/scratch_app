from django.shortcuts import render
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

# Create your views here.

# Main page for the Professional Profile
def index(request):
	'''View function for home page of professional profile'''
	return HttpResponse("Hello, you are at your professional profile.")

# 
# Individual pages for sections of professional profile
def prof_section(request):
	'''View function for home page of professional profile'''
	return HttpResponse("Hello, you are in a section of your professional profile.")
# 
# Page to edit a section
def prof_edit(request):
	'''View function for home page of professional profile'''
	return HttpResponse("Hello, you are to edit a section of your professional profile.")
# 
# Page to add a new section
def prof_create(request):
	'''View function for home page of professional profile'''
	return HttpResponse("Hello, you creating a new section for your professional profile.")