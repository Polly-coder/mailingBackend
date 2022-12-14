# Generated by Django 4.1 on 2022-08-07 17:08

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('telephon_number', models.IntegerField()),
                ('operator_code', models.IntegerField()),
                ('tag', models.CharField(max_length=256)),
                ('time_zone', models.CharField(max_length=256)),
            ],
        ),
        migrations.CreateModel(
            name='Mailing',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField()),
                ('text', models.CharField(max_length=256)),
                ('filter', models.CharField(max_length=256)),
                ('end_time', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('send_time', models.DateTimeField()),
                ('status', models.CharField(choices=[('S', 'sent'), ('W', 'on the way'), ('R', 'recieved')], max_length=1)),
                ('client_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.client')),
                ('mailing_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailing.mailing')),
            ],
        ),
    ]
