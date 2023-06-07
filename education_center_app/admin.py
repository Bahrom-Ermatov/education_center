from django.contrib import admin
from django.contrib.auth.models import Group
from education_center_app.models import Student, Cource, Mark

@admin.register(Student) 
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Cource) 
class CategoryAdmin(admin.ModelAdmin):
    pass

@admin.register(Mark) 
class CategoryAdmin(admin.ModelAdmin):
    pass

