import uuid
from django.db import models
from django.conf import settings
from athletes.models import Sport


class CoachProfile(models.Model):
    """Extended profile for coaches."""
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='coach_profile'
    )
    specialties = models.ManyToManyField(Sport, related_name='coaches', blank=True)
    certifications = models.TextField(blank=True)
    years_experience = models.PositiveIntegerField(default=0)
    hourly_rate = models.DecimalField(max_digits=8, decimal_places=2, null=True, blank=True)
    is_verified = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.user.email} - Coach Profile"


class CoachAthleteRelationship(models.Model):
    """Tracks coach-athlete relationships."""
    
    class Status(models.TextChoices):
        PENDING = 'pending', 'Pending'
        ACTIVE = 'active', 'Active'
        PAUSED = 'paused', 'Paused'
        ENDED = 'ended', 'Ended'
    
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    coach = models.ForeignKey(CoachProfile, on_delete=models.CASCADE, related_name='athletes')
    athlete = models.ForeignKey('athletes.AthleteProfile', on_delete=models.CASCADE, related_name='coaches')
    status = models.CharField(max_length=20, choices=Status.choices, default=Status.PENDING)
    started_at = models.DateTimeField(auto_now_add=True)
    ended_at = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        unique_together = ['coach', 'athlete']