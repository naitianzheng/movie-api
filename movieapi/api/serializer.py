from api.models import Movie, Order
from rest_framework import serializers

class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ['id','title','director','runningtime','description','price','quantity']

class OrderSerializer(serializers.ModelSerializer):
    movies = MovieSerializer(read_only=True, many=True)
    class Meta:
        model = Order
        fields = ['id', 'name', 'email', 'address', 'card', 'movies', 'total_price']

    def validate_name(self, value):
        i = 0;
        while i <= len(value):
            if (not value[i].isalpha()) and value[i] != ' ':
                raise serializers.ValidationError('This field must only contain letters and/or space')
        return value
    
    def validate_address(self, value):
        i = 0;
        while i <= len(value):
            if (not value[i].isalpha()) and (not value[i].isdigit) and value[i] != ' ':
                raise serializers.ValidationError('This field must only contain letters and/or digits')
        return value

    def validate_card(self, value):
        if len(str(value)) != 16:
            raise serializers.ValidationError('The length of this field must be 16')
        return value