from django.contrib.auth.decorators import login_required,permission_required,user_passes_test
from django.utils.decorators import method_decorator

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import get_object_or_404, render, HttpResponseRedirect,redirect

from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate,logout
from .models import Blog
from .forms import BlogForm,NewUserForm

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.") 
	return redirect("blog-list")

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("blog-list")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="login.html", context={"login_form":form})

def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("blog-list")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request, "register.html",context={"register_form":form})

def About(request):
    context = {}
    context["blog"] = Blog.objects.all()
    return render(request, "about.html", context)


@user_passes_test(lambda u: u.is_staff, login_url='blog-login')
def Delete(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}
    # fetch the object related to passed id
    obj = get_object_or_404(Blog, id=pk)
    if request.method == "POST":
        # delete object
        obj.delete()
        # after deleting redirect to
        # home page
        messages.success(request, "Delete successful." )
        return HttpResponseRedirect("/")

    return render(request, "delete.html", context)


@user_passes_test(lambda u: u.is_staff, login_url='blog-login')
def Update(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # fetch the object related to passed id
    obj = get_object_or_404(Blog, id=pk)

    # pass the object as instance in form
    form = BlogForm(request.POST or None, instance=obj)

    # save the data from the form and
    # redirect to detail_view
    if form.is_valid():
        form.save()
        #return HttpResponseRedirect("/"+id)
        messages.success(request, "Update successful." )
        return redirect("blog-list")

    # add form dictionary to context
    context["form"] = form
    context["blog"] = Blog.objects.get(id=pk)

    return render(request, "update.html", context)


@user_passes_test(lambda u: u.is_active,
                     login_url='blog-login',
                     )
def Detail(request, pk):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    context["blog"] = Blog.objects.get(id=pk)

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

    return render(request, 'list.html', {'blogs': blogs})


@user_passes_test(lambda u: u.is_staff, login_url='blog-login')
def Create(request):
    # dictionary for initial data with
    # field names as keys
    context = {}

    # add the dictionary during initialization
    form = BlogForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("blog-list")

    context['form'] = form

    return render(request, "create.html", context)
