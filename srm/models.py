from django.db import models


class Lead(models.Model):
    full_name = models.CharField(max_length=123)
    email = models.EmailField()
    subject_line = models.CharField(blank=True, null=True, max_length=123)
    message = models.TextField()
    status = models.PositiveSmallIntegerField(
        choices=(
            (1, 'Теплый'),
            (2, 'Горячий'),
            (3, 'Мертвый'),
            (4, 'Другое')
        ),
        default=1
    )
    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name