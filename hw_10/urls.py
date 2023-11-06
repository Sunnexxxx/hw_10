"""
URL configuration for hw_10 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static
from main import views


urlpatterns = [
    path('admin/', admin.site.urls),
    re_path(r'^band/(?P<genre>\D+)/(?P<slug>\D+)/', views.band_page, name='band'),
    re_path(r'^about/(?P<genre>\D+)/', views.about_page, name='about'),
    re_path(r'^$', views.main_page, name='main'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
