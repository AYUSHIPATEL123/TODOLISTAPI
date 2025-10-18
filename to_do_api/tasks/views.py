from django.shortcuts import render
from .serializers import TaskSerializer , RegisterSerializer , LoginSerializer
from rest_framework import viewsets,status
from rest_framework.views import APIView
from rest_framework.permissions import AllowAny,IsAuthenticated
from .models import Task
from rest_framework.response import Response
from django.contrib.auth.models import User 
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken 
from .permissions import IsOwnerOrAdmin
from .tasks import daily_task
from django_celery_beat.models import PeriodicTask, CrontabSchedule
# Create your views here.
def daily_task_view():
    schedule, _= CrontabSchedule.objects.get_or_create(minute='23',hour='56',day_of_week='*',day_of_month='*',month_of_year='*')
    task,created=PeriodicTask.objects.get_or_create(crontab=schedule,name='daily_task',task='tasks.tasks.daily_task')
    task.save()
    return None
    
class RegisterView(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = RegisterSerializer
    permission_classes = [AllowAny]
    # return Response({"message":"successfully created user","status":200},status=status.HTTP_200_OK)

class LoginView(APIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    def post(self, request):        
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            username = serializer.validated_data['username']
            password = serializer.validated_data['password']
            user = authenticate(username=username,password=password)
            token_pair = RefreshToken.for_user(user)
            return Response({"message":"successfully logged in","status":200,"user":user.username,"refresh":str(token_pair),"access token":str(token_pair.access_token)},status=status.HTTP_200_OK)
        else:
            Response({"message":"invalid credentials","status":400},status=status.HTTP_400_BAD_REQUEST)
        
class TaskViewSet(viewsets.ModelViewSet):
    # queryset = Task.objects.all()
    serializer_class = TaskSerializer
    permission_classes = [IsAuthenticated]
    
    def get_permissions(self):
        if self.action == 'create':
            return [IsOwnerOrAdmin()]
        elif self.action in ['update','partial_update','destroy']:
            return [IsOwnerOrAdmin()]
        elif self.action == 'list':
            return [IsOwnerOrAdmin()]
        return [IsOwnerOrAdmin()]
    
    def get_queryset(self):
        if self.request.user.is_staff:
            return Task.objects.all()
        else:
            return Task.objects.filter(user=self.request.user)
            