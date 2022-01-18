from django.urls import path
from .views import NFTViewSet

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
]
