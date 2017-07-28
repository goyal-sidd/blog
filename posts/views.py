from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect, Http404
# Create your views here.
from .forms import PostForm
from .models import Post
from django.contrib import messages
from django.utils import timezone
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render

def post_create(request):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404

	if not request.user.is_authenticated():
		raise Http404
		
	form = PostForm(request.POST or None, request.FILES or None)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.user = request.user
		instance.save()	
		messages.success(request, "Successfully created")
		return HttpResponseRedirect(instance.get_absolute_url())

	context = {
		"form": form,
	}
	return render(request, "post_form.html", context)

#def post_create(request):
#	return HttpResponse("<h1>Create</h1>")

def post_detail(request, slug=None):
	instance = get_object_or_404(Post, slug=slug)
	context = {
		#"object_list": queryset,
		"title": instance.title,
		"instance": instance,
	}
	return render(request, "post_detail.html", context)

def post_list(request):
	queryset_list = Post.objects.all().filter(draft=False).filter(publish__lte=timezone.now()).order_by("-timestamp")
	 
	paginator = Paginator(queryset_list, 5) # Show 25 contacts per page

	page = request.GET.get("page")
	try:
	    queryset = paginator.page(page)
	except PageNotAnInteger:
	    # If page is not an integer, deliver first page.
	    queryset = paginator.page(1)
	except EmptyPage:
	    # If page is out of range (e.g. 9999), deliver last page of results.
	    queryset = paginator.page(paginator.num_pages)

	context = {
		"object_list": queryset,
		"title": "List"
	}

	return render(request, "post_list.html", context)


def post_update(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	form = PostForm(request.POST or None, request.FILES or None, instance=instance)
	if form.is_valid():
		instance = form.save(commit=False)
		instance.save()	
		messages.success(request, "Successfully saved")
		return HttpResponseRedirect(instance.get_absolute_url())
	else:
		messages.error(request, "Not successfully saved")

	context = {
		"title": instance.title,
		"instance": instance,
		"form":form,
	}
	return render(request, "post_form.html", context)

def post_delete(request, slug=None):
	if not request.user.is_staff or not request.user.is_superuser:
		raise Http404
	instance = get_object_or_404(Post, slug=slug)
	instance.delete()
	messages.success(request, "Successfully deleted")
	#return HttpResponseRedirect(instance.get_absolute_url())
	return redirect("posts:list")