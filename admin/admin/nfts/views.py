from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import NFT, User
from .serializers import NFTSerializer
import random

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
        nft = NFT.objects.get(id=pk)
        serializer = NFTSerializer(nft)
        return Response(serializer.data)

    def update(self, request, pk=None):
        nft = NFT.objects.get(id=pk)
        serializer = NFTSerializer(instance=nft, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_202_ACCEPTED)


    def destroy(self, request, pk=None):
        nft = NFT.objects.get(id=pk)
        nft.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class UserAPIView(APIView):
  def get(self, _):
    users = User.objects.all()
    user = random.choice(users)
    return Response({
      'id': user.id
    })