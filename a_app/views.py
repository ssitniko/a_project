from django.shortcuts import render



def home_view(request):
    return render(request, 'a_app/home.html')

def catalog_view(request):
    return render(request, 'a_app/catalog.html')

def about_us_view(request):
    return render(request, 'a_app/about_us.html')

def contacts_view(request):
    return render(request, 'a_pp/contacts.html')

def feedback_view(request):
    return render(request, 'a_pp/feedback.html')

def payment_delivery_view(request):
    return render(request, 'a_pp/payment_delivery.html')

