from rest_framework import viewsets, status
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from datetime import date, timedelta
from .models import Task
from .serializers import TaskSerializer


class TaskViewSet(viewsets.ModelViewSet):
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_queryset(self):
        return Task.objects.filter(user=self.request.user)
    
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
