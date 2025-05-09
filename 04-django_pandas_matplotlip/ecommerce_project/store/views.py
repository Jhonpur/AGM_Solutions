from django.shortcuts import render
from .models import Product
import matplotlib.pyplot as plt
import pandas as pd


# Create your views here.
def product_list(request):
    products = Product.objects.all()
    return render(request, 'store/product_list.html', {'products': products})

def home(request):
    featured_products = Product.objects.all()
    return render(request, 'store/home.html', {'featured_products': featured_products})

def cart(request):
    nel_carello = []
    totale = 0
    return render(request, 'store/cart.html', {'nel_carrello': nel_carello, 'totale': totale})

def grafici(request):
    # Carica i dati
    df = pd.read_csv('prova.csv')
    
    # GRAFICO A TORTA
    # Raggruppa per categoria e somma le vendite
    sales_by_category = df.groupby('categoria')['vendite'].sum()
    
    # Crea il grafico a torta
    plt.figure(figsize=(8, 8))
    plt.pie(sales_by_category, labels=sales_by_category.index, autopct='%1.1f%%')
    plt.title('Distribuzione vendite per categoria')
    plt.savefig('store/static/store/pie_chart.png')
    plt.close()
    
    # GRAFICO A BARRE
    # Raggruppa per data e somma le vendite
    sales_by_date = df.groupby('data')['vendite'].sum().reset_index()
    
    # Crea il grafico a barre
    plt.figure(figsize=(10, 6))
    plt.bar(sales_by_date['data'], sales_by_date['vendite'])
    plt.xlabel('Data')
    plt.ylabel('Vendite')
    plt.title('Vendite per data')
    plt.xticks(rotation=45)
    plt.tight_layout()
    plt.savefig('store/static/store/bar_chart.png')
    plt.close()
    
    return render(request, 'store/grafici.html')