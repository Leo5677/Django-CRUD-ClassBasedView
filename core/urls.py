from django.urls import path
from .views import ListarProdutoView, CreateProdutoView, UpdateProdutoView, DeleteProdutoView

urlpatterns = [
    path('', ListarProdutoView.as_view(), name='listar'),
    path('cadastrar/', CreateProdutoView.as_view(), name='cadastrar_produto'),
    path('<int:pk>/atualizar/', UpdateProdutoView.as_view(), name='atualizar_produto'),
    path('<int:pk>/deletar/', DeleteProdutoView.as_view(), name='deletar_produto'),
]
