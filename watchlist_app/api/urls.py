from django.urls import path, include
# from watchlist_app.api.views import MovieListAV , MovieDetailAV
# from watchlist_app.api.views import movie_list , movie_detail 
from watchlist_app.api.views import WatchListView,WatchListDetailView ,StreamPlatformView ,StreamPlatformDetailView ,ReviewList, ReviewDetail
urlpatterns = [

    #Class based views for new WatchList and StreamPlatform
    path('list/', WatchListView.as_view(), name='watch-list'),
    path('<int:pk>/', WatchListDetailView.as_view(), name='watch-list-detail'),
    path('platform/', StreamPlatformView.as_view(), name='platform-list'),
    path('platform/<int:pk>', StreamPlatformDetailView.as_view(), name='platform-detail'),

    # using mixins
    # path('review',ReviewList.as_view(), name='review-list'),
    # path('review/<int:pk>/',ReviewDetail.as_view(), name='review-detail'),

    # using concrete api view
    path('platform/<int:pk>/review/',ReviewList.as_view(), name='review-list'),
    path('platform/review/<int:pk>/',ReviewDetail.as_view(), name='review-detail'),

    # Class based urls
    # path('list/', MovieListAV.as_view(),name="movie_list"),
    # path('<int:pk>/', MovieDetailAV.as_view(),name="movie-list"),

    # Function based url
    # path('list/',movie_list , name='movie-list' ),
    # path('<int:pk>/',movie_detail , name='movie-detail' ),


]

