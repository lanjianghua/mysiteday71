from django.db import models


# Create your models here.


# class Employee(models.Model):
#     name = models.CharField(max_length=64)
#     age = models.IntegerField()
#     salary = models.IntegerField()
#     province = models.CharField(max_length=64)
#     department = models.CharField(max_length=64)
#
#     def __str__(self):
#         return self.name
#
#     class Meta:
#         db_table = 'employee'


class Employee(models.Model):
    name = models.CharField(max_length=64)
    age = models.IntegerField()
    salary = models.IntegerField()
    province = models.CharField(max_length=64)
    department = models.ForeignKey(to='Department', on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'employee'


class Department(models.Model):
    name = models.CharField(max_length=64)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'department'


class Author(models.Model):
    name = models.CharField(max_length=64)
    book = models.ManyToManyField(to='Book')

    def __self__(self):
        return self.name

    class Meta:
        db_table = 'author'


class Book(models.Model):
    title = models.CharField(max_length=64)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'book'
