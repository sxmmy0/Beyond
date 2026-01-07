import uuid
from django.db import models
from django.conf import settings


class Exercise(models.Model):
    """Individual exercises in the library."""
    
    class Difficulty(models.TextChoices):
        BEGINNER = 'beginner', 'Beginner'
        INTERMEDIATE = 'intermediate', 'Intermediate'
        ADVANCED = 'advanced', 'Advanced'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    instructions = models.TextField(blank=True)
    muscle_groups = models.JSONField(default=list)  # ["chest", "triceps"]
    equipment = models.JSONField(default=list)  # ["barbell", "bench"]
    difficulty = models.CharField(max_length=20, choices=Difficulty.choices, default=Difficulty.BEGINNER)
    video_url = models.URLField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name


class WorkoutTemplate(models.Model):
    """Reusable workout templates."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.SET_NULL,
        null=True,
        related_name='workout_templates'
    )
    estimated_duration_minutes = models.PositiveIntegerField(default=60)
    difficulty = models.CharField(max_length=20, choices=Exercise.Difficulty.choices, default=Exercise.Difficulty.BEGINNER)
    is_public = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name


class WorkoutExercise(models.Model):
    """Exercises within a workout template (junction table)."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    workout = models.ForeignKey(WorkoutTemplate, on_delete=models.CASCADE, related_name='exercises')
    exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE)
    order = models.PositiveIntegerField(default=0)
    sets = models.PositiveIntegerField(default=3)
    reps = models.CharField(max_length=50, default="10")  # Can be "10" or "8-12" or "AMRAP"
    rest_seconds = models.PositiveIntegerField(default=60)
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['order']


class TrainingPlan(models.Model):
    """Multi-week training plans assigned to athletes."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    athlete = models.ForeignKey('athletes.AthleteProfile', on_delete=models.CASCADE, related_name='training_plans')
    coach = models.ForeignKey('coaches.CoachProfile', on_delete=models.SET_NULL, null=True, blank=True, related_name='assigned_plans')
    start_date = models.DateField()
    end_date = models.DateField()
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return f"{self.name} - {self.athlete.user.email}"


class ScheduledWorkout(models.Model):
    """Workouts scheduled on specific days within a training plan."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    training_plan = models.ForeignKey(TrainingPlan, on_delete=models.CASCADE, related_name='scheduled_workouts')
    workout_template = models.ForeignKey(WorkoutTemplate, on_delete=models.CASCADE)
    scheduled_date = models.DateField()
    notes = models.TextField(blank=True)
    
    class Meta:
        ordering = ['scheduled_date']


class WorkoutSession(models.Model):
    """Completed workout sessions (actual performance data)."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    athlete = models.ForeignKey('athletes.AthleteProfile', on_delete=models.CASCADE, related_name='workout_sessions')
    scheduled_workout = models.ForeignKey(ScheduledWorkout, on_delete=models.SET_NULL, null=True, blank=True)
    workout_template = models.ForeignKey(WorkoutTemplate, on_delete=models.SET_NULL, null=True)
    started_at = models.DateTimeField()
    completed_at = models.DateTimeField(null=True, blank=True)
    notes = models.TextField(blank=True)
    rating = models.PositiveIntegerField(null=True, blank=True)  # 1-5 how it felt
    created_at = models.DateTimeField(auto_now_add=True)