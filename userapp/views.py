from django.shortcuts import render
from rest_framework.decorators import api_view

from rest_framework.views import APIView
# import seriliazer and models
from .serializers import TaskSerializer
from .models import Task
# Create your views here.
from rest_framework.response import Response

from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser 
from rest_framework import status


# task view
@api_view(['GET', 'POST', 'DELETE'])
def task_list(request):
    if request.method=='GET':
        tasks = Task.objects.all()
        task_serializer = TaskSerializer(tasks, many=True)
        return JsonResponse(task_serializer.data, safe=False)
 
    # post
    elif request.method=='POST':
        task_data=JSONParser().parse(request)
        task_serializer = TaskSerializer(data=task_data)
        if task_serializer.is_valid():
            task_serializer.save()
            # return JsonResponse(task_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse("Added Successfully!!" , safe=False)
        return JsonResponse("Failed to Add.",safe=False)
        # return JsonResponse(task_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'DELETE':
        count = Task.objects.all().delete()
        return JsonResponse({'message': '{} Task were deleted successfully!'.format(count[0])}, status=status.HTTP_204_NO_CONTENT)

    # delete
    # elif request.method=='DELETE':
    #     task=Task.objects.get(TaskId=id)
    #     task.delete()
    #     return JsonResponse("Deleted Succeffully!!", safe=False)
 
 
@api_view(['GET', 'PUT', 'DELETE'])
# get by id
def task_detail(request, pk):
    try: 
        tasks = Task.objects.get(pk=pk) 
    except Task.DoesNotExist: 
        return JsonResponse({'message': 'The id does not exist'}, status=status.HTTP_404_NOT_FOUND) 
 
    if request.method == 'GET': 
        tasks_serializer = TaskSerializer(tasks) 
        return JsonResponse(tasks_serializer.data) 
 
    elif request.method == 'PUT': 
        tasks_data = JSONParser().parse(request) 
        tasks_serializer = TaskSerializer(tasks, data=tasks_data) 
        if tasks_serializer.is_valid(): 
            tasks_serializer.save() 
            return JsonResponse(tasks_serializer.data) 
        return JsonResponse(tasks_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 
 
    elif request.method == 'DELETE': 
        tasks.delete() 
        return JsonResponse({'message': 'Task was deleted successfully!'}, status=status.HTTP_204_NO_CONTENT)
    
        
