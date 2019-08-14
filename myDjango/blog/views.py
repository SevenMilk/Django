from django.shortcuts import render
from .models import Post
from .forms import PostForm
from django.shortcuts import redirect
from django.contrib.auth import get_user_model
#from django.views.decorators.csrf import csrf_exempt #CSRF token
me = get_user_model().objects.get(username = 'wei')

# Create your views here.
def post_list(request):
    #return render(request,'blog/post_list.html',{})
    posts = Post.objects.all().order_by('-created_date') # '-' = desc 遞減
    post_form = PostForm()
    return render(request, 'blog/post_list.html', locals())

#@csrf_exempt
def add_record(request):
    if request.POST:
        title = request.POST["title"]
        text = request.POST['text']
        Post.objects.create(author=me, title=title, text=text)
    return redirect('/blog')

def post_record(request,id):
    post = Post.objects.get(id=id)
    return render(request, 'blog/post_record.html',locals())