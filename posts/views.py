from django.shortcuts import render
import requests
from django.http import HttpResponse
from . import models


def index(request):
    r = requests.get('http://jsonplaceholder.typicode.com/users')
    users = r.json()
    for user in users:
        newuser = models.PostUser()
        newuser.id = user.get('id')
        newuser.name = user.get('name')
        newuser.username = user.get('username')
        newuser.email = user.get('email')
        newuser.phone = user.get('phone')
        newuser.website = user.get('website')

        address = user.get('address')
        user_address = models.Address()
        user_address.street = address.get('street')
        user_address.suite = address.get('suite')
        user_address.city = address.get('city')
        user_address.zipcode = address.get('zipcode')

        geo = address.get('geo')
        address_geo = models.Geo()
        address_geo.lat = geo.get('lat')
        address_geo.lng = geo.get('lng')
        address_geo.save()
        user_address.geo = address_geo
        user_address.save()
        newuser.address = user_address

        company = user.get('company')
        user_company = models.Company()
        user_company.name = company.get('name')
        user_company.catchPhrase = company.get('catchPhrase')
        user_company.bs = company.get('bs')
        user_company.save()
        newuser.company = user_company
        newuser.save()

    return HttpResponse()


# def index(request):
#     r = requests.get('http://jsonplaceholder.typicode.com/users')
#     users = r.json()
#     # print(users)
#     for user in users:
#         newuser = models.PostUser()
#         for key, value in user.items():
#             newuser[key] =
#             print(key, value)
#     return HttpResponse()