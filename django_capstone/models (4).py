from django.db import models

class Board(models.Model):
    title = models.CharField(max_length=64)
    contents = models.TextField()
    writer = models.ForeignKey('ceoaccounts.User', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title

    class Meta:
        db_table = 'ceoboards'
        verbose_name = '점주 게시판'
        verbose_name_plural = '점주 게시판'