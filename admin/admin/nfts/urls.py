from django.urls import path
from .views import NFTViewSet, UserAPIView

urlpatterns = [
    path("nfts", NFTViewSet.as_view({"get": "list", "post": "create"})),
    path(
        "nfts/<str:pk>",
        NFTViewSet.as_view(
            {
                "get": "retrieve",
                "put": "update",
                "delete": "destroy",
            }
        ),
    ),
    path('user', UserAPIView.as_view())
]
