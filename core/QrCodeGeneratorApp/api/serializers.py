from rest_framework import serializers


class GeneratorSerializer(serializers.Serializer):
    text = serializers.CharField(max_length=255)
    class Meta:
        # fields = "__all__"
        fields = ['text']
        
