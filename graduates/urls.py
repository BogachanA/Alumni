from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^graduates/(\d+)/',views.graduateInfo, name='grad_bilgi'),
    url(r'^graduates/',views.graduates,name="mezunlar"),
]