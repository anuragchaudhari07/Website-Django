"""ebarristers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from consumer.views import SignUpView,HomeView,LibraryView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',HomeView.as_view(), name='home'),
	path('consumer/', include('consumer.urls', namespace='consumer')),
	path('harassment/', include('harassment.urls', namespace='harassment')),
    path('divorce/', include('divorce.urls', namespace='divorce')),
    path('domestic/', include('domestic.urls', namespace='domestic')),
    path('signup/',SignUpView.as_view(), name='signup'),
    path('library/',LibraryView.as_view(), name='library'),
    path('accounts/', include('django.contrib.auth.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
