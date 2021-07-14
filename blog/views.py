from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect
# relative import of forms
from .models import Blog
from .forms import BlogForm

def TentangKami(request):
    context={}
    context["blog"] = Blog.objects.all()
    return render(request, "tentangkami.html", context)

def Delete(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(Blog, id=id)
    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        return HttpResponseRedirect("/")

    return render(request, "delete.html", context)

def Update(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Blog, id=id)

    # pass the object as instance in form
    form = BlogForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        return HttpResponseRedirect("/"+id)

    # add form dictionary to context
    context["form"] = form

    return render(request, "update.html", context)

def Detail(request, id):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["blog"] = Blog.objects.get(id=id)

    return render(request, "detail.html", context)

def List(request):
    blog_list = Blog.objects.all()
    page = request.GET.get('page', 1)
    paginator = Paginator(blog_list, 3)
    try:
        blogs = paginator.page(page)
    except PageNotAnInteger:
        blogs = paginator.page(1)
    except EmptyPage:
        blogs = paginator.page(paginator.num_pages)

    return render(request, 'list.html', { 'blogs': blogs })

def Create(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()

    context['form'] = form
    return render(request, "create.html", context)
