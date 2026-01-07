import uuid
from django.db import models
from django.conf import settings


class Sport(models.Model):
    """Sports that athletes can participate in."""
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True)
    icon = models.CharField(max_length=50, blank=True)  # Icon name/class
    
    def __str__(self):
        return self.name


class AthleteProfile(models.Model):
    """Extended profile for athletes."""
    
    class ExperienceLevel(models.TextChoices):
        BEGINNER = 'beginner', 'Beginner'
        INTERMEDIATE = 'intermediate', 'Intermediate'
        ADVANCED = 'advanced', 'Advanced'
        ELITE = 'elite', 'Elite'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='athlete_profile'
    )
    sports = models.ManyToManyField(Sport, related_name='athletes', blank=True)
    experience_level = models.CharField(
        max_length=20,
        choices=ExperienceLevel.choices,
        default=ExperienceLevel.BEGINNER,
    )
    date_of_birth = models.DateField(null=True, blank=True)
    height_cm = models.PositiveIntegerField(null=True, blank=True)
    weight_kg = models.DecimalField(max_digits=5, decimal_places=2, null=True, blank=True)
    goals = models.TextField(blank=True)  # What they want to achieve
    injuries = models.TextField(blank=True)  # Any injuries to consider
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.email} - Athlete Profile"
        