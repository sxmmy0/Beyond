import strawberry
from typing import List, Optional
from workouts.models import Exercise, WorkoutTemplate
from graphql_api.types import ExerciseType, WorkoutTemplateType


@strawberry.type
class WorkoutQueries:
    @strawberry.field
    def exercises(self) -> List[ExerciseType]:
        return Exercise.objects.all()
    
    @strawberry.field
    def exercise(self, id: strawberry.ID) -> Optional[ExerciseType]:
        try:
            return Exercise.objects.get(id=id)
        except Exercise.DoesNotExist:
            return None
    
    @strawberry.field
    def workout_templates(self, public_only: bool = True) -> List[WorkoutTemplateType]:
        if public_only:
            return WorkoutTemplate.objects.filter(is_public=True)
        return WorkoutTemplate.objects.all()
    
    @strawberry.field
    def workout_template(self, id: strawberry.ID) -> Optional[WorkoutTemplateType]:
        try:
            return WorkoutTemplate.objects.get(id=id)
        except WorkoutTemplate.DoesNotExist:
            return None