from django.contrib import admin
from django.conf.urls import  url
from .import views
app_name='todolist'
urlpatterns = [
    #url('admin/', admin.site.urls),
    url(r'^$', views.home,name='home'),
    url(r'^mark/(?P<pk>\d+)$',views.mark ,name="complete"),
    url(r'^unmark/(?P<pk>\d+)$',views.unmark ,name="incomplete"),
    url(r'^schedule/(?P<pk>\d+)$',views.see,name="see"),
    url(r'^deletecompleted/$',views.deletecompleted,name="deletecompleted"),
    url(r'^delete/(?P<pk>\d+)$',views.delete,name="delete"),
    url(r'^update/(?P<pk>\d+)$',views.update,name="update"),

]
