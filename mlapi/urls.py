
from django.contrib import admin
from django.urls import path,include
from django.conf.urls import url,include  
  

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^',include('api_test.urls'))
]
