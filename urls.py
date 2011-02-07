from django.conf.urls.defaults import *
from django.conf import settings

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()


urlpatterns = patterns('',
    # Example:
    # (r'^apprising/', include('apprising.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    (r'^admin/', include(admin.site.urls)),

    # django-tinymce
    (r'^tinymce/', include('tinymce.urls')),

    # wynton - blog app
    #(r'^blog/categories/', include('wynton.urls.categories')),
    #(r'^blog/', include('wynton.urls.entries')),
    url(r'^weblog/', include('zinnia.urls')),
    url(r'^comments/', include('django.contrib.comments.urls'))
)

if settings.DEBUG:
    urlpatterns += patterns('',
        (r'^static/(?P<path>.*)$', 'django.views.static.serve', \
        {'document_root': settings.STATIC_FILE_ROOT}),
    # tinymce setup from "Practical Django Projects", Ch. 3
    #(r'^tiny_mce/(?P<path>.*)$', 'django.views.static.serve', \
    #    {'document_root': settings.STATIC_FILE_ROOT + "/js/tiny_mce"}),
    )

# wes handles content like flatpages
# i.e. wildcards all get sent to wes to handle
# this has to go below everything else, or it breaks things
urlpatterns += patterns('',
        (r'', include('wes.urls')),
)
