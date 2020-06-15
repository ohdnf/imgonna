from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Article, ArticleComment


class ArticleListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Article
        fields = ('id', 'title', 'user',)


class ArticleSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)   # is_valid()에서 필수여부 검증 PASS
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", required=False)

    class Meta:
        model = Article
        fields = '__all__'
        # read_only_fields = ('id', 'user', 'created_at', 'updated_at')


class ArticleCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = ArticleComment
        fields = '__all__'
        # read_only_fields = ('id', 'user', 'created_at', 'updated_at')
