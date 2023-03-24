# Generated by Django 4.1.7 on 2023-03-22 22:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('property', '0001_initial'),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommentUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TextField()),
                ('reply', models.PositiveBigIntegerField(default=0)),
                ('host', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commentuser_host', to='account.account')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentuser_user', to='account.account')),
            ],
        ),
        migrations.CreateModel(
            name='CommentProperty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('comment', models.TimeField()),
                ('reply', models.PositiveBigIntegerField(default=0)),
                ('property', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='commentproperty_property', to='property.property')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='commentproperty_user', to='account.account')),
            ],
        ),
    ]