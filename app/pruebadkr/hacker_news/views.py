import requests, json
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.cache import cache_page
from django.utils.decorators import method_decorator

#@method_decorator(cache_page(100, key_prefix='main'), name='dispatch')
def index(request):
    return render(request, "busqueda.html", {})

def is_integer(value):
	try:
		int(value)
		return True
	except:
		return False

def busqueda(request, inicio = 0, cantidad = 0):
	print("inicio:{}, cantidad:{}".format(inicio, cantidad))
	url = requests.get("https://hacker-news.firebaseio.com/v0/topstories.json?")
	# text = json.dumps(url.text)
	data = {}
	if is_integer(inicio) and is_integer(cantidad) and int(inicio) >= 0 and int(cantidad) > 0:
		identificaciones = url.json()
		identificaciones = identificaciones[inicio:inicio+cantidad]
		for identificacion in identificaciones:
			url_detalle = requests.get("https://hacker-news.firebaseio.com/v0/item/{}.json?print=pretty".format(identificacion))
			# detalle = url_detalle.json()
			detalle = url_detalle.text
			data[identificacion] = detalle
		# data["usuario_2"] = {"nombre":"Menganita", "apellido":"soles"}
	response_data = {"data":data}
	return HttpResponse(json.dumps(response_data), content_type="application/json")