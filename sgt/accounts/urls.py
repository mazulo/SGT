from django.conf.urls import url


urlpatterns = [
    url(r'^register/$', 'sgt.accounts.views.register', name='register'),
    url(r'^login/$', 'sgt.accounts.views.login', name='login'),
    url(r'^logout/$', 'sgt.accounts.views.logout', name='logout'),
]
