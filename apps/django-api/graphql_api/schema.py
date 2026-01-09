import strawberry
from strawberry.django.views import GraphQLView
from .queries import UserQueries, WorkoutQueries
from .mutations import AuthMutations


@strawberry.type
class Query(UserQueries, WorkoutQueries):
    pass


@strawberry.type
class Mutation(AuthMutations):
    pass


schema = strawberry.Schema(query=Query, mutation=Mutation)