import strawberry
from strawberry import auto
from progress.models import Goal, Streak, Achievement, AthleteAchievement


@strawberry.django.type(Goal)
class GoalType:
    id: auto
    title: auto
    description: auto
    goal_type: auto
    target_value: auto
    current_value: auto
    unit: auto
    deadline: auto
    status: auto
    created_at: auto
    updated_at: auto


@strawberry.django.type(Streak)
class StreakType:
    id: auto
    streak_type: auto
    current_count: auto
    longest_count: auto
    last_activity_date: auto


@strawberry.django.type(Achievement)
class AchievementType:
    id: auto
    name: auto
    description: auto
    icon: auto