"""
URL configuration for config project.
"""
from django.contrib import admin
from django.urls import path
from django.views.decorators.csrf import csrf_exempt
from strawberry.django.views import GraphQLView
from graphql_api.schema import schema

graphql_view = csrf_exempt(GraphQLView.as_view(schema=schema))

urlpatterns = [
    path('admin/', admin.site.urls),
    path('graphql/', graphql_view),
    path('graphql', graphql_view),  # Handle requests without trailing slash
]
