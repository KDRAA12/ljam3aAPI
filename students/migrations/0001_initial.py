# Generated by Django 3.1.4 on 2021-09-05 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_ordre', models.CharField(max_length=256)),
                ('name', models.CharField(max_length=256)),
                ('genre', models.CharField(choices=[('male', 'MALE'), ('femme', 'FEMME')], max_length=256)),
                ('birthdate', models.DateField()),
                ('nni', models.CharField(max_length=256)),
                ('num_tel', models.CharField(max_length=256)),
                ('num_whatsapp', models.CharField(max_length=256)),
                ('bac_id', models.CharField(max_length=256)),
                ('bac_type', models.CharField(max_length=256)),
                ('bac_year', models.DateField()),
                ('formation', models.CharField(max_length=256)),
                ('first_inscription', models.DateField()),
                ('level', models.CharField(max_length=256)),
                ('inscription_date', models.DateField()),
                ('place_of_birth', models.CharField(max_length=256)),
                ('diplomes', models.TextField()),
                ('level_justification', models.BooleanField(default=False)),
                ('carte_identite', models.BooleanField(default=False)),
                ('birth', models.BooleanField()),
                ('nombre_de_photo', models.TextField()),
                ('diplome', models.BooleanField(default=True)),
                ('carte_etudiant', models.BooleanField(default=False)),
                ('Bulltins', models.BooleanField(default=False)),
                ('Attestation', models.BooleanField(default=False)),
                ('image', models.TextField()),
            ],
        ),
    ]
