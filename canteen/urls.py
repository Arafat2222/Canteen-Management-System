from . import views
from django.urls import*

urlpatterns = [
    path('',views.home,name = 'home'),
    path('about/',views.about,name='about'),
    path('breakfast/',views.breakfast,name='breakfast'),
    path('lunch/',views.lunch,name='lunch'),
    path('others/',views.others,name='others'),
    path('cart/',views.cart,name='cart'),
    path('login/',views.login_signup,name='login'),
    # path('home/',views.HOME,name = 'home'),
]
