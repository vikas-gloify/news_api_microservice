from django.db import models

class BusinessGroup(models.Model):
    name = models.CharField(max_length=50)
    code = models.SmallIntegerField(unique=True, db_index=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Business Group"
        verbose_name_plural = "Business Groups"
