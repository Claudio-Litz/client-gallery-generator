from django.shortcuts import render, get_object_or_404
from django.http import HttpResponseForbidden # Importação não usada, mas ok
from .models import Gallery, Photo
from django.db.models import Q 

def gallery_list(request):
    """
    View da lista de galerias, com a busca que implementamos.
    """
    search_query = request.GET.get('q', '') 
    
    if search_query:
        galleries = Gallery.objects.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query)
        ).distinct()
    else:
        galleries = Gallery.objects.all()
        
    context = {
        'galleries': galleries,
        'search_query': search_query 
    }
    return render(request, 'galleries/gallery_list.html', context)


def gallery_detail(request, gallery_id):
    """
    View de detalhe da galeria.
    Esta é a versão CORRIGIDA para bater com seu models.py.
    """
    gallery = get_object_or_404(Gallery, pk=gallery_id)

    # Lógica 1: Se a galeria NÃO for protegida
    # CORREÇÃO: Voltamos a usar 'is_protected' [cite: 78]
    if not gallery.is_protected:
        context = {'gallery': gallery}
        return render(request, 'galleries/gallery_detail.html', context)

    # Lógica 2: Se for um POST (usuário enviou a senha)
    if request.method == 'POST':
        submitted_password = request.POST.get('password')

        # CORREÇÃO: Voltamos à comparação direta de texto 
        # (Isso é inseguro, mas é o que o seu modelo suporta agora)
        if submitted_password == gallery.password:
            # Senha CORRETA.
            context = {'gallery': gallery}
            return render(request, 'galleries/gallery_detail.html', context)
        else:
            # Senha INCORRETA.
            context = {
                'gallery': gallery,
                'error': 'Senha incorreta. Tente novamente.'
            }
            return render(request, 'galleries/gallery_password_prompt.html', context)

    # Lógica 3: Se for um GET (primeiro acesso)
    context = {'gallery': gallery}
    return render(request, 'galleries/gallery_password_prompt.html', context)