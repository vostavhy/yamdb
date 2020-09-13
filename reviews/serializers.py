from .models import Review, Comment
from rest_framework import serializers, status


class ReviewSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Review
        fields = ('id', 'text', 'author', 'score', 'pub_date',)

    def validate(self, data):
        # один пользователь может оставлять не более одного отзыва под одной статьёй
        # пользователь, который делает запрос на подписку
        super().validate(data)
        current_user = self.context['request'].user
        title_id = self.context['request'].parser_context['kwargs'].get('title_id')
        review_exists = Review.objects.filter(author=current_user, title_id=title_id).exists()
        method = self.context['request'].stream.method

        if review_exists and method == 'POST':
            raise serializers.ValidationError('не более одного отзыва на статью', code=status.HTTP_400_BAD_REQUEST)

        return data


class CommentSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(slug_field='username', read_only=True)

    class Meta:
        model = Comment
        fields = ('id', 'text', 'author', 'pub_date',)
