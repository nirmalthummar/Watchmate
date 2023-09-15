from django.urls import path, include
from movieapp.api.views import (WatchListAV, WatchDetailAV, StreamPlatformAV,
                                StreamPlatformDetailAV, ReviewAV, ReviewDetailAV,
                                ReviewListGAV, ReviewDetailGAV,
                                ReviewListCAV, ReviewDetailCAV,
                                ReviewCreateCAV, StreamPlatformViewset,
                                StreamPlatformModelViewset, UserReview, WatchListSearch)
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('stream', StreamPlatformViewset, basename='stream-platform')
router.register('model-stream', StreamPlatformModelViewset, basename='stream-platform-model-view-set')

urlpatterns = [
    path('list/', WatchListAV.as_view(), name='movie-list'),
    path('list2/search/', WatchListSearch.as_view(), name='movie-search'),
    path('list/<int:pk>/', WatchDetailAV.as_view(), name='movie-details'),
    # path('stream/', StreamPlatformAV.as_view(), name='stream-platform-list'),
    # path('stream/<int:pk>', StreamPlatformDetailAV.as_view(), name='stream-platform-details'),
    path('stream/<int:pk>/create-review/', ReviewCreateCAV.as_view(), name='create-review'),
    path('stream/<int:pk>/reviews/', ReviewListCAV.as_view(), name='review-list'),
    path('stream/reviews/<int:pk>/', ReviewDetailCAV.as_view(), name='review-detail'),

    path('reviews/<str:user>/', UserReview.as_view(), name='user-review'),

    path('', include(router.urls))
]
