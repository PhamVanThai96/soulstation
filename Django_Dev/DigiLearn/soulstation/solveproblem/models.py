from django.db import models

import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname('__file__'), '..')))

class SolveProblem(models.Model):
    problem = models.CharField(max_length=10000, unique=True)

    def __str__(self):
        return self.problem

class Question(models.Model):
    question_id = models.AutoField(primary_key=True)
    original_text = models.TextField()
    translated_text = models.TextField()
    answer_string = models.CharField(max_length=1000)
    category = models.CharField(max_length=255)

    def __str__(self):
        return f"Question {self.question_id} - {self.category}"
