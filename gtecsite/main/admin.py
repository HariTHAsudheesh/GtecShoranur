from django.contrib import admin
from .models import Course, Trainer,Category

admin.site.register(Category)

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title',)

@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('name', 'role')
