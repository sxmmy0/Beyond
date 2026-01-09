import strawberry
from strawberry import auto
from typing import List, Optional
from athletes.models import Sport, AthleteProfile
from .user import UserType


@strawberry.django.type(Sport)
class SportType:
    id: auto
    name: auto
    description: auto
    icon: auto


@strawberry.django.type(AthleteProfile)
class AthleteProfileType:
    id: auto
    user: UserType
    experience_level: auto
    date_of_birth: auto
    height_cm: auto
    weight_kg: auto
    goals: auto
    injuries: auto
    created_at: auto
    updated_at: auto
    
    @strawberry.django.field
    def sports(self) -> List[SportType]:
        return self.sports.all()