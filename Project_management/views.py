from django.shortcuts import render
from . import models


# Create your views here.
def common_data(request):
    return {'common_data': models.Self_details.objects.all(), 'service_items': models.Service_item.objects.all(), }


def index(request):
    about_us_objs = models.About_us.objects.order_by('-datetime').all()

    self_objects = models.Self_details.objects.all()
    service_home = models.Service_name.objects.all()
    service_item = models.Service_item.objects.all()
    team_name = models.Team_name.objects.all()
    team_members = models.Team_members.objects.all()
    print("service_item", service_item)
    return render(request, 'index.html',
                  {'home_context': self_objects, 'about_us': about_us_objs, 'service_home': service_home,
                   'service_items': service_item, 'team_name': team_name, 'team_members': team_members})


def about_us(request):
    context = models.About_us.objects.order_by('-datetime').all()
    print(context)
    return render(request, 'about-us.html', {'about_us': context})


def services(request):
    context = models.About_us.objects.all()
    print(context)
    return render(request, 'our_services.html', {'our_services': context})


def our_services_page(request):
    context = models.Service_item.objects.all()

    return render(request, 'our_services_homepage.html', {'service_items': context})


def services_item(request, id):
    print(id)
    context = models.Service_item.objects.filter(id=id)
    print(context)

    return render(request, 'our_services.html', {'service': context})


def our_team(request):
    print(id)
    context = models.Team_members.objects.all()

    return render(request, 'our_team.html', {'team_members': context})


def contact_us(request):
    if request.method == 'POST':
        name = (request.POST.get('name'))
        email = (request.POST.get('email'))
        subject = (request.POST.get('subject'))
        message = (request.POST.get('message'))
        object = models.Customer_Messages(name=name, email=email, subject=subject, message=message)
        object.save()
    context = {'self_details': models.Self_details.objects.all()}
    return render(request, 'contact_us.html', context)
