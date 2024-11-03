from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import KeyValueSerializer

# Внутреннее хранилище данных в памяти
store_data = {}

class StoreDataView(APIView):
    def post(self, request):
        serializer = KeyValueSerializer(data=request.data)
        if serializer.is_valid():
            key = serializer.validated_data['key']
            value = serializer.validated_data['value']
            store_data[key] = value
            return Response({'message': 'Data stored successfully'}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RetrieveDataView(APIView):
    def get(self, request, key):
        value = store_data.get(key)
        if value:
            return Response({'key': key, 'value': value}, status=status.HTTP_200_OK)
        return Response({'error': 'Key not found'}, status=status.HTTP_404_NOT_FOUND)
