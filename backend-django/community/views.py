from .models import Article, Comment
from django.shortcuts import get_object_or_404
from django.db.models import Count, Q
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import (
    ArticleListSerializer, 
    ArticleSerializer, 
    CommentSerializer,
    )


@api_view(['GET'])
def category(request, category_pk):
    # 전체 게시글
    if category_pk == 1:
        articles = Article.objects.annotate(
            comment_count=Count('comments', distinct=True),
            like_count=Count('like_users', distinct=True)
        ).order_by('pk')
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)
    # 공지사항
    if category_pk == 2:
        articles = Article.objects.annotate(
            comment_count=Count('comments', distinct=True),
            like_count=Count('like_users', distinct=True)
        ).order_by('pk')
        article = articles.filter(category='공지사항')
        serializer = ArticleListSerializer(article, many=True)
        return Response(serializer.data)
    # 자유게시판
    if category_pk == 3:
        articles = Article.objects.annotate(
            comment_count=Count('comments', distinct=True),
            like_count=Count('like_users', distinct=True)
        ).order_by('pk')
        article = articles.filter(category='자유게시판')
        serializer = ArticleListSerializer(article, many=True)
        return Response(serializer.data)
    # 질문게시판
    if category_pk == 4:
        articles = Article.objects.annotate(
            comment_count=Count('comments', distinct=True),
            like_count=Count('like_users', distinct=True)
        ).order_by('pk')
        article = articles.filter(category='질문게시판')
        serializer = ArticleListSerializer(article, many=True)
        return Response(serializer.data)
    else:
        return Response("카테고리의 선택을 잘못했습니다.", status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def search(request):
    article_list = Article.objects.all()
    search = request.GET.get('search','')
    if search:
        search_list = article_list.filter(
        Q(title__icontains = search) | #제목
        Q(content__icontains = search) |  #내용
        Q(category__icontains = search) |
        Q(user__nickname__icontains = search) #글쓴이
        )
        serializer = ArticleSerializer(search_list, many=True)
        return Response(serializer.data)
    return Response('해당 내용이 없습니다.', status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def article_create(request):
    serializer = ArticleSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_or_update_or_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    if request.method == 'GET':
        article.hits += 1 
        article.save()
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    if request.method == 'PUT':
        if request.user == article.user:
            serializer = ArticleSerializer(instance=article, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response(serializer.data)

    if request.method == 'DELETE':
        if request.user == article.user:
            article.delete()
            return Response('게시글이 삭제되었습니다.', status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def like_article(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    user = request.user
    if article.user.pk != user.pk:
        if article.like_users.filter(pk=user.pk).exists():
            article.like_users.remove(user)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
        else:
            article.like_users.add(user)
            serializer = ArticleSerializer(article)
            return Response(serializer.data)
    return Response("자신의 게시물에는 좋아요를 할 수 없습니다.",status=status.HTTP_400_BAD_REQUEST)


@api_view(['POST'])
def create_comment(request, article_pk):
    user = request.user
    article = get_object_or_404(Article, pk=article_pk)
    
    serializer = CommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(article = article, user=user)

        comments = article.comments.all()
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['PUT', 'DELETE'])
def comment_update_or_delete(request, article_pk, comment_pk):
    article = get_object_or_404(Article, pk=article_pk)
    comment = get_object_or_404(Comment, pk=comment_pk)

    if request.method == 'PUT':
        if request.user == comment.user:
            serializer = CommentSerializer(instance=comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                comments = article.comments.all()
                serializer = CommentSerializer(comments, many=True)
                return Response(serializer.data)

    if request.method == 'DELETE':
        if request.user == comment.user:
            comment.delete()
            comments = article.comments.all()
            serializer = CommentSerializer(comments, many=True)
            return Response(serializer.data)

