from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import date, timedelta
from drf_yasg.utils import swagger_auto_schema
from drf_yasg import openapi
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
    @swagger_auto_schema(
        method='post',
        responses={
            200: openapi.Response('Tasks moved successfully', openapi.Schema(
                type=openapi.TYPE_OBJECT,
                properties={
                    'moved': openapi.Schema(type=openapi.TYPE_INTEGER, description='Number of tasks moved'),
                    'message': openapi.Schema(type=openapi.TYPE_STRING, description='Success message'),
                }
            ))
        },
        operation_description="Move all incomplete tasks to the next day"
    )
    @action(detail=False, methods=['post'])
    def carry_forward(self, request):
        """
        Move incomplete tasks to the next day
        """
        user_tasks = Task.objects.filter(user=request.user, completed=False)
        moved_count = 0
        
        for task in user_tasks:
            task.date = task.date + timedelta(days=1)
            task.save()
            moved_count += 1
        
        return Response({
            'moved': moved_count,
            'message': 'Incomplete tasks moved to next day.'
        })
