from django.shortcuts import render, get_object_or_404 , redirect
from django.db.models import Q
from products.models import Product
from django.contrib.auth import authenticate , login
# from .forms import LoginForm
from accounts.forms import RegisterForm
#from example.config import pagination
# Create your views here.
def cat(request, category_id ):
    category_all = Product.objects.all()
    caat=[]
    if category_id == '0':
        f = "Health and Medicine"
    elif category_id == '1':
        f = "Self Improvement"
    elif category_id == '2':
        f = "Lifestyle"
    elif category_id == '3':
        f = "Engineering"
    elif category_id == '4':
        f = "Business and Economics"
    elif category_id == '5':
        f = "Computers and Technology"
    elif category_id == '6':
        f = "Arts and Design"
    elif category_id == '7':
        f = "Language and Communication"
    elif category_id == '8':
        f = "Math and Science"

    for c in category_all:
        if (c.category == f):
            caat.append(c)
    return render(request, 'courses.html', {'caat' : caat} )



def login_page(request):
    form = LoginForm(request.POST or None)
    print(request.user.is_authenticated)

    context = {
    'form' : form ,
    "myAcc" : "Log in"
    }
    if form.is_valid():
        print (form.cleaned_data)
        email = form.cleaned_data.get("name")
        password = form.cleaned_data.get("password")
        user = authenticate(request, email=email, password=password)
        if user is not None:
            login(request, user)
            context['form'] = LoginForm()
            return redirect("/")
        else:
            print("Error !!!")
    return render(request, 'login.html' , context)



def register_page(request):
    form = RegisterForm(request.POST or None)
    context = {
    'form' : form
    }
    if form.is_valid():
        form.save()
        return redirect("/")
    return render(request, 'register.html' , context)

def details(request , course_id):
    course = get_object_or_404( Product , pk=course_id)
    return render(request, 'details.html', {'course': course})

def home_page(request):
##    if request.user.is_authenticated():
    #print request.user.is_authenticated()
    all = Product.objects.all()
    return render(request, 'home_page.html',{'all':all})

def course_details(request , course_id):
    course = get_object_or_404( Product , pk=course_id)
    # context =  {
    # 'course' : course ,
    # 'flag' : 0
    # }
    return render(request, 'course_details.html', {'course': course})


def join_course(request , course_id):
    courses = get_object_or_404( Product , pk=course_id)
    request.user.joinedCourses.add(courses)
    request.user.save()

    context = {
    'course': courses,
    }
    return render(request, 'join.html', context)


def profile(request):
    courses = request.user.joinedCourses.all()
    userinfo = request.user.user_name
    context = {
    'course': courses,
    }
    return render(request, 'profile.html', context)


def payment(request, course_id):
    courses = get_object_or_404( Product , pk=course_id)
    request.user.joinedCourses.add(courses)
    request.user.save()

    context = {
    'course': courses,
    }
    return render(request, 'payment.html', context)
