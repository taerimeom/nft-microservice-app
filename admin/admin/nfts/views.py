from rest_framework import viewsets, status
from rest_framework.response import Response

from .models import NFT
from .serializers import NFTSerializer

# Create your views here.
class NFTViewSet(viewsets.ViewSet):
    def list(self, request):
        nfts = NFT.objects.all()
        serializer = NFTSerializer(nfts, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = NFTSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        pass

    def update(self, request, pk=None):
        pass

    def destroy(self, request, pk=None):
        pass
