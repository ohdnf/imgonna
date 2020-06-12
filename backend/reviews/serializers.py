from rest_framework import serializers
from accounts.serializers import UserSerializer
from .models import Review, ReviewComment


class ReviewListSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Review
        fields = ('id', 'title', 'user',)


class ReviewSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = Review
        fields = '__all__'
        # read_only_fields = ('id', 'user', 'created_at', 'updated_at')


class ReviewCommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(required=False)
    created_at = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S")

    class Meta:
        model = ReviewComment
        fields = '__all__'
        # read_only_fields = ('id', 'user', 'created_at', 'updated_at')
