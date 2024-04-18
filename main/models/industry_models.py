from django.db import models
from main.models.major_sector_models import MajorSector
from main.models.broad_industry_models import BroadIndustry

class Industry(models.Model):
    name = models.CharField(max_length=50)
    code = models.SmallIntegerField(unique=True, db_index=True)
    broad_industry = models.ForeignKey(BroadIndustry, on_delete=models.CASCADE, related_name="industries", db_index=True, null=False)
    major_sector = models.ForeignKey(MajorSector, on_delete=models.CASCADE, related_name="industries", db_index=True, null=False)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Industry"
        verbose_name_plural = "Industries"
    