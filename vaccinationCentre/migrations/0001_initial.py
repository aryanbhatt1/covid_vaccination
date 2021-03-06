# Generated by Django 4.0.6 on 2022-07-06 10:51

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='home',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('homepage_banner', models.ImageField(null=True, upload_to='home_img/')),
                ('navbar_title', models.CharField(max_length=30, null=True, verbose_name='Title')),
                ('heading', models.CharField(max_length=30, null=True, verbose_name='Heading')),
                ('subheading', models.TextField(null=True, verbose_name='Sub Heading')),
            ],
        ),
        migrations.CreateModel(
            name='VaccinationCentre',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('allowed_candidates', models.IntegerField(default=10, null=True, verbose_name='Allowed Candidates')),
            ],
        ),
    ]
