from rest_framework import serializers


class DescribeYourSymptomsSerializer(serializers.Serializer):
    text = serializers.CharField()