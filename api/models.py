from django.db import models

# Create your models here.


class User(models.Model):
    id = models.CharField(max_length=255, primary_key=True)
    nama = models.CharField(max_length=255)
    nik = models.CharField(max_length=16)
    password = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    departemen = models.CharField(max_length=255)


class Lapor(models.Model):
    tanggal = models.DateTimeField()
    judul = models.CharField(max_length=50)
    deskripsi = models.CharField(max_length=255)
    lokasi = models.CharField(max_length=255)
    status = models.CharField(max_length=255)
    url = models.CharField(max_length=255)
    url_progress = models.CharField(max_length=255)
    kategori = models.CharField(max_length=255)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)
    # Create / Insert / Add - POST
    # Retrieve /  Fetch - GET
    # Update / Edit - PUT
    # Delete / Remove - DELETE
