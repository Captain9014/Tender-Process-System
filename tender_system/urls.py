"""
URL configuration for tender_system project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.views.generic import TemplateView
from django.urls import path, include



urlpatterns = [
    path('',TemplateView.as_view(
        template_name='home.html'
    ),
    name='home'
    ),
    path('admin/', admin.site.urls),
    path('', include('accounts.urls')),
    path('', include('tenderapp.urls')),
    path('',include('bidapp.urls')),
    path('',include('builderapp.urls')),
    path('',include('chatapp.urls')),
    path('',include('progressapp.urls')),
    path('',include('fileapp.urls')),
    path('',include('reviewapp.urls')),
    path('',include('notificationapp.urls')),
    path('', include('clientapp.urls')),
    
]

urlpatterns += static(
    settings.MEDIA_URL,
    document_root=settings.MEDIA_ROOT
)

if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )