from django.shortcuts import render, redirect, get_object_or_404
from django.views import generic
from .models import Piece, Collection
from .forms import UserForm
from django.contrib.auth import authenticate, login
from django.views.generic import View, ListView
from django.contrib.auth import views as auth_views
from django.db.models import Q

class index(generic.ListView):
    model = Collection
    template_name = 'genre/genretemplate.html'
    context_object_name = 'object_list'

class details(generic.DetailView):
    model = Collection
    template_name = "genre/detailtemplate.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['Pitem'] = Piece.objects.filter(collection=self.object)
        return context

class SearchView(ListView):
    model = Piece
    template_name = 'genre/search.html'
    context_object_name = 'results'

    def get_queryset(self):
        query = self.request.GET.get('q')
        return Piece.objects.filter(
            Q(title__icontains=query) | 
            Q(artist__icontains=query) |
            Q(typ__icontains=query)
        )

class UserFormView(View):
    form_class = UserForm
    template_name = 'genre/formtemplate.html'

    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = self.form_class(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password'])
            user.save()

            newuser = authenticate(username=form.cleaned_data['username'], password=form.cleaned_data['password'])

            if newuser is not None and newuser.is_active:
                login(request, newuser)
                return redirect("/genre")
        
        return render(request, self.template_name, {'form': form})
    
def piece_detail(request, piece_id):
        piece = get_object_or_404(Piece, id=piece_id)
        return render(request, 'genre/piece_detail.html', {'piece': piece})
