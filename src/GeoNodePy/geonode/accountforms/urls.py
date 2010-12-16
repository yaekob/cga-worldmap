from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template
from django.contrib.auth import views as auth_views

from registration.views import activate
from registration.views import register
from geonode.accountforms.views import registerHarvard, registercompleteHarvard
from geonode.accountforms.forms import UserRegistrationForm

urlpatterns = patterns('',
                       url(r'^register/$',
                           registerHarvard,
                           {'form_class' : UserRegistrationForm},
                           name='registration_register'),
                       url(r'^registercomplete/$',
                           registercompleteHarvard,
                           name='registration_complete'),                                                      
                       (r'', include('registration.urls')),
                       )