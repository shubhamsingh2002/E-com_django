# Generated by Django 3.1.7 on 2021-05-20 14:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.CreateModel(
            name='Orders',
            fields=[
                ('Order_id', models.AutoField(primary_key=True, serialize=False)),
                ('item_json', models.CharField(max_length=5000)),
                ('name', models.CharField(max_length=90)),
                ('email', models.CharField(max_length=110)),
                ('address', models.CharField(max_length=150)),
                ('city', models.CharField(max_length=150)),
                ('state', models.CharField(max_length=150)),
                ('zip_code', models.CharField(max_length=150)),
            ],
        ),
    ]
