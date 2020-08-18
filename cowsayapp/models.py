from django.db import models


class InputHistory(models.Model):
    capture_text = models.CharField(max_length=100)

    def __str__(self):
        return self.capture_text
