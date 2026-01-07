from django.contrib import admin
from .models import Goal, Streak, Achievement, AthleteAchievement


@admin.register(Goal)
class GoalAdmin(admin.ModelAdmin):
    list_display = ('title', 'athlete', 'goal_type', 'status', 'deadline')
    list_filter = ('goal_type', 'status')
    search_fields = ('title', 'athlete__user__email')


@admin.register(Streak)
class StreakAdmin(admin.ModelAdmin):
    list_display = ('athlete', 'streak_type', 'current_count', 'longest_count', 'last_activity_date')
    list_filter = ('streak_type',)


@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('name', 'icon')
    search_fields = ('name',)


@admin.register(AthleteAchievement)
class AthleteAchievementAdmin(admin.ModelAdmin):
    list_display = ('athlete', 'achievement', 'earned_at')