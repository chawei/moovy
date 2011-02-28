import views

urlpatterns = (
    (r'^movies/$', 'views.index'),
    # Example:
    # (r'^moovy/', include('moovy.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)