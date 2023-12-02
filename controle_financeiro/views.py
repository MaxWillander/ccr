from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, get_object_or_404, redirect
from django.db.models import Sum
from .models import Receita, Despesa, Categoria
from .forms import ReceitaForm, DespesaForm
import datetime

def listar_receitas(request):
    receitas = Receita.objects.all()
    total_receitas = Receita.objects.aggregate(Sum('valor'))['valor__sum'] or 0
    total_despesas = Despesa.objects.aggregate(Sum('valor'))['valor__sum'] or 0
    total_geral = total_receitas - total_despesas  # Corrigir aqui  
   
    return render(request, 'receitas/listar_receitas.html', {'receitas': receitas, 'total_geral': total_geral, 'total_receitas': total_receitas})

def adicionar_receita(request):
    if request.method == 'POST':
        form = ReceitaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_receitas')
    else:
        form = ReceitaForm()
    return render(request, 'receitas/adicionar_receitas.html', {'form': form})

def detalhar_receita(request, receita_id):
    receita = get_object_or_404(Receita, pk=receita_id)
    return render(request, 'receitas/detalhar_receitas.html', {'receita': receita})

def listar_despesa(request):
    despesas = Despesa.objects.all()
    total_despesas = Despesa.objects.aggregate(Sum('valor'))['valor__sum'] or 0
    total_receita = Receita.objects.aggregate(Sum('valor'))['valor__sum'] or 0
    total_geral = total_receita - total_despesas

    return render(request, 'despesas/listar_despesas.html', {'despesas': despesas, 'total_geral': total_geral, 'total_despesas': total_despesas})

def adicionar_despesa(request):
    if request.method == 'POST':
        form = DespesaForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('listar_despesas')
    else:
        form = DespesaForm()
    return render(request, 'despesas/adicionar_despesas.html', {'form': form})

def detalhar_despesa(request, despesa_id):
    despesa = get_object_or_404(Despesa, pk=despesa_id)
    return render(request, 'despesas/detalhar_despesas.html', {'despesa': despesa})
