"""practicesite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),

    # forwards requests with the pattern applications/ to the module applications.urls (the file with the relative URL /applications/urls.py).
    path('applications/', include('applications.urls')),

    # deal with professional profile data
    path('prof_profile/', include('prof_profile.urls')),

    # add url to redirect the base url to our applications app
    path('', RedirectView.as_view(url='/applications/', permanent=True)),

    # add django auth urls for login, logout, and password management
    path('accounts/', include('django.contrib.auth.urls')),
]

# use Static() to add url mappings to serve static files during development 

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)