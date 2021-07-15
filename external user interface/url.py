urlpatterns = patterns('',
    ...
    url(r'^n3code/$', HomeView.as_view(template_name='home.html'), name='home'),
    url(r'^accounts/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^accounts/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    ...
)