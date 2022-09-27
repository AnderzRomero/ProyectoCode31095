from django.urls import path

from UserCoder.views import *

urlpatterns = [
   path('login/', login_request, name='UserCoderLogin'),
   path('registro/', register, name='UserCoderRegister'),

]

