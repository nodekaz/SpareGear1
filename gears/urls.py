from django.conf.urls import url
from. import views

urlpatterns = [

    url(r'^$' , views.home , name='home'),
    url(r'^show/', views.show_gear , name='show'),
    url(r'^add_gear/', views.add_gear , name='add_gear'),

]
