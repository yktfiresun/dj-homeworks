from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import TokenAuthentication
from rest_framework.viewsets import ModelViewSet
from .serializers import AdvertisementSerializer
from .models import Advertisement
from .filters import AdvertisementFilter
from .permissions import IsOwnerOrReadOnly
from django_filters import rest_framework as filters

class AdvertisementViewSet(ModelViewSet):
    """ViewSet для объявлений."""

    queryset = Advertisement.objects.all()
    serializer_class = AdvertisementSerializer
    filter_backends = (filters.DjangoFilterBackend,)
    filterset_class = AdvertisementFilter

    def get_permissions(self):
        """Получение прав для действий."""
        if self.action in ["create"]:
            return [IsAuthenticated()]
        if self.action in ["update", "partial_update","delete"]:
            return [IsAuthenticated(),IsOwnerOrReadOnly()]
        return []

