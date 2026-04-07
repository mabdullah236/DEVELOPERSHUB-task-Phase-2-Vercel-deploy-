from rest_framework import serializers
from .models import Book

class BookSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    
    def validate_price(self, value):
        if value <= 0:
            raise serializers.ValidationError("Price must be greater than zero.")
        return value
    def validate_isbn(self, value):
        if len(value) == 13 and value.isdigit():
            return value
        else:
            raise serializers.ValidationError("ISBN must be exactly 13 digits long and contain only numbers.")
    class Meta:
        model=Book
        fields = ['id', 'title', 'author', 'price', 'isbn', 'publishedDate', 'owner']