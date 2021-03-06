from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from urllib.parse import unquote
from .models import Movie, Rating
from .serializers import MovieSerializer, MovieListSerializer, RatingSerializer

from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes


#movies/
@api_view(['GET'])
def movie_list(request):
    movies = Movie.objects.all()
    query = request.GET.get("q")
    if query:
        unquote(query)
        movies = movies.filter(Q(title__icontains=query)).distinct()
    serializer = MovieListSerializer(movies, many=True)
    return Response(serializer.data)
    
@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieSerializer(movie)
    return Response(serializer.data)

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticated])
def rating_get_create(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    def rating_get(request, movie_pk):
        rating = Rating.objects.filter(user=request.user, movie=movie)
        serializer = RatingSerializer(rating, many=True)
        return Response(serializer.data)

    def rating_create(request, movie_pk):
        serializer = RatingSerializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(user=request.user, movie=movie)  # NOT NULL CONSTRAINT FAILED
            return Response(serializer.data)

    if request.method == 'POST':
        return rating_create(request, movie_pk)
    else:
        return rating_get(request, movie_pk)

@api_view(['PUT', 'DELETE'])
@permission_classes([IsAuthenticated])
def rating_update_delete(request, movie_pk, rating_pk):
    rating = get_object_or_404(Rating, pk=rating_pk, movie_id=movie_pk)

    # 본인 확인
    if request.user == rating.user:
        # 평점 수정
        if request.method == 'PUT':
            serializer = RatingSerializer(instance=rating, data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return Response({'message': '평점이 수정되었습니다.', 'data': serializer.data})
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        # 평점 삭제
        elif request.method == 'DELETE':
            rating.delete()
            return Response({'message': '성공적으로 삭제되었습니다.'})
    else:
        return Response(serializer.errors, status=status.HTTP_401_UNAUTHORIZED)