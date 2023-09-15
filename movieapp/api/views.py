from django.shortcuts import get_object_or_404
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters

from rest_framework.response import Response
from rest_framework import status
from rest_framework import viewsets
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.generics import GenericAPIView
from rest_framework.mixins import (ListModelMixin, RetrieveModelMixin, CreateModelMixin,
                                   UpdateModelMixin, DestroyModelMixin)
from rest_framework.generics import (CreateAPIView, RetrieveUpdateDestroyAPIView,
                                     ListAPIView)

from rest_framework.throttling import UserRateThrottle, AnonRateThrottle
from movieapp.models import WatchList, StreamPlatform, Review
from movieapp.api.serializers import WatchListSerializer, StreamPlatformSerializer, ReviewSerializer
from movieapp.api.permissions import AdminOrReadOnly, ReviewUserOrReadOnly
from movieapp.api.pagination import WatchListPagination, WatchListCursorPagination


class UserReview(ListAPIView):
    serializer_class = ReviewSerializer

    def get_queryset(self):
        user = self.kwargs.get('user')
        return Review.objects.filter(user__username=user)


class WatchListAV(APIView):

    def get(self, request):
        movies = WatchList.objects.all()
        serializers = WatchListSerializer(movies, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = WatchListSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class WatchDetailAV(APIView):

    def get(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {
                    'error': "Not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = WatchListSerializer(movie)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {
                    'error': "Not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = WatchListSerializer(data=request.data, instance=movie)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            movie = WatchList.objects.get(pk=pk)
        except WatchList.DoesNotExist:
            return Response(
                {
                    'error': "Not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformAV(APIView):

    def get(self, request):
        platforms = StreamPlatform.objects.all()
        serializers = StreamPlatformSerializer(platforms, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class StreamPlatformDetailAV(APIView):

    def get(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(
                {
                    'error': "Not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = StreamPlatformSerializer(platform)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(
                {
                    'error': "Not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = StreamPlatformSerializer(data=request.data, instance=platform)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(
                {
                    'error': "Not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# review using APIView
class ReviewAV(APIView):

    def get(self, request):
        reviews = Review.objects.all()
        serializers = ReviewSerializer(reviews, many=True)
        return Response(serializers.data)

    def post(self, request):
        serializer = ReviewSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class ReviewDetailAV(APIView):

    def get(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response(
                {
                    'error': "Not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = ReviewSerializer(review)
        return Response(serializer.data)

    def put(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response(
                {
                    'error': "Not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = ReviewSerializer(data=request.data, instance=review)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        try:
            review = Review.objects.get(pk=pk)
        except Review.DoesNotExist:
            return Response(
                {
                    'error': "Not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        review.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# Review using GenericAPIView and ModelMixins
class ReviewListGAV(ListModelMixin, CreateModelMixin, GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class ReviewDetailGAV(RetrieveModelMixin, UpdateModelMixin, DestroyModelMixin, GenericAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    def get(self, request, *args, **kwargs):
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        return self.destroy(request, *args, **kwargs)


# Review using concrete APIView
class ReviewListCAV(ListAPIView):
    # queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    permission_classes = [IsAuthenticated]
    # permission_classes = [AdminOrReadOnly]
    # throttle_classes = [UserRateThrottle, AnonRateThrottle]

    # we can also mention scope rate directly
    # throttle_scope = 'review-new'

    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['user__username', 'active']

    # overriding the query method as per the requirement
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        queryset = Review.objects.filter(watchlist=pk)
        return queryset


class ReviewCreateCAV(CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

    # def get_queryset(self):
    #     return Review.objects.all()

    def perform_create(self, serializer):
        pk = self.kwargs.get('pk')
        watchlist = WatchList.objects.get(pk=pk)

        user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist, user=user)

        if review_queryset.exists():
            raise ValidationError("You have already given a review for this movie!")

        if watchlist.number_rating == 0:
            watchlist.avg_rating = serializer.validated_data['rating']

        else:
            watchlist.avg_rating = (watchlist.avg_rating + serializer.validated_data['rating']) / 2

        watchlist.number_rating = watchlist.number_rating + 1
        watchlist.save()

        serializer.save(watchlist=watchlist, user=user)


class ReviewDetailCAV(RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    # permission_classes = [AdminOrReadOnly]
    permission_classes = [ReviewUserOrReadOnly]


class StreamPlatformViewset(viewsets.ViewSet):

    """
        View-set (only difference looks like in API view we have to write separate
        urls and in view-set it will be handled by router)
    """

    def list(self, request):
        queryset = StreamPlatform.objects.all()
        serializer = StreamPlatformSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = StreamPlatformSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def retrieve(self, request, pk):
        queryset = StreamPlatform.objects.all()
        watchlist = get_object_or_404(queryset, pk=pk)
        serializer = StreamPlatformSerializer(watchlist)
        return Response(serializer.data)

    def update(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(
                {
                    'error': "Not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        serializer = StreamPlatformSerializer(data=request.data, instance=platform)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def destroy(self, request, pk):
        try:
            platform = StreamPlatform.objects.get(pk=pk)
        except StreamPlatform.DoesNotExist:
            return Response(
                {
                    'error': "Not Found"
                },
                status=status.HTTP_404_NOT_FOUND
            )
        platform.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class StreamPlatformModelViewset(viewsets.ModelViewSet):

    """
        Model view set is consist of all the mixins
    """
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer


class WatchListSearch(ListAPIView):
    queryset = WatchList.objects.all()
    serializer_class = WatchListSerializer

    # Django filters
    # filter_backends = [DjangoFilterBackend]
    # filterset_fields = ['title', 'platform__name']

    # Django Search
    # filter_backends = [filters.SearchFilter]
    # search_fields = ['title', 'platform__name']

    # Ordering
    # filter_backends = [filters.OrderingFilter]
    # ordering_fields = ['avg_rating']

    # Pagination
    pagination_class = WatchListCursorPagination
