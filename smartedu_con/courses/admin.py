from django.contrib import admin
from . models import Course,Category,Tag

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display=('name','available','teacher')
    list_filter= ('available',)
    search_fields= ('name',)
# Register your models here.

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}

@admin.register(Tag) 
class TagAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('name',)}   