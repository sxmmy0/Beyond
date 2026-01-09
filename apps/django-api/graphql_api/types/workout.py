import strawberry
from strawberry import auto
from typing import List, Optional
from workouts.models import Exercise, WorkoutTemplate, WorkoutExercise
from .user import UserType


@strawberry.django.type(Exercise)
class ExerciseType:
    id: auto
    name: auto
    description: auto
    instructions: auto
    muscle_groups: auto
    equipment: auto
    difficulty: auto
    video_url: auto
    created_at: auto


@strawberry.django.type(WorkoutExercise)
class WorkoutExerciseType:
    id: auto
    exercise: ExerciseType
    order: auto
    sets: auto
    reps: auto
    rest_seconds: auto
    notes: auto


@strawberry.django.type(WorkoutTemplate)
class WorkoutTemplateType:
    id: auto
    name: auto
    description: auto
    created_by: Optional[UserType]
    estimated_duration_minutes: auto
    difficulty: auto
    is_public: auto
    created_at: auto
    updated_at: auto
    
    @strawberry.django.field
    def exercises(self) -> List[WorkoutExerciseType]:
        return self.exercises.all()