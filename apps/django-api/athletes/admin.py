from django.contrib import admin
from .models import Sport, AthleteProfile


@admin.register(Sport)
class SportAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name',)


@admin.register(AthleteProfile)
class AthleteProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'experience_level', 'created_at')
    list_filter = ('experience_level', 'sports')
    search_fields = ('user__email', 'user__username')
    filter_horizontal = ('sports',)