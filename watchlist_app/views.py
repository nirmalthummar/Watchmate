# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse
#
#
# def movie_list(request):
#     movies = Movie.objects.all().values()
#     print("Movies...", movies)
#     data = {
#         'movies': list(movies)
#     }
#     return JsonResponse(data)
#
#
# def movie_details(request, pk):
#     movie = Movie.objects.get(id=pk)
#     print("movie is...", movie)
#     data = {
#         'movie': movie.name,
#         'description': movie.description
#     }
#     return JsonResponse(data)
