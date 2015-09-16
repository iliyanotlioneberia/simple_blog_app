from django.shortcuts import render, redirect
from com.models import BlogEntry
from com.forms import blog_posts
from datetime import datetime
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def landing_page(request):
    if request.method == "POST":
        data = blog_posts(request.POST)
        if data.is_valid():
            print data.cleaned_data['title']
            print data.cleaned_data['body']
            mod = BlogEntry()
            mod.title = data.cleaned_data['title']
            mod.body = data.cleaned_data['body']
            mod.date = datetime.today().replace(microsecond=0)
            mod.save()

            return redirect('home')
    else:

        data = BlogEntry.objects.all()
        if data:
            paginator = Paginator(data, 10)
            page = request.GET.get('page')

            try:
                records = paginator.page(page)
            except PageNotAnInteger:
                records = paginator.page(1)
            except EmptyPage:
                records = paginator.page(paginator.num_pages)

            return render(request, 'index.html', {'data': records})
        else:

            return render(request, 'index.html')


def edit(request, num):
    if request.method == "POST":
        data = blog_posts(request.POST)
        if data.is_valid():
            num = int(request.POST['id'])
            print data.cleaned_data['title']
            print data.cleaned_data['body']
            print datetime.today().replace(microsecond=0)

            BlogEntry.objects.filter(id=num).update(title=data.cleaned_data['title'], body=data.cleaned_data['body'], date=datetime.today().replace(microsecond=0))

            return redirect('home')
    else:
        print num
        data = BlogEntry.objects.filter(id=num)
        return render(request, 'edit.html', {'data': data})


def delete(request, num):
    BlogEntry.objects.filter(id=num).delete()
    return redirect('home')

