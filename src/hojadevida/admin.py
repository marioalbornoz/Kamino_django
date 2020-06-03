from django.contrib import admin
from .models import Curriculum

# Register your models here.

class CurriculumAdmin(admin.ModelAdmin):
    readonly_fields = ('created', 'updated')
    list_display = ['__str__', 'user']
    search_fields = ['user__username','user__email']
    class Meta:
        model = Curriculum

admin.site.register(Curriculum, CurriculumAdmin)