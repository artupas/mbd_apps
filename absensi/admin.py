from django.contrib import admin
from .custom_widgets import CheckboxSelectMultiple
from django import forms
from .models import Absensi,Student

# Register your models here.

class YourModelAdminForm(forms.ModelForm):
    class Meta:
        model = Absensi
        fields = '__all__'
        widgets = {
            'student': CheckboxSelectMultiple(),  # Replace with the actual field name
        }

class SiswaiInline(admin.TabularInline):
    model = Student

class AbsensiAdmin(admin.ModelAdmin):
    form = YourModelAdminForm

admin.site.register(Absensi,AbsensiAdmin)
admin.site.register(Student)