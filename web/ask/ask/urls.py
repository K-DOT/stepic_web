from django.conf.urls import patterns, include, url
from qa.views import index, popular, question, ask, test
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ask.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', index, name='index'),
    url(r'^login/', test),
    url(r'^signup/', test),
    url(r'^question/(?P<id>\d+)/', question, name='question'),
    url(r'^ask/', ask),
    url(r'^popular/', popular),
    url(r'^new/', test)
)
