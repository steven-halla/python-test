# Generated by Django 3.1.1 on 2020-11-16 21:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_test_django', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Trip',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('destination', models.CharField(max_length=20)),
                ('startdate', models.DateTimeField()),
                ('enddate', models.DateTimeField()),
                ('plan', models.CharField(max_length=30)),
                ('uploaded_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trip_uploaded', to='app_test_django.user')),
            ],
        ),
    ]