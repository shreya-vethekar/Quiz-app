from django.db import models

# Create your models here.

#different choices for difficulty level
DIFF_CHOCIES=(
    ('easy','easy'),
    ('medium','medium'),
    ('hard','hard'),
)
class Quiz(models.Model):
    name=models.CharField(max_length=120)
    topic=models.CharField(max_length=120)
    number_of_question=models.IntegerField()
    time=models.IntegerField(help_text="Duration of the quiz in minutes")
    required_score_to_pass=models.IntegerField(help_text="Required score in %")
    difficulty=models.CharField(max_length=6,choices=DIFF_CHOCIES)

    def __str__(self):
        return f"{self.name} - {self.topic}"

    def get_questions(self):
        # here we have all the questions for the quiz
        return self.question_set.all()

    class Meta:
        verbose_name_plural = 'Quizes'