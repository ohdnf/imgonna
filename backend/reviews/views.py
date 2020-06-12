from django.shortcuts import render, get_object_or_404
from .models import Review, ReviewComment
from .serializers import ReviewSerializer, ReviewListSerializer, ReviewCommentSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


#reviews/
@api_view(['GET', 'POST'])
def review_list_create(request):
    def review_list(request):
        reviews = Review.objects.all()
        serializer = ReviewListSerializer(reviews, many=True)
        return Response(serializer.data)

    @permission_classes([IsAuthenticated])
    def review_create(request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user)  # NOT NULL CONSTRAINT FAILED
            return Response(serializer.data)
    
    if request.method == 'POST':
        return review_create(request)
    else:
        return review_list(request)


#reviews/1
@api_view(['GET', 'PUT', 'DELETE'])
def review_detail_update_delete(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)

    # 글 상세
    if request.method == 'GET':
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    # 본인 확인
    if request.user == review.user:
        # 글을 수정(찾아 바꾼다)
        if request.method == 'PUT':
            serializer = ReviewSerializer(data=request.data, instance=review)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': '글이 수정되었습니다.', 'data': serializer.data})
            return Response({'message': '뭔가 잘 못 되었습니다.', 'data': serializer.data})

        # 글을 삭제
        elif request.method == 'DELETE':
            review.delete()
            return Response({'message': '글이 삭제되었습니다.'})
    else:
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_create(request, review_pk):
    review = get_object_or_404(Review, pk=review_pk)
    serializer = ReviewCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(user=request.user, review=review)  # NOT NULL CONSTRAINT FAILED
        return Response(serializer.data)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def comment_update_delete(request, review_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk, review_id=review_pk)

    # 본인 확인
    if request.user == comment.user:
        # 댓글 수정
        if request.method == 'POST':
            serializer = ReviewCommentSerializer(comment, data=request.data)
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