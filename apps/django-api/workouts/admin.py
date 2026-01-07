from django.contrib import admin
from .models import (
    Exercise, WorkoutTemplate, WorkoutExercise,
    TrainingPlan, ScheduledWorkout, WorkoutSession
)


@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'created_at')
    list_filter = ('difficulty',)
    search_fields = ('name', 'description')


class WorkoutExerciseInline(admin.TabularInline):
    model = WorkoutExercise
    extra = 1


@admin.register(WorkoutTemplate)
class WorkoutTemplateAdmin(admin.ModelAdmin):
    list_display = ('name', 'difficulty', 'estimated_duration_minutes', 'is_public', 'created_by')
    list_filter = ('difficulty', 'is_public')
    search_fields = ('name',)
    inlines = [WorkoutExerciseInline]


@admin.register(TrainingPlan)
class TrainingPlanAdmin(admin.ModelAdmin):
    list_display = ('name', 'athlete', 'coach', 'start_date', 'end_date', 'is_active')
    list_filter = ('is_active',)
    search_fields = ('name', 'athlete__user__email')


@admin.register(ScheduledWorkout)
class ScheduledWorkoutAdmin(admin.ModelAdmin):
    list_display = ('workout_template', 'training_plan', 'scheduled_date')
    list_filter = ('scheduled_date',)


@admin.register(WorkoutSession)
class WorkoutSessionAdmin(admin.ModelAdmin):
    list_display = ('athlete', 'workout_template', 'started_at', 'completed_at', 'rating')
    list_filter = ('rating',)