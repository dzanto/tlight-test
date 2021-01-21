from django.db import models


class Geo(models.Model):
    lat = models.CharField(max_length=50)
    lng = models.CharField(max_length=50)


class Company(models.Model):
    name = models.CharField(max_length=50)
    catchPhrase = models.CharField(max_length=50)
    bs = models.CharField(max_length=50)


class Address(models.Model):
    street = models.CharField(max_length=100)
    suite = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    zipcode = models.CharField(max_length=30)
    geo = models.ForeignKey(Geo, on_delete=models.CASCADE)



class PostUser(models.Model):
    name = models.CharField(max_length=100)
    username = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    address = models.ForeignKey(Address, on_delete=models.CASCADE)
    phone = models.CharField(max_length=50)
    website = models.CharField(max_length=50)
    company = models.ForeignKey(Company, on_delete=models.CASCADE)

class Post(models.Model):
    user = models.ForeignKey(PostUser, on_delete=models.CASCADE)
    title = models.CharField(max_length=300)
    body = models.TextField()
