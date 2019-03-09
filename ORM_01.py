import os
import sys

if __name__ == '__main__':
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysiteday71.settings')
    import django

    django.setup()

    from app01 import models

    # ret = models.Employee.objects.all().values('name', 'department')
        # print(ret)
        # from django.db.models import Avg
        # ret = models.Employee.objects.values('department').annotate(avg=Avg('salary')).values('department', 'avg')
        # print(ret)
        # ret = models.Employee.objects.values('department_id').annotate(avg=Avg('salary')).values('department__name', 'avg')
        # print(ret)
    # ret = models.Author.objects.select_related().values('name', 'book__title')
    # print(ret)
    # print('='*120)
    # ret = models.Author.objects.prefetch_related().values('name', 'book__title')
    # print(ret)


    # 批量创建
    # 有100个书籍对象
    obj = [models.Book(title='沙河{}'.format(i)) for i in range (100)]
    models.Book.objects.bulk_create(obj, 10)