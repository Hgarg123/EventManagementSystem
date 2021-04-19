from django.urls import path
from .views import *
from django.contrib.auth import views as auth_views
from django.conf.urls import url
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('Home/', HomePageView, name="home"),
    path('AdminHome/', AdminHomePageView, name="adminhome"),
    path('About/', AboutView),
    path('forgot/', ForgotView),
    path('knowmore/', KnowmoreView),
    path('menu/', MenuView),
    path('AdminOrCust/',AdminOrCustView),
    path('Gallery/',GalleryView),
    path('Services/',ServicesView),
    path('MyEvents/',MyEventsView,name='myevents'),
    path('ForgotPassword/',forgotView),
    path('ContactUs/',ContactUsView),
    path('Logout/',LogoutView),
    path('Blog/',BlogView),
    path('cart/', CartView),
    path('venues/<int:pk>/',VenuesView),
    path('booking/<int:pk>/',BookingView),
    path('confirmbooking/<int:pk>/',ConfirmBookingView),
    path('cancelbooking/<int:pk>/',CancelBookingView),
    path('', LoginHomePageView, name="homepage"),
    path('login/', login2, name="loginhome"),
    path('adminlogin/', loginadmin, name="adminlogin"),
    path('register/', RegisterView),
    path("logout", logout_request, name="logout"),
    path("privacypolicy/", policy_View, name="privacy" ),
    path("termsofservices/", terms_View, name="terms"),
    path(
        'change-password/',
        auth_views.PasswordChangeView.as_view(
            template_name='commons/change-password.html',
            success_url = '/'
        ),
        name='change_password'
    ),
]
