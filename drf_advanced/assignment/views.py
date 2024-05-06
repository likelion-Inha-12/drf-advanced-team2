from django.shortcuts import get_object_or_404
from django.http import HttpResponse, JsonResponse

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.views import View, APIView

from .serializers import AssignmentSerializer
from .models import *

class AssignmentApiView(APIView):

    def get_object(self, pk):
        assignment = get_object_or_404(Assignment, pk=pk)
        return assignment

    def get(self, request, pk):
        assignment = self.get_object(pk)

        assignmentSerializer = AssignmentSerializer(assignment)
        return JsonResponse(assignmentSerializer.data, status=status.HTTP_200_OK)