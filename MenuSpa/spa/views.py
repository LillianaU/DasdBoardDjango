from django.shortcuts import render
# Importa la función `render` del módulo `django.shortcuts` para renderizar plantillas HTML.

def menu_view(request):
    # Define la vista `menu_view` que maneja las solicitudes a la página del menú.
    return render(request, 'spa/base.html')
    # Renderiza la plantilla 'base.html' ubicada en la carpeta 'templates/spa'.

def suma_view(request):
    # Define la vista `suma_view` que maneja las solicitudes a la página de suma.
    if request.method == 'POST':
        # Verifica si la solicitud es de tipo POST.
        num1 = int(request.POST.get('num1', 0))
        # Obtiene el valor del primer número del formulario y lo convierte a entero.
        num2 = int(request.POST.get('num2', 0))
        # Obtiene el valor del segundo número del formulario y lo convierte a entero.
        resultado = num1 + num2
        # Calcula la suma de los dos números.
        return render(request, 'suma.html', {'resultado': resultado})
        # Renderiza la plantilla 'suma.html' con el resultado de la suma.
    return render(request, 'spa/suma.html')
    # Si la solicitud no es de tipo POST, renderiza la plantilla 'suma.html' sin resultado.

def resta_view(request):
    # Define la vista `resta_view` que maneja las solicitudes a la página de resta.
    resultado = None
    # Inicializa la variable `resultado` como None.
    if request.method == 'POST':
        # Verifica si la solicitud es de tipo POST.
        num1 = request.POST.get('num1')
        # Obtiene el valor del primer número del formulario.
        num2 = request.POST.get('num2')
        # Obtiene el valor del segundo número del formulario.
        if num1 and num2:
            # Verifica si ambos números están presentes.
            resultado = float(num1) - float(num2)
            # Calcula la resta de los dos números.
    return render(request, 'spa/resta.html', {'resultado': resultado})
    # Renderiza la plantilla 'resta.html' con el resultado de la resta.

def palindromos_view(request):
    # Define la vista `palindromos_view` que maneja las solicitudes a la página de palíndromos.
    resultado = None
    # Inicializa la variable `resultado` como None.
    if request.method == 'POST':
        # Verifica si la solicitud es de tipo POST.
        texto = request.POST.get('texto', '').replace(" ", "").lower()
        # Obtiene el texto del formulario, elimina los espacios y lo convierte a minúsculas.
        if texto == texto[::-1]:
            # Verifica si el texto es igual a su reverso (es un palíndromo).
            resultado = f'"{request.POST.get("texto")}" es un palíndromo.'
            # Si es un palíndromo, establece el resultado como un mensaje indicando que lo es.
        else:
            resultado = f'"{request.POST.get("texto")}" no es un palíndromo.'
            # Si no es un palíndromo, establece el resultado como un mensaje indicando que no lo es.
    return render(request, 'spa/palindromos.html', {'resultado': resultado})
    # Renderiza la plantilla 'palindromos.html' con el resultado de la verificación.from django.shortcuts import render
from django.shortcuts import render

def menu_view(request):
    return render(request, 'spa/base.html')  # Asegúrate de que la plantilla 'menu.html' exista en la carpeta 'templates/spa'

"""

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
"""