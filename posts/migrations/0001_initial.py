# Generated by Django 3.1.5 on 2021-01-21 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Address',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100)),
                ('suite', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('zipcode', models.CharField(max_length=30)),
                ('phone', models.CharField(max_length=50)),
                ('website', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('catchPhrase', models.CharField(max_length=50)),
                ('bs', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Geo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('lat', models.CharField(max_length=50)),
                ('lng', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='PostUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('username', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('address', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.address')),
            ],
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=300)),
                ('body', models.TextField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.postuser')),
            ],
        ),
        migrations.AddField(
            model_name='address',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.company'),
        ),
        migrations.AddField(
            model_name='address',
            name='geo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='posts.geo'),
        ),
    ]
