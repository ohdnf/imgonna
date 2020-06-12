from django.shortcuts import render, get_object_or_404
from .models import Article, ArticleComment
from .serializers import ArticleSerializer, ArticleListSerializer, ArticleCommentSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


#articles/
@api_view(['GET', 'POST'])
def article_list_create(request):
    def article_list(request):
        articles = Article.objects.all()
        serializer = ArticleListSerializer(articles, many=True)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def article_create(request):
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)  # NOT NULL CONSTRAINT FAILED
            return Response(serializer.data)
    
    if request.method == 'POST':
        return article_create(request)
    else:
        return article_list(request)


#articles/1
@api_view(['GET', 'PUT', 'DELETE'])
def article_detail_update_delete(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)

    # 글 상세
    if request.method == 'GET':
        serializer = ArticleSerializer(article)
        return Response(serializer.data)

    # 본인 확인
    if request.user == article.user:
        # 글을 수정(찾아 바꾼다)
        if request.method == 'PUT':
            serializer = ArticleSerializer(data=request.data, instance=article)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': '글이 수정되었습니다.', 'data': serializer.data})
            return Response({'message': '뭔가 잘 못 되었습니다.', 'data': serializer.data})

        # 글을 삭제
        elif request.method == 'DELETE':
            article.delete()
            return Response({'message': '글이 삭제되었습니다.'})
    else:
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, article_pk):
    article = get_object_or_404(Article, pk=article_pk)
    serializer = ArticleCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, article=article)  # NOT NULL CONSTRAINT FAILED
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, article_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, article_id=article_pk)

    # 본인 확인
    if request.user == comment.user:
        # 댓글 수정
        if request.method == 'POST':
            serializer = ArticleCommentSerializer(comment, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': '댓글이 수정되었습니다.', 'data': serializer.data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 댓글 삭제
        elif request.method == 'DELETE':
            comment.delete()
            return Response({'message': '성공적으로 삭제되었습니다.'})
    else:
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)