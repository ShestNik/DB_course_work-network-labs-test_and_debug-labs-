# Generated by Django 3.0.6 on 2020-05-27 20:51

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('description', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.TextField()),
                ('last_name', models.TextField()),
                ('date_of_birth', models.DateField(blank=True, null=True)),
                ('email', models.TextField(null=True)),
                ('phone_num', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Lot',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.TextField()),
                ('start_price', models.FloatField(validators=[django.core.validators.MinValueValidator(0.01)])),
                ('cur_price', models.FloatField(null=True)),
                ('timeout', models.TimeField(null=True)),
                ('timer', models.IntegerField(null=True)),
                ('is_sold', models.BooleanField(default=False, null=True)),
                ('link1', models.TextField(null=True)),
                ('category_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='auction.Category')),
                ('cur_customer_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='customer', to=settings.AUTH_USER_MODEL)),
                ('dj_owner_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='owner', to=settings.AUTH_USER_MODEL)),
                ('owner_id', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='owner', to='auction.User')),
            ],
        ),
    ]
