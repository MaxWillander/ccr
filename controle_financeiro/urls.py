from django.urls import path
from .views import listar_despesa, listar_receitas, adicionar_receita, detalhar_receita, \
                    listar_despesa, adicionar_despesa, detalhar_despesa

urlpatterns = [
    path('receitas/listar/', listar_receitas, name='listar_receitas'),
    path('receitas/adicionar/', adicionar_receita, name='adicionar_receita'),
    path('receitas/<int:receita_id>/', detalhar_receita, name='detalhar_receita'),
    path('despesas/listar/', listar_despesa, name='listar_despesa'),
    path('despesas/adicionar/', adicionar_despesa, name='adicionar_despesa'),
    path('despesas/<int:despesa_id>/', detalhar_despesa, name='detalhar_despesa'),
]
