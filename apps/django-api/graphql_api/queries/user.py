import strawberry
from typing import Optional
from strawberry.types import Info
from users.models import User
from graphql_api.types import UserType


@strawberry.type
class UserQueries:
    @strawberry.field
    def me(self, info: Info) -> Optional[UserType]:
        user = info.context.request.user
        if user.is_authenticated:
            return user
        return None
    
    @strawberry.field
    def user(self, id: strawberry.ID) -> Optional[UserType]:
        try:
            return User.objects.get(id=id)
        except User.DoesNotExist:
            return None