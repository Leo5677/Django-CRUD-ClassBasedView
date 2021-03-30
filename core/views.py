from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Produto
from django.urls import reverse_lazy
from .forms import ProdutoModelForm

# Create your views here.


class ListarProdutoView(ListView):
    """LISTAR PRODUTOS LISTVIEW"""
    models = Produto
    template_name = 'listar.html'
    queryset = Produto.objects.all()
    context_object_name = 'produtos'


class CreateProdutoView(CreateView):
    """CADASTRA PRODUTOS"""
    model = Produto
    template_name = 'cadastrar_produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('listar')


class UpdateProdutoView(UpdateView):
    """ATUALIZA PRODUTOS"""
    model = Produto
    template_name = 'cadastrar_produto_form.html'
    fields = ['nome', 'preco']
    success_url = reverse_lazy('listar')


class DeleteProdutoView(DeleteView):
    """DELETAR PRODUTOS"""
    model = Produto
    template_name = 'deletar_produto.html'
    success_url = reverse_lazy('listar')
