from django.urls import include, path
from rest_framework.routers import DefaultRouter

from .views import (
    CommentViewSet,
    ReviewViewSet,
)

router_v1 = DefaultRouter()
router_v1.register(r'titles/(?P<title_id>\d+)/reviews', ReviewViewSet)
router_v1.register(r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments', CommentViewSet)

urlpatterns = [
    path('v1/', include(router_v1.urls)),
]
