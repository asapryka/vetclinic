from django.contrib import admin
from .models import Clinic, User, Animal, Record

admin.site.register(Clinic)
admin.site.register(User)
admin.site.register(Animal)
admin.site.register(Record)
