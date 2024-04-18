from datetime import datetime, timedelta

from django.db import models
from django.db.models import Q, Sum

from main.models.business_group_models import BusinessGroup
from main.models.industry_models import Industry


class Company(models.Model):
    name = models.CharField(max_length=75)
    code = models.DecimalField(max_digits=12, decimal_places=2, unique=True, db_index=True)
    short_name = models.CharField(max_length=20)
    business_group = models.ForeignKey(BusinessGroup, on_delete=models.CASCADE, related_name="companies", db_index=True, null=False)
    industry = models.ForeignKey(Industry, on_delete=models.CASCADE, related_name="companies", db_index=True, null=False)
    incorporation_date = models.DateField(null=True)
    first_public_issue_date = models.DateField(null=True)
    cin_no = models.CharField(max_length=30)
    remarks = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Company"
        verbose_name_plural = "Companies"
