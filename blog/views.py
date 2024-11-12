from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.http import HttpResponse
from .models import Post


def renderPosts(request):
    total_posts = Post.objects.count()
    posts = Post.objects.order_by("-date")
    return render(request, "blog.html", {"posts": posts, "total_posts": total_posts})


def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, "post_detail.html", {"post": post})

def form_view(request):
    return render(request, 'form.html')

def enviar_mensaje(request):
    if request.method == 'POST':
        mensaje = request.POST.get('mensaje')
        
        # Procesa el mensaje o envíalo a algún lugar
        print("Mensaje recibido:", mensaje)  # Esto se verá en la consola
        
        # Redirige a la página de éxito o al formulario
        return redirect(reverse('form'))
    else:
        return HttpResponse("Método no permitido", status=405)