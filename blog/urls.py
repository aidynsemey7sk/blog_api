from django.urls import path
from blog.views import (post_list, post_detail, post_new, post_draft_list, post_publish,
                        post_edit, add_comment_to_post, comment_approve, comment_remove,
                        post_remove)

urlpatterns = [
    path('', post_list, name='post_list'),
    path('<str:post_slug>/', post_detail, name='post_detail'),
    path('post/drafts/', post_draft_list, name='post_draft_list'),
    path('post/<str:post_slug>/publish/', post_publish, name='post_publish'),
    path('post/new/', post_new, name='post_new'),
    path('post/<str:post_slug>/edit/', post_edit, name='post_edit'),
    path('post/<pk>/remove/', post_remove, name='post_remove'),
    path('post/<str:post_slug>/comment/', add_comment_to_post, name='add_comment_to_post'),
    path('comment/<int:pk>/approve/', comment_approve, name='comment_approve'),
    path('comment/<int:pk>/remove/', comment_remove, name='comment_remove'),
]
