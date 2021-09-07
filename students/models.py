from django.db import models


GENRES = [
    ('male','MALE'),
    ('femme','FEMME')
]
FORMATION = [
    ('professionnelle','professionnelle'),
    ('academique','academique')
]
# Create your models here.
class Student(models.Model):
    num_ordre= models.CharField(max_length=256)
    name = models.CharField(max_length=256)
    genre = models.CharField(max_length=256,choices=GENRES)
    birthdate=models.DateField()
    nni = models.CharField(max_length=256)
    bac_id = models.CharField(max_length=256)
    num_tel = models.CharField(max_length=256)
    num_whatsapp =models.CharField(max_length=256,null=True,blank=True)
    bac_id = models.CharField(max_length=256,null=True,blank=True)
    bac_type = models.CharField(max_length=256,null=True,blank=True)
    bac_year = models.DateField()
    formation = models.CharField(max_length=256)
    first_inscription= models.DateField()
    level = models.CharField(max_length=256)
    place_of_birth = models.CharField(max_length=256)
    diplomes = models.TextField()
    classes = models.TextField(null=True,blank=True)
    level_justification = models.BooleanField(default=False)
    carte_identite= models.BooleanField(default=False)
    birth = models.BooleanField()
    nombre_de_photo = models.TextField()
    diplome = models.BooleanField(default=True)
    carte_etudiant = models.BooleanField(default=False)
    Bulltins = models.BooleanField(default=False)
    Attestation = models.BooleanField(default=False)
    
    image = models.TextField(null=True,blank=True) 
