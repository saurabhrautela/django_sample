from rest_framework import serializers


class MathOperationSerializer(serializers.Serializer):
    operation = serializers.CharField(required=True, max_length=25)
    data = serializers.JSONField()


class HelloWorldSerializer(serializers.Serializer):
    name = serializers.CharField(required=True, max_length=12)
    age = serializers.IntegerField(required=False, min_value=0, max_value=300)


"""
Create according to the Person Model in models.py
"""


class PersonSerializer(serializers.Serializer):
    name = serializers.CharField(max_length=50)
    age = serializers.IntegerField()
    email = serializers.EmailField()
