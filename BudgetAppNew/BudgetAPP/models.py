from django.db import models

# Create your models here.

class AccountInfo(models.Model):
    name = models.CharField(max_length=120)
    address = models.CharField(max_length=300)
    mobilenum = models.IntegerField()
    emailid = models.CharField(unique=True,max_length=150)
    username = models.CharField(max_length=20)
    password = models.CharField(max_length=20)
    isActive = models.BooleanField(default=True)
    def __str__(self):
        return self.username


class Category(models.Model):
    category_name = models.CharField(max_length=200)

    def __str__(self):
        return self.category_name

class ExpenseInfo(models.Model):
        user = models.CharField(max_length=120)
        category = models.ForeignKey(Category, on_delete=models.CASCADE)
        expense_name = models.CharField(max_length=200)
        amount = models.IntegerField()
        date = models.DateField()

        def __str__(self):
            return self.expense_name

