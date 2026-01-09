import strawberry
from strawberry import auto
from typing import Optional
from users.models import User


@strawberry.django.type(User)
class UserType:
    id: auto
    email: auto
    username: auto
    role: auto
    bio: auto
    created_at: auto
    updated_at: auto


@strawberry.type
class AuthPayload:
    user: UserType
    token: str


@strawberry.input
class LoginInput:
    email: str
    password: str


@strawberry.input
class RegisterInput:
    email: str
    username: str
    password: str