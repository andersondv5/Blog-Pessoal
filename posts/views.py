from django.shortcuts import render, get_object_or_404
from .models import Post

def post_list(request):
    posts = Post.objects.all().order_by('-published_at')
    return render(request, 'posts/post_list.html', {'posts': posts})

def post_detail(request, slug):
    post = get_object_or_404(Post, slug=slug)
    
    # Posts em ordem cronológica
    all_posts = Post.objects.all().order_by('published_at')
    post_list = list(all_posts)
    
    # Encontrar índice atual
    current_index = None
    for i, p in enumerate(post_list):
        if p.id == post.id:
            current_index = i
            break
    
    # Posts anterior e próximo (agora corretos)
    previous_post = post_list[current_index - 1] if current_index > 0 else None
    next_post = post_list[current_index + 1] if current_index < len(post_list) - 1 else None
    
    return render(request, 'posts/post_detail.html', {
        'post': post,
        'previous_post': previous_post,
        'next_post': next_post,
        'post_number': current_index + 1 if current_index is not None else 1,
        'total_posts': len(post_list)
    })

def sobre_mim(request):
    return render(request, 'sobre_mim.html')

def buscar(request):
    query = request.GET.get('q', '')  # pega o que o usuário digitou
    resultados = Post.objects.filter(title__icontains=query) if query else []
    
    return render(request, 'buscar.html', {'resultados': resultados, 'query': query})
