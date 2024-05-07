from django.db import models


# 카테고리 table
class Category(models.Model):
    name = models.CharField(max_length = 10, unique=True)

    def __str__(self):
        return self.name

# 과제 table
class Assignment(models.Model):
    PART_CHOICES = (
        ('BE', 'BE'),
        ('FE', 'FE'),
        ('ALL', 'ALL'),
    )
    title = models.CharField(max_length = 100)
    created_at = models.DateTimeField(auto_now_add = True)
    deadline = models.DateTimeField()
    part = models.CharField(max_length = 10,choices=PART_CHOICES)
    #category = models.ForeignKey(Category, on_delete=models.CASCADE)
    #category = models.CharField(max_length = 20)
    category=models.ForeignKey(Category, verbose_name = "subject_category", on_delete=models.CASCADE, related_name="category")
    github_link = models.URLField()
    content = models.TextField()

    def __str__(self):
        return self.title



# 제출 table
class Submission(models.Model):
    assignment_id = models.ForeignKey(Assignment, on_delete=models.CASCADE, related_name="submissions")
    description = models.TextField() # 과제에 대한 설명
    github_link = models.URLField()
    created_at = models.DateTimeField(auto_now_add = True)

    def __str__(self):
        return self.description