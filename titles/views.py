from django.db.models import Avg, F
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters, mixins, viewsets
from rest_framework.permissions import SAFE_METHODS

from titles.filters import TitleFilter
from .models import Category, Genre, Title
from users.permissions import IsAdminUserOrReadOnly
from .serializers import CategorySerializer, GenreSerializer, ListTitleSerializer, CreateTitleSerializer


class ListCreateDestroyAPIView(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    mixins.DestroyModelMixin,
    viewsets.GenericViewSet
):
    pass


class CategoryViewSet(ListCreateDestroyAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class GenreViewSet(ListCreateDestroyAPIView):
    queryset = Genre.objects.all()
    serializer_class = GenreSerializer
    lookup_field = 'slug'
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)


class TitleViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    permission_classes = (IsAdminUserOrReadOnly,)
    filter_backends = (DjangoFilterBackend,)
    filter_class = TitleFilter

    def get_queryset(self):
        return super().get_queryset().annotate(rating=Avg(F('reviews__score')))

    def get_serializer_class(self):
        if self.request.method in SAFE_METHODS:
            return ListTitleSerializer
        return CreateTitleSerializer
