from django.conf.urls import url

from . import views


urlpatterns = [
    url(r'^graduates/(\d+)/',views.graduateInfo, name='grad_bilgi'),
    url(r'^clubs/(\d+)',views.clubPage,name='club_info'),
    url(r'^clubs/',views.clubs,name='clubs'),
    url(r'^$',views.graduates,name="mezunlar"),
]