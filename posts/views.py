from django.shortcuts import render
import requests
from django.http import HttpResponse
from . import models


# def index(request):
#     r = requests.get('http://jsonplaceholder.typicode.com/users')
#     users = r.json()
#     for user in users:
#         newuser = models.PostUser()
#         newuser.id = user.get('id')
#         newuser.username = user.get('username')
#         newuser.email = user.get('email')
#         newuser.phone = user.get('phone')
#         newuser.website = user.get('website')
#
#         address = user.get('address')
#         user_address = models.Address()
#         for detail in address:
#             user_address.street = detail.get('street')
#             user_address.suite = detail.get('suite')
#             user_address.city = detail.get('city')
#             user_address.zipcode = detail.get('zipcode')
#
#             user_address.street = detail.get('street')
#
#         company = user.get('company')
#         user_company = models.Company()
#         for detail in company:
#             user_company.name = detail.get('name')
#             user_company.catchPhrase = detail.get('catchPhrase')
#             user_company.bs = detail.get('bs')
#         user_company.save()
#         newuser.company = user_company
#
#
#
#     return HttpResponse()


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