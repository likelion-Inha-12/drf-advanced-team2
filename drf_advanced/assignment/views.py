from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse
import json
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import View, APIView

from django.core.serializers import serialize
from .serializers import *
from .models import *

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

        if category:
                category, created = Category.objects.get_or_create(name=category)
        else:
                category = None
        

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
        assignment_id = data.get('assignment_id')
        description=data.get('description')
        github_link=data.get('github_link')
        created_at=data.get('created_at')

        submission = Submission(
            assignment_id = get_object_or_404(Assignment, pk=assignment_id),
            description=description,
            github_link=github_link,
            created_at=created_at

        )
        submission.save()
        return JsonResponse({'message': 'success'})
    return JsonResponse({'message':'POST 요청만 허용됩니다'})

#api 3
from django.http import JsonResponse
from .models import Assignment, Category

def get_assignment(request):
    
    categories = Category.objects.values_list('name', flat=True)

 
    assignments = Assignment.objects.all()
    assignments_data = []
    for assignment in assignments:
        assignment_info = {
            'title': assignment.title,
            'created_at': assignment.created_at,
            'part': assignment.part,
            'category': assignment.category.name if assignment.category else None
        }
        assignments_data.append(assignment_info)

    response_data = {
        'categories': list(categories),
        'assignments': assignments_data
    }
    return JsonResponse(response_data, status=200)
    
#api 5 - 특정 과제 수정
@api_view(['PATCH'])
def update_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)

    if request.method == 'PATCH':
        data = request.data
        serializer = AssignmentSerializer(assignment, data=data, partial=True)
       
    if serializer.is_valid():
        serializer.save()
        return JsonResponse(serializer.data, status=status.HTTP_200_OK)
    return JsonResponse(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#api6 - 특정 과제 삭제
@api_view(['DELETE'])
def delete_assignment(request, pk):
    assignment = get_object_or_404(Assignment, pk=pk)

    if request.method == 'DELETE':
        assignment.delete()
        return JsonResponse({'message': '과제 및 연관된 제출물들이 삭제되었습니다.'}, status=status.HTTP_204_NO_CONTENT)


#api 4, 7, 8
class AssignmentApiView(APIView):

    def get_object(self, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        return assignment

    def get(self, request, pk = None):

        if pk is not None: # api 4 - 특정 과제 조회
            assignment = self.get_object(pk)
            assignmentSerializer = AssignmentSerializer(assignment)
            return JsonResponse(assignmentSerializer.data, status=status.HTTP_200_OK)
        
        part = request.GET.get('part') 
        category = request.GET.get('category')

        if part: # api 7 - 파트별 과제 조회
            assignments = Assignment.objects.filter(part = part)
            assignmentSerializer = PartAssignmentSerializer(assignments, many=True)
            return JsonResponse(assignmentSerializer.data, safe=False, status=status.HTTP_200_OK)
        
        if category: # api 8 - 카테고리별 과제 조회
            assignments = Assignment.objects.filter(category__name = category)
            assignmentSerializer = SimpleAssignmentSerializer(assignments, many=True)
            return JsonResponse(assignmentSerializer.data, safe=False, status=status.HTTP_200_OK)
        
    