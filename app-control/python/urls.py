from django.contrib import admin
from django.urls import path
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('ab-test/', TemplateView.as_view(template_name="index.html")),
    path('control-response/', views.clicked),
    path('treatment-response/', views.clicked)
] + staticfiles_urlpatterns()