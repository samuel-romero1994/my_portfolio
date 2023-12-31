"""
URL configuration for sam_web project.

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
from core import views as views_core
from portafolio import views as views_port
from django.contrib import admin
from django.urls import path

from django.conf import settings #accedo a las configuraciones que hice en settings

urlpatterns = [
    path('', views_core.home, name="home"),
    path('about_me/', views_core.about, name="about"),
    path('portfolio/', views_port.portfolio, name="portfolio"),
    path('contact/', views_core.contact, name="contact"),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) + static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
               #=url de donde queremos mostrar los archivos(lo importo de settings, la raiz donde lo va a encontrar los ficheros media)
