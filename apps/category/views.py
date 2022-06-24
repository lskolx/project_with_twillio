from rest_framework.viewsets import ModelViewSet
from .models import Category
from .serializers import CategorySerializer
from rest_framework import permissions

class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = None
    """
    action:
    list
    retrieve
    update
    pertial_update
    create
    destroy
    """

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            self.permission_classes = [permissions.AllowAny]
        elif self.action in ['update', 'create', 'destroy', 'pertial_update']:
            self.permission_classes = [permissions.IsAdminUser]
            return [permission() for permission in self.permission_classes]

    