from django.conf.urls import patterns,url
from dbapp import views
urlpatterns=patterns('',
   url(r'^$',views.index,name='index'),
   url(r'^department/(?P<department_name_url>\w+)/$', views.department, name='department'),
   )