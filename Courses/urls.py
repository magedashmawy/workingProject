"""Courses URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.conf.urls import include,url
# from accounts.models import LoginForm

from products.views import product_LView , search , product_list_view

### changed !!!
from .views import *
from . import views
from django.conf import settings
from django.conf.urls.static import static
#### --- >>
## logout -->
from django.contrib.auth.views import logout
urlpatterns = [

    url(r'^admin/', admin.site.urls),
    url(r'^products-fbv/$', product_LView ),
    url(r'^(?P<category_id>[0-9]+)/$', views.cat, name="cat"),
    url(r'^category/(?P<course_id>[0-9]+)/$' , views.course_details, name="course_details"),
    url(r'^login$', views.login_page, name="login"),
    url(r'^register$', views.register_page , name="register"),
    ## new !!!!!
    url(r'^$', home_page, name="home_page"),
    url(r'^results/$', search , name ="search"),
    url(r'^join/(?P<course_id>[0-9]+)/$', join_course, name="join"),
    url(r'^profile$', profile, name="profile"),
    url(r'^payment/(?P<course_id>[0-9]+)/$', payment, name="payment"),
    url(r'^logout/$', logout, {'next_page': home_page }, name='logout'),
    url(r'^upload/$', views.upload, name="upload"),
    


    ###---->
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root= settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT , name="media")


""" url(r'^$', views.index, name="index")
 url('^products/',include('products.urls')) """
