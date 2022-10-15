from django.http import HttpResponse
from django.shortcuts import render
import cv2
import base64

from django.http import JsonResponse

from backend.Classes.Controller import ServerController
from backend.Classes.ObjectRecognizer import ObjectRecognizer
from backend.Classes.FaceDetection import FaceDetection
from backend.Classes.SceneElaborator import SceneElaborator
from backend.serializers import ImageSerializer, ImageFile
from rest_framework.views import APIView
from rest_framework.response import Response

class RecognitionAPIView(APIView):
    def post(self, request, format=None):

        image_data = request.data['img']
        env = request.data['env']
        image = base64.b64decode(image_data)
        filename = 'some_image.jpg'
        with open(filename, 'wb') as f:
            f.write(image)
        image = cv2.imread('some_image.jpg')
        controller = ServerController()
        image_result = controller.getEnvironmentUnderstanding(image, env)
        print(image_result)
        if (env == "1"):
            data = {
                'environment': image_result
            }
            return JsonResponse(data, safe=False)

        classes = []
        for obj in image_result['objects']:
            classes.append(obj.name)
        cv2.imwrite("image1.jpg", image_result['final_image'])
        result = ''
        with open("image1.jpg", "rb") as imageFile:
            result = base64.b64encode(imageFile.read()).decode()
        resultant_image = ImageFile(result, classes, image_result['distances'])
        serialized_obj = ImageSerializer(resultant_image)
        print(classes)
        print(image_result['distances'])
        return Response(serialized_obj.data)


    def home(request):
        recognizer = ObjectRecognizer()
        face_detector = FaceDetection()
        scene_elaborator = SceneElaborator()

        return HttpResponse('Setting up model...')