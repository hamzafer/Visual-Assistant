from rest_framework import serializers

class ImageSerializer(serializers.Serializer):
    image = serializers.CharField(max_length=9999999999999)
    classes = serializers.ListField()
    distances = serializers.ListField()

class ImageFile:
    def __init__(self, image, classes, distances):
        self.image = image
        self.classes = classes
        self.distances = distances
