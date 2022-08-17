from . import views
from django.urls import path

app_name = 'community'

urlpatterns = [
    # 커뮤니티
    # 게시판 카테고리별로 보기
    path('<int:category_pk>/', views.category),

    # 게시글 검색
    path('search/', views.search),
    
    # 게시글 쓰기
    path('article/', views.article_create),

    # 게시글 보기, 수정, 삭제
    path('article/<int:article_pk>/', views.article_detail_or_update_or_delete),

    # 게시글 좋아요
    path('article/<int:article_pk>/like/', views.like_article),
    
    #댓글
    # 댓글 달기
    path('article/<int:article_pk>/comments/', views.create_comment),
    
    # 댓글 수정 및 삭제
    path('article/<int:article_pk>/comments/<int:comment_pk>/', views.comment_update_or_delete),
    
]
