from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'home.views.home', name='home'),
    # url(r'^payu_demo/', include('payu_demo.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^payu-success/$','home.views.payu_success', name='payu_success'),

    url(r'^payu-failure/$', 'home.views.payu_failure', name='payu_failure'),
 
    url(r'^payu-cancel/$', 'home.views.payu_cancel', name='payu_cancel'),

)
