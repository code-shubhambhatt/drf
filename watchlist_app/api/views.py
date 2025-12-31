from rest_framework.response import Response
from rest_framework import status
from rest_framework.exceptions import ValidationError
# from rest_framework import mixins
from rest_framework import generics
from rest_framework.views import APIView
from rest_framework import viewsets

from watchlist_app.models import WatchList , StreamPlatform , Review
from watchlist_app.api.serializers import (WatchListSerializer , StreamPlatformSerializer , ReviewSerializer)

from django.shortcuts import get_object_or_404
# from rest_framework.decorators import api_view
# from watchlist_app.models import Movie
# from watchlist_app.api.serializers import MovieSerializer

# using viewsets
# class StreamPlatformVS(viewsets.ViewSet):
#     def list(self,request):
#         queryset = StreamPlatform.objects.all()
#         serializer = StreamPlatformSerializer(queryset, many=True)
#         return Response(serializer.data)

#     def retrieve(self, request, pk=None):
#         queryset = StreamPlatform.objects.all()
#         watchlist = get_object_or_404(queryset, pk=pk)
#         serializer = StreamPlatformSerializer(watchlist)
#         return Response(serializer.data)

# Using ModelViewset
class StreamPlatformVS(viewsets.ModelViewSet):
    queryset = StreamPlatform.objects.all()
    serializer_class = StreamPlatformSerializer

# Using concrete view class
 
class ReviewCreate(generics.CreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
    def perform_create(self,serializer):
        pk=self.kwargs['pk']
        watchlist = WatchList.objects.get(pk=pk)
        review_user = self.request.user
        review_queryset = Review.objects.filter(watchlist=watchlist , review_user=review_user)
        if review_queryset.exists():
            raise ValidationError("Review alredy exists for this. Cannot create more than review")

        serializer.save(watchlist= watchlist , review_user=review_user)
        

class ReviewList(generics.ListAPIView):
    # queryset=Review.objects.all()
    serializer_class = ReviewSerializer

    def get_queryset(self):
        watchlist_id = self.kwargs['pk']
        return Review.objects.filter(watchlist_id= watchlist_id)


class ReviewDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset=Review.objects.all()
    serializer_class = ReviewSerializer
    


# Using Mixins

# class ReviewList(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.list(request, *args, **kwargs)

#     def post(self, request, *args, **kwargs):
#         return self.create(request, *args, **kwargs)

# class ReviewDetail(mixins.RetrieveModelMixin,mixins.UpdateModelMixin,mixins.DestroyModelMixin,generics.GenericAPIView):
#     queryset = Review.objects.all()
#     serializer_class = ReviewSerializer

#     def get(self, request, *args, **kwargs):
#         return self.retrieve(request, *args, **kwargs)

#     def put(self, request, *args, **kwargs):
#         return self.update(request, *args, **kwargs)

#     def delete(self, request, *args, **kwargs):
#         return self.destroy(request, *args, **kwargs)

class WatchListView(APIView) :
    def get(self, request):
        item = WatchList.objects.all() 
        serializer = WatchListSerializer(item , many = True)
        return Response(serializer.data)
    
    def post (self, request):
        serializer = WatchListSerializer(data=request.data )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class WatchListDetailView(APIView):
    def get(self, request, pk):
        item = WatchList.objects.get(pk=pk)
        serializer=WatchListSerializer(item)
        return Response(serializer.data , status = status.HTTP_200_OK)
    
    def put(self,request, pk):
        item = WatchList.objects.get(pk=pk)
        serializer = WatchListSerializer(item, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status= status.HTTP_200_OK)
        else :
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,pk):
        item = WatchList.objects.get(pk=pk)
        item.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# class StreamPlatformView(APIView) :
#     def get(self, request):
#         item = StreamPlatform.objects.all() 
#         serializer = StreamPlatformSerializer(item , many = True,context={'request':request})
#         return Response(serializer.data)
    
#     def post (self, request):
#         serializer = StreamPlatformSerializer(data=request.data )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status= status.HTTP_201_CREATED)
#         else:
#             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
# class StreamPlatformDetailView(APIView):
#     def get(self,request , pk) :
#         platform = StreamPlatform.objects.get(pk=pk)
#         serializer = StreamPlatformSerializer(platform ,context={'request': request})
#         return Response(serializer.data , status= status.HTTP_200_OK)
#     def put(self,request , pk):
#         platform = StreamPlatform.objects.get(pk=pk)
#         serializer = StreamPlatformSerializer(platform , data=request.data , context={'request': request})
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data , status=status.HTTP_200_OK)
#         else :
#             return Response(serializer.errors, status = status.HTTP_400_BAD_REQUEST)
#     def delete(self,request,pk):
#         platform = StreamPlatform.objects.get(pk=pk)
#         platform.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

# class MovieListAV(APIView):
#     def get(self, request):
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies , many=True)
#         return Response(serializer.data)

#     def post(self ,request):
#         serializer = MovieSerializer(data = request.data )
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         else:
#             return Response(serializer.errors)

# class MovieDetailAV(APIView) :
#     def get(self, request, pk) :
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data)
    
#     def put(self, request, pk):
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data = request.data)
#         if serializer.is_valid() :
#             serializer.save()
#             return Response(serializer.data)
#         else :
#             return Response(serializer.errors)

#     def delete(self, request,pk):
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response({'message':"item DELETED"})

# Function based views
# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method == 'GET' :
#         movies = Movie.objects.all()
#         serializer = MovieSerializer(movies, many=True)
#         return Response(serializer.data)

#     if request.method == 'POST' :
#         serializer = MovieSerializer(data= request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data )
#         else :
#             return Response(serializer.errors)

# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request,pk) :
#     if request.method == 'GET' :
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie)
#         return Response(serializer.data )
    
#     if request.method == 'PUT' :
#         movie = Movie.objects.get(pk=pk)
#         serializer = MovieSerializer(movie, data=request.data)
#         if serializer.is_valid() :
#             serializer.save()
#             return Response(serializer.data)
#         else :
#             return Response(serializer.errors)

#     if request.method == 'DELETE' :
#         movie = Movie.objects.get(pk=pk)
#         movie.delete()
#         return Response({'message':"item DELETED"})

