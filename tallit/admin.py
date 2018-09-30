from django.contrib import admin

# Register your models here.
from .models import Horse, HorseText, HorseImg, Show, Merit, Breed, Breeder, Owner

admin.site.register(HorseText)
admin.site.register(Show)
admin.site.register(Owner)
admin.site.register(Breeder)
admin.site.register(Breed)
admin.site.register(Merit)
admin.site.register(HorseImg)
@admin.register(Horse)
class HorseAdmin(admin.ModelAdmin):
    search_fields = ['name', 'id', 'stable']