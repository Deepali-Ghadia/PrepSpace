from django.db import models
from syllabus_tracker.models import Topic  # import Topic for foreign key link

class DailyToDo(models.Model):
    date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.date.strftime("%Y-%m-%d")

class Task(models.Model):
    daily_todo = models.ForeignKey(DailyToDo, on_delete=models.CASCADE, related_name='tasks')
    topic = models.ForeignKey(Topic, on_delete=models.SET_NULL, null=True, blank=True)  # nullable for non-syllabus tasks
    custom_label = models.CharField(max_length=255, blank=True, null=True)
    is_done = models.BooleanField(default=False)
    estimated_time = models.DurationField(null=True, blank=True)  # Estimated time to complete task
    time_spent = models.DurationField(default=0)  # Time actually spent on task
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        label = self.custom_label if self.custom_label else (self.topic.topic_name if self.topic else "Untitled Task")
        return label
