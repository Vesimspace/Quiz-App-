from django.db import models
import random

DIFF_CHOICES = (
    ('easy', 'easy'),
    ('medium', 'medium'),
    ('hard', 'hard'),
)

class Quiz(models.Model):

    name = models.CharField(max_length=200)
    topic = models.CharField(max_length=150)
    question_number = models.IntegerField()
    time = models.IntegerField(help_text="duration of the quiz in minutes")
    required_score = models.IntegerField(help_text="required score in %")
    difficulty = models.CharField(max_length=6, choices=DIFF_CHOICES)

    def __str__(self):
        return f"{self.name}-{self.topic}"
    
    def get_quesitons(self):
        questions = list(self.question_set.all())
        random.shuffle(questions)
        return questions[:self.question_number]



