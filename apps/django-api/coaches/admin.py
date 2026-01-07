from django.contrib import admin
from .models import CoachProfile, CoachAthleteRelationship


@admin.register(CoachProfile)
class CoachProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'years_experience', 'is_verified', 'created_at')
    list_filter = ('is_verified', 'specialties')
    search_fields = ('user__email', 'user__username')
    filter_horizontal = ('specialties',)


@admin.register(CoachAthleteRelationship)
class CoachAthleteRelationshipAdmin(admin.ModelAdmin):
    list_display = ('coach', 'athlete', 'status', 'started_at')
    list_filter = ('status',)