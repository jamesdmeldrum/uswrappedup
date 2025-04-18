# Generated by Django 4.2.7 on 2023-11-18 06:45

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('gamepage', '0008_alter_track_game_delete_gametrack'),
    ]

    operations = [
        migrations.CreateModel(
            name='GameTrack',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('game', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamepage.game')),
                ('track', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='gamepage.track')),
            ],
        ),
    ]
