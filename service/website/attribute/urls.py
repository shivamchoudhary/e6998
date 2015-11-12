from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
        #url(r'^$',views.index,name='index'),
        url(r'^index/$',views.index,name='index'),
        url(r'^test/$',views.test,name='test'),
        ]
urlpatterns += staticfiles_urlpatterns()
