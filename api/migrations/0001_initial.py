# Generated by Django 3.1.7 on 2022-02-27 13:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Organization',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=500)),
                ('fax_number', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Employee',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('employee_ssn', models.CharField(max_length=100)),
                ('employee_name', models.CharField(max_length=50)),
                ('contact_number', models.IntegerField(max_length=50)),
                ('organization', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='api.organization')),
            ],
        ),
    ]