from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import View, APIView

from .serializers import AssignmentSerializer
from .models import *


#api 1
def create_assignment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title =data.get('title')
        deadline =data.get('deadline')
        part =data.get('part')
        created_at = data.get('created_at')
        github_link = data.get('github_link')
        content =data.get('content')
        

        post =Assignment(
            title = title,
            deadline =deadline,
            part = part,
            created_at = created_at,
            github_link = github_link,
            content = content
            
            
        )
        post.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다'})

#api 2
def create_submission(request):
    if request.method == "POST":
        data =json.loads(request.body)

        description=data.get('description')
        github_link=data.get('github_link')
        created_at=data.get('created_at')

        post = Submission(
            description=description,
            github_link=github_link,
            created_at=created_at

        )
        post.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다'})

#api 3




#api 4
class AssignmentApiView(APIView):

    def get_object(self, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        return assignment

    def get(self, request, pk):
        assignment = self.get_object(pk)

        assignmentSerializer = AssignmentSerializer(assignment)
        return JsonResponse(assignmentSerializer.data, status=status.HTTP_200_OK)