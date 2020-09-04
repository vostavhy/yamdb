from django.core import validators
from django.db import models
from titles.models import Title
from users.models import User


class Review(models.Model):
    text = models.TextField()
    title = models.ForeignKey(Title, on_delete=models.CASCADE, related_name='reviews')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    score = models.PositiveSmallIntegerField(validators=[
        validators.MinValueValidator(1, message='оценка не может быть меньше 1'),
        validators.MaxValueValidator(10, message='оценка не может быть больше 10'), ])
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True, db_index=True)


class Comment(models.Model):
    text = models.TextField()
    review = models.ForeignKey(Review, on_delete=models.CASCADE, related_name='comments')
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    pub_date = models.DateTimeField('Дата публикации', auto_now_add=True, db_index=True)
