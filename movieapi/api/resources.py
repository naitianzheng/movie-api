from tastypie.resources import ModelResource
from api.models import Movie, Order
from tastypie.authorization import Authorization

class MovieResource(ModelResource):
    class Meta:
        queryset = Movie.objects.all()
        resource_name = 'movie'
        authorization = Authorization()
        fields = ['id','title','director','runningtime','description','quantity']

class OrderResource(ModelResource):
    class Meta:
        queryset = Order.objects.all()
        resource_name = 'order'
        authorization = Authorization()