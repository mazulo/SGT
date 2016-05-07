from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.dashboard, name='dashboard'),
    url(r'^register/$', views.register, name='register'),
    url(r'^login/$', views.login, name='login'),
    url(r'^logout/$', views.logout, name='logout'),
    url(r'^edit/$', views.edit, name='edit'),
    url(r'^list-dbvs/$', views.list_dbvs, name='list_dbvs'),
    url(r'^dbv/(?P<pk>\d+)/', views.dbv_view, name='dbv_view')
]
