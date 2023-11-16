from django.db import models
from django.contrib.auth.models import User


class Schedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='schedules')
    day = models.CharField(max_length=10)
    open_time = models.TimeField()
    middle_time = models.TimeField()
    close_time = models.TimeField()

    def __str__(self):
        return f'{self.user}: {self.day}: {self.open_time} ~ {self.close_time}'

    class Meta:
        db_table = 'user_schedule'
        verbose_name = '유저 시간표'
        verbose_name_plural = '유저 시간표'