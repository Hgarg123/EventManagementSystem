from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout 
from .forms import *
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm

GUEST_COUNT_CHOICES = { 'Upto 50':50,  'Upto 100':100, 'Upto 150': 150, 'Upto 250': 250, 'Upto 350': 350, 'Upto 450': 450, 'Upto 500':500 }

def login2(request):
    _message = 'Please sign in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active and user.is_admin:
                 _message = 'Yor are Admin. Please login as Admin Panel'
            elif user.is_active:
                login(request, user)
                return redirect('home')
            else:
                _message = 'Your account is not activated'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'login.html', context)

def forgotView(request):
    _message = 'Please Enter Details'
    if request.method == 'POST':
        _username = request.POST['username']
        _email = request.POST['email']
        _mobileno = request.POST['mobileno']
        _password = request.POST['password']
        _confirmpassword = request.POST['confirmpassword']
        user = User.objects.filter(username=_username)
        if user.count() == 0:
            _message = 'Invalid Username'
        elif user is not None:
            user = User.objects.get(username=_username)
            if user.email!=_email or user.mobile_no!=_mobileno:
                _message = 'Invalid Mobile Number or Email'
            elif _password != _confirmpassword :
                _message = "Passowrd do not match"
            else:
                user.set_password(_password)
                user.save()
                _message = "Password changed successfully"
    context = {'message': _message}
    return render(request, 'ForgotPassword.html', context)


def loginadmin(request):
    _message = 'Please sign in'
    if request.method == 'POST':
        _username = request.POST['username']
        _password = request.POST['password']
        user = authenticate(username=_username, password=_password)
        if user is not None:
            if user.is_active and user.is_admin:
                login(request, user)
                return redirect('adminhome')
            # if user.is_active:
            #     login(request, user)
            #     return redirect('home')
            else:
                _message = 'Please Login as Admin Account'
        else:
            _message = 'Invalid login, please try again.'
    context = {'message': _message}
    return render(request, 'AdminLogin.html', context=context)

def RegisterView(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            login(request, user)
            return redirect("home")

        else:
            for msg in form.error_messages:
                print(form.error_messages[msg])

            return render(request=request,
                          template_name="Registration.html",
                          context={"form": form})

    form = SignUpForm
    return render(request=request,
                  template_name="Registration.html",
                  context={"form": form})



def HomePageView(request):
    events = Event.objects.all()
    context = {'events': events }
    return render(request, 'home.html',context=context)

def AdminHomePageView(request):
    bookings = Booking.objects.filter()
    context = {'bookings': bookings }
    return render(request, 'AdminHome.html',context=context)

def AboutView(request):
    return render(request, 'About.html')

def AdminOrCustView(request):
    return render(request, 'AdminOrCust.html')

def GalleryView(request):
    return render(request, 'Gallery.html')

def VenuesView(request,pk):
    if request.user == None:
        return redirect('homepage')
    venues = Venue.objects.filter(event__id=pk)
    context = {'venues': venues }
    print(venues)
    return render(request, 'Venues.html',context=context)

def BookingView(request,pk):
    if request.user == None:
        return redirect('homepage')
    venue = Venue.objects.get(id=pk)
    print(venue)
    context = {'venue': venue }
    if request.method == "POST":
        food_type = request.POST['food']
        dinner_type = request.POST['food-type']
        guest_count = request.POST['guest']
        date = request.POST['date']
        print(request.user)
        user = User.objects.get(id=request.user.id)
        amount = 0
        if dinner_type == "normal":
            amount = GUEST_COUNT_CHOICES[guest_count] * venue.normal_plate_rate 
        elif dinner_type == "deluxe":
            amount = GUEST_COUNT_CHOICES[guest_count] * venue.deluxe_plate_rate 
        elif dinner_type == "royal":
            amount = GUEST_COUNT_CHOICES[guest_count] * venue.royal_plate_rate 
        Booking.objects.create(user=user,venue=venue,food_type=food_type,dinner_type=dinner_type,guest_count=GUEST_COUNT_CHOICES[guest_count],date=date,total_cost=amount)
        return redirect('myevents')
    return render(request, 'Booking.html',context=context)

def ServicesView(request):
    return render(request, 'Services.html')

def BlogView(request):
    return render(request, 'Blog.html')

def policy_View(request):
    return render(request, 'Privacypolicy.html')

def terms_View(request):
    return render(request, 'TermsOfServices.html')

def MyEventsView(request):
    bookings = Booking.objects.filter(user=request.user)
    context = { 'bookings' : bookings }
    return render(request, 'MyEvents.html',context=context)

def ContactUsView(request):
    return render(request, 'ContactUs.html')


def ForgotView(request):
    return render(request, 'ForgotPassword.html')

def LogoutView(request):
    logout(request)
    return redirect('homepage')

def KnowmoreView(request):
    return render(request, 'Knowmore.html')


def MenuView(request):
    return render(request, 'menu.html')


def CartView(request):
    return render(request, 'cart.html')


def logout_request(request):
    logout(request)
    messages.info(request, "Logged out successfully!")
    return redirect("homepage")


def LoginHomePageView(request):
    return render(request, 'index.html')

def ConfirmBookingView(request,pk):
    booking = Booking.objects.get(id=pk)
    booking.status = "CONFIRMED"
    booking.isPending = False
    booking.save()
    return redirect('adminhome')

def CancelBookingView(request,pk):
    booking = Booking.objects.get(id=pk)
    booking.status = "CANCELLED"
    booking.isPending = False
    booking.save()
    return redirect('adminhome')