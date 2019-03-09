from django.shortcuts import render

# Create your views here.
from app01 import models


def book(request):
    page_num = request.GET.get('page')
    # page_num = int(page_num)
    # data_start = (page_num - 1) * 10
    # data_end = page_num * 10
    # per_page = 10
    total_count = models.Book.objects.all().count()
    # total_page, m = divmod(total_count, per_page)
    # if m:
    #     total_page += 1
    # try:
    #     page_num = int(page_num)
    # except Exception as e:
    #     page_num = 1
    # all_book = models.Book.objects.all()[data_start:data_end]
    # max_page = 11
    # half_max_page = max_page // 2
    # page_start = page_num - half_max_page
    # page_end = page_num + half_max_page
    # if page_start < 1:
    #     page_start = 1
    #     page_end = max_page
    # if page_end > total_page:
    #     page_start = total_page - max_page + 1
    #     page_end = total_page
    #
    # # 自己拼接分页的HTML代码
    #
    #
    # html_str_list = []
    # html_str_list.append('<li><a href="/book/?page=1">首页</a></li>')
    # if page_num <= 1:
    #     html_str_list.append('<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>')
    # else:
    #     html_str_list.append(
    #         '<li><a href="#" aria-label="Previous"><span aria-hidden="true">&laquo;</span></a></li>')
    #
    # for i in range(page_start, page_end + 1):
    #     tmp = '<li><a href="/book/?page={0}">{0}</a></li>'.format(i)
    #     html_str_list.append(tmp)
    # if page_num >= total_page:
    #     html_str_list.append('<li class="disabled"><a href="#" aria-label="Previous"><span aria-hidden="true">&raquo;</span></a></li>')
    # else:
    #     html_str_list.append('<li><a href="#" aria-label="Previous"><span aria-hidden="true">&raquo;</span></a></li>')
    # html_str_list.append('<li><a href="/book/?page={}">尾页</a></li>'.format(total_page))
    # page_html = "".join(html_str_list)
    #
    # return render(request, 'books.html', {'books': all_book, 'page_html': page_html})

    # 调用一个类
    from mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/books/", max_page=9, )

    ret = models.Book.objects.all()[page_obj.start:page_obj.end]

    page_html = page_obj.page_html()

    return render(request, "books.html", {"books": ret, "page_html": page_html})


def depts(request):
    # 从URL取参数
    page_num = request.GET.get("page")
    print(page_num, type(page_num))
    # 总数据是多少
    total_count = models.Department.objects.all().count()
    from mypage import Page
    page_obj = Page(page_num, total_count, per_page=10, url_prefix="/depts/", max_page=11, )

    ret = models.Department.objects.all()[page_obj.start:page_obj.end]
    print(ret)

    page_html = page_obj.page_html()
    return render(request, "department.html", {"depts": ret, "page_html": page_html})
