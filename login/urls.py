from django.urls import path
from django.conf.urls import url,include
from django.urls import include
from login import views
app_name='login'
urlpatterns = [
    path('index/', views.index),
    # path('table/', views.table),
    # path('spread/', views.spread),
    # path('remark/', views.remark),
    # path('people/', views.people),
    url(r'^table/(?P<id>[0-9]+)$', views.table, name='table'),
    url(r'^spread/(?P<id>[0-9]+)$', views.spread, name='spread'),
    url(r'^remark/(?P<id>[0-9]+)$', views.remark, name='remark'),
    url(r'^people/(?P<id>[0-9]+)$', views.people, name='people'),
]