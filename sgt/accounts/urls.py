from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'sgt.accounts.views.dashboard', name='dashboard'),
    url(r'^register/$', 'sgt.accounts.views.register', name='register'),
    url(r'^login/$', 'sgt.accounts.views.login', name='login'),
    url(r'^logout/$', 'sgt.accounts.views.logout', name='logout'),
    url(r'^edit/$', 'sgt.accounts.views.edit', name='edit'),
    url(r'^list-dbvs/$', 'sgt.accounts.views.list_dbvs', name='list_dbvs'),
    url(r'^dbv/(?P<pk>\d+)/', 'sgt.accounts.views.dbv_view', name='dbv_view')
]
