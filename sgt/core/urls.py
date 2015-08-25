from django.conf.urls import url


urlpatterns = [
    url(r'^$', 'sgt.core.views.index', name='index'),
    # url(r'^listar_dbvs/$', views.list_dbvs, name='list_dbvs'),
    # url(r'^listar_unidades/$', views.list_unidades, name='list_unidades'),
    # url(r'^listar_mensalidade/(?P<user_dbv>[\w\-]+)/$', views.list_mensalidade, name='list_mensalidade'),
]
