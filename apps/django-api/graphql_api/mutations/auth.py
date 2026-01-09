import strawberry
from strawberry.types import Info
from django.contrib.auth import authenticate, login, logout
from users.models import User
from graphql_api.types import UserType, AuthPayload, LoginInput, RegisterInput


@strawberry.type
class AuthMutations:
    @strawberry.mutation
    def register(self, info: Info, input: RegisterInput) -> UserType:
        # Check if user already exists
        if User.objects.filter(email=input.email).exists():
            raise Exception("A user with this email already exists")
        
        if User.objects.filter(username=input.username).exists():
            raise Exception("A user with this username already exists")
        
        # Create user
        user = User.objects.create_user(
            email=input.email,
            username=input.username,
            password=input.password,
        )
        
        # Log them in
        login(info.context.request, user)
        
        return user
    
    @strawberry.mutation
    def login(self, info: Info, input: LoginInput) -> UserType:
        user = authenticate(
            info.context.request,
            username=input.email,  # We use email as username
            password=input.password,
        )
        
        if user is None:
            raise Exception("Invalid email or password")
        
        login(info.context.request, user)
        return user
    
    @strawberry.mutation
    def logout(self, info: Info) -> bool:
        logout(info.context.request)
        return True