# myapp/views.py

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContentSerializer
# from .phoBERT.detect_content import DetectContent as PhoBERTDetectContent


# detector = PhoBERTDetectContent()

# class ContentDetection(APIView):
#     def post(self, request):
#         serializer = ContentSerializer(data=request.data)
#         if serializer.is_valid():
#             input_text = serializer.validated_data['content']
#             text, predictions = detector.predict_from_input(input_text)
#             return Response({"text": text,'predictions': predictions}, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class ContentDetection(APIView):
    def post(self, request):
        serializer = ContentSerializer(data=request.data)
        if serializer.is_valid():
            input_text = serializer.validated_data['content']
            # text, predictions = detector.predict_from_input(input_text)
            return Response({"text": input_text}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
