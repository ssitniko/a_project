from django.shortcuts import render



def home_view(request):
    return render(request, 'akorzina/home.html')

def catalog_view(request):
    return render(request, 'akorzina/catalog.html')

def about_us_view(request):
    return render(request, 'akorzina/about_us.html')

def contacts_view(request):
    return render(request, 'akorzina/contacts.html')

def feedback_view(request):
    return render(request, 'akorzina/feedback.html')

def payment_delivery_view(request):
    return render(request, 'akorzina/payment_delivery.html')


def lampshades_view(request):
    return render(request, 'akorzina/catalog/lampshades.html')

def chandeliers_view(request):
    return render(request, 'akorzina/catalog/chandeliers.html')

def mirrors_view(request):
    return render(request, 'akorzina/catalog/mirrors.html')

def other_view(request):
    return render(request, 'akorzina/catalog/other.html')

def pano_view(request):
    return render(request, 'akorzina/catalog/pano.html')