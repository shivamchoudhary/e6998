from django.conf.urls import url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from . import views

urlpatterns = [
        #url(r'^$',views.index,name='index'),
        url(r'^index/$',views.index,name='index'),
        url(r'^test/$',views.test,name='test'),
        url(r'^dryrun/$',views.dryrun,name='dryrun'),
        url(r'^configure/$',views.configure,name='configure'),
        url(r'^multielements/$',views.multielements,name='multielements'),
        url(r'^chart/$',views.chart,name='chart'),
        url(r'^multichart/$',views.multichart,name='multichart'),
        url(r'^prob/$',views.probability,name='probability'),
        url(r'^multiprob/$',views.multiprobability,name='multiprobability'),
        url(r'^visualization/(?P<path>.*)$',views.visualization,name='visualization'),
        ]
urlpatterns += staticfiles_urlpatterns()
