import uuid
from django.db import models
from django.conf import settings


class Goal(models.Model):
    """Athlete goals to track."""
    
    class GoalType(models.TextChoices):
        STRENGTH = 'strength', 'Strength'
        ENDURANCE = 'endurance', 'Endurance'
        WEIGHT = 'weight', 'Weight'
        HABIT = 'habit', 'Habit'
        CUSTOM = 'custom', 'Custom'
    
    class Status(models.TextChoices):
        ACTIVE = 'active', 'Active'
        COMPLETED = 'completed', 'Completed'
        ABANDONED = 'abandoned', 'Abandoned'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    athlete = models.ForeignKey('athletes.AthleteProfile', on_delete=models.CASCADE, related_name='tracked_goals')
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    goal_type = models.CharField(max_length=20, choices=GoalType.choices, default=GoalType.CUSTOM)
    target_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    current_value = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    unit = models.CharField(max_length=50, blank=True)  # "kg", "miles", "days"
    deadline = models.DateField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.ACTIVE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.athlete.user.email} - {self.title}"


class Streak(models.Model):
    """Track consistency streaks."""
    
    class StreakType(models.TextChoices):
        WORKOUT = 'workout', 'Workout'
        LOGIN = 'login', 'Login'
        GOAL = 'goal', 'Goal'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    athlete = models.ForeignKey('athletes.AthleteProfile', on_delete=models.CASCADE, related_name='streaks')
    streak_type = models.CharField(max_length=20, choices=StreakType.choices)
    current_count = models.PositiveIntegerField(default=0)
    longest_count = models.PositiveIntegerField(default=0)
    last_activity_date = models.DateField(null=True, blank=True)
    
    class Meta:
        unique_together = ['athlete', 'streak_type']


class Achievement(models.Model):
    """Badges and achievements."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)
    criteria = models.JSONField(default=dict)  # Logic for earning
    
    def __str__(self):
        return self.name


class AthleteAchievement(models.Model):
    """Achievements earned by athletes."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    athlete = models.ForeignKey('athletes.AthleteProfile', on_delete=models.CASCADE, related_name='achievements')
    achievement = models.ForeignKey(Achievement, on_delete=models.CASCADE)
    earned_at = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        unique_together = ['athlete', 'achievement']