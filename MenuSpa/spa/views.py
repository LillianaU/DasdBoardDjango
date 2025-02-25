from django.shortcuts import render
from django.shortcuts import render

def menu_view(request):
    return render(request, 'spa/base.html')  # Asegúrate de que la plantilla 'menu.html' exista en la carpeta 'templates/spa'



def suma_view(request):
    if request.method == 'POST':
        num1 = int(request.POST.get('num1', 0))
        num2 = int(request.POST.get('num2', 0))
        resultado = num1 + num2
        return render(request, 'suma.html', {'resultado': resultado})
    return render(request, 'spa/suma.html')




def resta_view(request):
    resultado = None
    if request.method == 'POST':
        num1 = request.POST.get('num1')
        num2 = request.POST.get('num2')
        if num1 and num2:
            resultado = float(num1) - float(num2)
    return render(request, 'spa/resta.html', {'resultado': resultado})

    #return render(request, 'spa/resta.html')



def palindromos_view(request):
   # return render(request, 'spa/palindromos.html')

    resultado = None
    if request.method == 'POST':
        texto = request.POST.get('texto', '').replace(" ", "").lower()
        if texto == texto[::-1]:
            resultado = f'"{request.POST.get("texto")}" es un palíndromo.'
        else:
            resultado = f'"{request.POST.get("texto")}" no es un palíndromo.'
    return render(request, 'spa/palindromos.html', {'resultado': resultado})
