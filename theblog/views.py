from django.shortcuts import get_object_or_404, render
from django.views.generic import ListView,DeleteView,CreateView,UpdateView,DeleteView
from .models import post,category,Comment
from .form import PostForm,EditForm,CommentForm
from django.urls import reverse_lazy,reverse
from django.http import HttpResponseRedirect


# Create your views here.
# def home(request):
    # return render(request,'home.html',{})

def likeview(request, pk):
    # Retrieve the post instance
    post_instance = get_object_or_404(post, id=request.POST.get('post_id'))
    
    # Check if the user has already liked the post
    liked = False
    if post_instance.likes.filter(id=request.user.id).exists():
        # If yes, remove the user's like
        post_instance.likes.remove(request.user)
        liked = False
    else:
        # If no, add the user's like
        post_instance.likes.add(request.user)
        liked = True
    
    # Redirect to the article details page
    return HttpResponseRedirect(reverse('article_details', args=[str(pk)]))


class HomeView(ListView):
    model = post
    template_name = 'homedemo.html'
    ordering = ['-id']
    # ordering = ['-post_date']
    def get_context_data(self, *arg, **kwargs):
        cat_menu=category.objects.all()
        context= super(HomeView, self).get_context_data(*arg, **kwargs)
        context['cat_menu']= cat_menu
        return context

def categoryView(request,cats):
    category_posts=post.objects.filter(category=cats)
    return render(request,'categories.html',{'cats':cats,'category_posts':category_posts})


class ArticleDetailView(DeleteView):
    model=post
    template_name= 'article_details.html'
    def get_context_data(self, *arg, **kwargs):
        cat_menu=category.objects.all()       
        context= super(ArticleDetailView, self).get_context_data(*arg, **kwargs)
        stuff = get_object_or_404(post,id=self.kwargs['pk'])
        total_likes=stuff.total_likes()
        liked=False
        if stuff.likes.filter(id=self.request.user.id).exists():
            liked=True
        context['cat_menu']= cat_menu
        context['total_likes']= total_likes
        context['liked']= liked
        return context


    

class AddPostView(CreateView):
    model=post
    form_class= PostForm
    template_name= 'add_post.html'

class AddCommentView(CreateView):
    model=Comment
    form_class= CommentForm
    template_name= 'add_comments.html'
    # fields='__all__'
    def form_valid(self,form):
        form.instance.Post_id =self.kwargs['pk']
        return super().form_valid(form)
    success_url=reverse_lazy('home')
    
    

class AddcategoryView(CreateView):
    model= category
    # form_class= PostForm
    template_name= 'add_category.html'
    fields='__all__'
    



class UpdatePostView(UpdateView):
    model=post
    form_class=EditForm
    template_name ='update_post.html'
    # fields=['title','body']
class DeletePostView(DeleteView):
    model = post
    template_name = 'delete_post.html'
    success_url=reverse_lazy('home')


