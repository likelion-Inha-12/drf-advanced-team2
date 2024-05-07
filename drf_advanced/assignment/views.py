from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import View, APIView

from .serializers import AssignmentSerializer, PartAssignmentSerializer
from .models import *

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
    