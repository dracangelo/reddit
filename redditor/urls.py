from django.conf.urls import url
from . import views


urlpatterns=[
    url(r'^$',views.landing,name='landing'),
    url(r'^profile/$', views.profile, name='profile'),
    # url(r'^update_profile/$', views.update_profile, name='update_profile'),
    url(r'^image_form/$', views.image_form, name='image_form'),
]


