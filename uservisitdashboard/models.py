from django.db import models

class UserVisit(models.Model):
    customer_name=models.CharField(max_length=50)
    customer_address=models.CharField(max_length=120)
    branch =models.CharField(max_length=20)
    assigned_CSE =models.CharField(max_length=50)
    visit_date=models.DateField(auto_now=False)
    doc_attached=models.BooleanField(default=False)
    visit_completed=models.BooleanField(default=False)