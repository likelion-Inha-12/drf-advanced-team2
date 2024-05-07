from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import View, APIView

from .serializers import AssignmentSerializer, PartAssignmentSerializer
from .models import *
#api 1
@api_view(['POST'])
def create_post_v2(request):
    assignment = Assignment(
        title = request.data.get('title'),
        deadline = request.data.get('deadline'),
        part = request.data.get('part'),
        created_at = request.data.get('created_at'),
        github_link = request.data.get('github_link'),
        content = request.data.get('content')
    )
    assignment.save()

    message = f"id: {assignment.pk}번 포스트생성 성공"
    return JsonResponse({'message': 'success'})

#api 1
def create_assignment(request):
    if request.method == "POST":
        data = json.loads(request.body)
        title =data.get('title')
        deadline =data.get('deadline')
        part =data.get('part')
        category = data.get('category')
        created_at = data.get('created_at')
        github_link = data.get('github_link')
        content =data.get('content')
        

        assignment =Assignment(
            title = title,
            deadline =deadline,
            part = part,
            created_at = created_at,
            category = category,
            github_link = github_link,
            content = content
            
            
        )
        assignment.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다'})

#api 2
def create_submission(request):
    if request.method == "POST":
        data =json.loads(request.body)

        description=data.get('description')
        github_link=data.get('github_link')
        created_at=data.get('created_at')

        submission = Submission(
            description=description,
            github_link=github_link,
            created_at=created_at

        )
        submission.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다'})

#api 3




#api 4
class AssignmentApiView(APIView):

    def get_object(self, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        return assignment

    def get(self, request, pk = None):

        if pk is not None: # id로 특정 과제를 조회
            assignment = self.get_object(pk)
            assignmentSerializer = AssignmentSerializer(assignment)
            return JsonResponse(assignmentSerializer.data, status=status.HTTP_200_OK)
        
        # 파트별 과제 조회
        part = request.GET.get('part')
        assignments = Assignment.objects.filter(part = part)
        assignmentSerializer = PartAssignmentSerializer(assignments, many=True)
        return JsonResponse(assignmentSerializer.data, safe=False, status=status.HTTP_200_OK)
    