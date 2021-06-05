from django.shortcuts import get_object_or_404, render
from .models import  Post, Category
from .serializers import PostSerializer ,DatasetSerializer
from profiles.serializer import ProfileSerializer
from rest_framework import generics
from rest_framework import filters
from rest_framework.permissions import AllowAny
from rest_framework.authtoken.views import APIView
from rest_framework.response import Response
from rest_framework import permissions,status as  statu
import json
import pandas as pd
import joblib
model=joblib.load('modelPipeline5.pkl')
dataset=pd.read_csv('https://raw.githubusercontent.com/AhmadAmr/start-up-prediction-system/main/companiesfinal.csv')

#from django_filters.rest_framework import DjangoFilterBackend
#next update >> APIVIEW instead of generics
#dont forget to remove allowany permission
# class CategoryCreateView(generics.ListCreateAPIView):
#     queryset  = Category.objects.all()
#     serializer_class = CategorySerializer
#     permission_classes = [AllowAny]


#after applying machine learning it would be only list View, 
#dont forget to remove allowany permission
#DONE
class PostListView(generics.ListAPIView):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    filter_backends = [filters.OrderingFilter]
    ordering_fields = ['created_at']
    #permission_classes = [AllowAny]

    
#dont forget to remove allowany permission
class PostDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.order_by('-created_at')
    serializer_class = PostSerializer
    lookup_field = 'id'
    #permission_classes = [AllowAny]


class PostLike(APIView):

    def get(self, request, slug = None, format=None):
        obj = get_object_or_404(Post, slug=slug)
        url_ = obj.get_abslute_url()
        user = self.request.user
        updated = False
        liked = False
        if user.is_authnticated():
            if user in obj.likes.all():
                liked = False
                obj.likes.remove(user)
            else :
                liked= True
                obj.likes.add(user)
            updated= True
            data ={
                "updated": updated,
                "liked": liked
            }

        return Response(data)

class AddPost(APIView):
    #permission_classes = [AllowAny]

    def post(self, request, slug = None, format='json'):
        # User data
        data  = json.loads(request.body)
        dataF = pd.DataFrame({'x':data}).transpose()
        filt1 = (dataset['country_code'] == data['country_code'])
        filt2 = (dataset['category_list'] == data['category_list'])
        country = dataset.loc[filt1]
        final   = country.loc[filt2]
        fail    = dataset.loc[filt2]
        status  = True
        #compute score
        if final.empty :
            score  = model.predict_proba(fail)[:,-1][0]
            status = False
        else :
            score = model.predict_proba(dataF)[:,-1][0]
        
        # save to Models 
        data['user']    = request.user.id
        data['score']   = score
        data['maxfund'] = final['funding_total_usd'].max()
        data['minfund'] = final['funding_total_usd'].median()
        data['status']  = status
        
        serializer = DatasetSerializer(data=data)
        if serializer.is_valid():
           serializer.save()
           json_obj = serializer.data
           return Response(json_obj, status=statu.HTTP_201_CREATED)
        return Response(serializer.errors, status=statu.HTTP_400_BAD_REQUEST)

        