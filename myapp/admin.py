from django.contrib import admin
from .models import Resume

@admin.register(Resume)
class ResumeModelAdmin(admin.ModelAdmin):
 list_display = ['id', 'name', 'dob', 'gender', 'city', 'pin', 'locality', 'state', 'mobile', 'job_city', 'profile_image', 'my_file']
