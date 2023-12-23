from django.db import models
from django.contrib.auth.models import User
import uuid

KELOMPOK = (
    (1,"SD KELOMPOK 1"),
    (2,"SD KELOMPOK 2"),
    (3,"SD GELOMBANG 2"),
    (3,"SMP - SMA"),
)

# Create your models here.

class Student (models.Model):
    '''Menyimpan data anak didik'''
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    nama_lengkap = models.CharField(max_length=250)
    nama_panggilan = models.CharField(max_length=50)
    status = models.BooleanField()
    umur = models.PositiveSmallIntegerField()
    kelompok = models.SmallIntegerField(choices=KELOMPOK)
    telp_pribadi = models.IntegerField()
    telp_orangtua = models.IntegerField()
    sekolah = models.CharField(max_length=200)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '%s' % self.nama_panggilan
        

class Absensi (models.Model):
    '''class untuk menampung absensi pelatih'''
    id = models.UUIDField(primary_key=True,default=uuid.uuid4,editable=False,unique=True)
    pelatih = models.ForeignKey(User,on_delete=models.PROTECT)
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    tgl_latihan = models.DateTimeField()
    materi_latihan = models.TextField()
    kendala = models.TextField(blank=True)
    student = models.ManyToManyField(Student,related_name="Siswa_Absen")

    def __str__(self):
        return "%s" %self.id