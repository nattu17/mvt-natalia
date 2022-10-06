from django.http import HttpResponse
from datetime import datetime
from django.template import Context, Template

def bienvenidos(request):
    return HttpResponse('<h1>Buenas clase 41765!</h1>')

def fecha(request):
    fecha_y_hora = datetime.now()
    return HttpResponse(f'<h1>La fecha y hora actual es {fecha_y_hora}</h1>')

def calcular_facha_nacimiento(request, edad):    
    fecha = datetime.now().year - edad    
    return HttpResponse(f'Tu fecha de nacimiento aproximada para tus {edad} años seria: {fecha}')

def mi_template(request):
    
    cargar_archivo = open(r'C:\Users\natal\Desktop\MVT_Natalia_Lopez_Gonzalez\template\template.html', 'r')    
    
    template = Template(cargar_archivo.read())  
      
    cargar_archivo.close()
    
    contexto = Context()
    
    template_renderizado = template.render(contexto)
    
    return HttpResponse(template_renderizado)