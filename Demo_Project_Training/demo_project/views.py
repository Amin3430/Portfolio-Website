from django.http import HttpResponse
from django.shortcuts import render
from .forms import UserForm

def aboutUs(request):
    return HttpResponse("Welcome to this page")

def contact(request):
    return HttpResponse("Welcome to contact page")

def services(request):
    return HttpResponse("Welcome to the services page")

def help_page(request):
    return HttpResponse("How can we he help you?")

def blog(request):
    return HttpResponse("Read our latest blog posts here.")


def home_page(request):
    data = {
        'title': 'Home page',
        'welcome': 'Welcome to Flynaut',
        'numbers':[],
        'student_details':[
            {'name': 'ABC', 'phone': 12345},
            {'name':'testing','phone':578797}],
    }
    return render(request,"index.html",data)


def user_form(request):
    form = UserForm()
    if request.method == 'POST':
        candidate_name = request.POST.get('candidate_name')
        contact = request.POST.get('contact')
        email = request.POST.get('email')
        expected_ctc = request.POST.get('expected_ctc')

        error_message = ""
        if email and not email.endswith("@gmail.com"):
            error_message = "Email must end with @gmail.com"
            
            return render(request, "userform.html", {
                'form': form,
                'candidate_name': candidate_name,
                'contact': contact,
                'email': email,
                'expected_ctc': expected_ctc,
                'error_message': error_message,
            })
            
    return render(request, "userform.html", {'form': form})
       
def submitform(request):
    return HttpResponse(request)



"""
def about(request):
    return render(request, "about.html")

def services(request):
    return render(request, "services.html")

def contact(request):
    return render(request, "contact.html")

def blog(request):
    return render(request, "blog.html")

def help(request):
    return render(request, "help.html")
"""


"""
def Dynamicdata(request,amin):
    return HttpResponse ("Name: Amin Pinjari")

def user_detail(request, id):
    return HttpResponse(f"User ID is: {id}")

def blog_detail(request, slug):
    return HttpResponse("This is the blog post:",slug)
"""


"""
from django.http import HttpResponse
from django.shortcuts import render, redirect

def home_page(request):
    return render(request, 'home.html')

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')
        print(f'Contact from {name} ({email}): {message}') 
        return redirect('thanks') 
    return render(request, 'contact.html') 

def thanks(request):
    return render(request, 'thanks.html')
"""