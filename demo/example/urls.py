
from django.conf.urls import patterns, url, include


urlpatterns = patterns('example.views',
    url(r'^table/$', 'formset', { 'template': 'example/formset-table.html'}, name='example_table'),
 )
