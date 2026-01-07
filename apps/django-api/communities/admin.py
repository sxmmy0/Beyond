from django.contrib import admin
from .models import Community, CommunityMember, Post, Comment, Like


class CommunityMemberInline(admin.TabularInline):
    model = CommunityMember
    extra = 1


@admin.register(Community)
class CommunityAdmin(admin.ModelAdmin):
    list_display = ('name', 'sport', 'is_public', 'created_by', 'created_at')
    list_filter = ('is_public', 'sport')
    search_fields = ('name',)
    inlines = [CommunityMemberInline]


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ('author', 'community', 'created_at')
    list_filter = ('community',)
    search_fields = ('content', 'author__email')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('author', 'post', 'created_at')


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ('user', 'post', 'created_at')