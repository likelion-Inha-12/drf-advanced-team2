from rest_framework import serializers
from .models import Assignment, Submission
from django.utils import timezone

# 과제 내용 조회할 때 필요한 제출물 정보
# 1. 제출물의 내용 -> SubmissionSerializer에서 얻어오기
#     - 제출물의 깃허브 링크
#     - 과제 작성 일자
# 2. 지금까지 제출한 과제 수

class SubmissionSerializer(serializers.ModelSerializer):
    github_link = serializers.URLField()
    created_at = serializers.DateTimeField()

    class Meta:
        model = Submission
        fields = ["github_link", "created_at"]

class AssignmentSerializer(serializers.ModelSerializer):
    submissions = SubmissionSerializer(many=True)
    time_left = serializers.SerializerMethodField()
    submissions_count = serializers.SerializerMethodField()

    class Meta:
        model = Assignment
        fields = ["title", "created_at", "part", "category", "time_left", "github_link", "content", "submissions", "submissions_count"]
 
    def get_time_left(self, obj): # Serializer 클래스에서 메서드의 이름은 필드명과 동일하게 설정
        remaining_time = obj.deadline - timezone.now()
        return remaining_time
    
    def get_submissions_count(self, obj):
        return obj.submissions.count()
    
class PartAssignmentSerializer(serializers.ModelSerializer):
    title = serializers.CharField(max_length = 100)
    created_at = serializers.DateTimeField()
    part = serializers.CharField()

    class Meta:
        model = Assignment
        fields = ["title", "created_at", "part"]