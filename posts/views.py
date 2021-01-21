from django.shortcuts import render
import requests
from . import models


def get_users(url):
    r = requests.get(url)
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


def get_posts(url):
    r = requests.get(url)
    posts = r.json()
    for post in posts:
        new_post = models.Post()
        user_id = post.get('userId')
        user = models.PostUser.objects.get(id=user_id)
        new_post.user = user
        new_post.id = post.get('id')
        new_post.title = post.get('title')
        new_post.body = post.get('body')
        new_post.save()


def index(request):
    get_users('http://jsonplaceholder.typicode.com/users')
    get_posts('http://jsonplaceholder.typicode.com/posts')

    posts = models.Post.objects.all()
    return render(request, "index.html", {"posts": posts})
