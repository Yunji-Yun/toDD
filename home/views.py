from django.shortcuts import redirect, render
from django.views.generic import ListView, DetailView, CreateView
from .models import Post, Category
from django.http import JsonResponse


def todo_complete(request, pk):
    try:
        print(f'todo_incomplete called for id: {pk}')
        todo = Post.objects.get(id=pk)
        todo.completed = True
        todo.save()
        return JsonResponse({'status': 'success'})
    except Post.DoesNotExist:
        return JsonResponse({'status': 'error', 'message': 'Post not found'}, status=404)


def todo_incomplete(request, pk):
    todo = get_object_or_404(Post, pk=pk)
    todo.completed = False
    todo.save()
    return JsonResponse({'status': 'success'})

def category_page(request, slug):
    if slug == 'no_category':
        category = '미분류'
        post_list = Post.objects.filter(category=None)
    else:
        category = Category.objects.get(slug=slug)
        post_list = Post.objects.filter(category=category)

    return render (
        request,
        'home/category_list.html',
        {
            'post_list' : post_list,
            'categories' : Category.objects.all(),
            'no_categories_post_count' : Post.objects.filter(category=None).count(),
            'category' : category,
        }
    )

class PostList(ListView):
    model = Post
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_categories_post_count'] = Post.objects.filter(category=None).count()
        return context

    # def todo_com(request, pk):
    #     todo = Post.objects.get(id=pk)
    #     todo.completed = True
    #     todo.save()
    #     return redirect('post_list')
    #
    # def todo_income(request):
    #     todo = Post.objects.get(id=pk)
    #     todo.completed = False
    #     todo.save()
    #     return redirect('post_list')

class CategoryList(ListView):
    def get_context_data(self, **kwargs):
        context = super(PostList, self).get_context_data()
        context['categories'] = Category.objects.all()
        context['no_categories_post_count'] = Post.objects.filter(category=None).count()
        return context

class PostDetail(DetailView):
    model = Post


class PostCreate(CreateView):
    model = Post
    fields = ['title', 'content', 'deadline']