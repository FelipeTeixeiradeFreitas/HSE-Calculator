from .models import *
import pandas as pd
from django.views import View
from django.shortcuts import render
from .input_data import dimencionamento
from .input_data import consulta_divisao
from .input_data import consulta_divisao
from .input_data import busca_codigo
from .input_data import busca_tipo_variavel
from django.http import JsonResponse
import json
class tabela_dados(View):

    template_name = 'tabela_dados.html'

    def get(self, request):
        #dimencionamento('A-3', '15')
        valor=consulta_divisao('Residencial')
        valor2=busca_codigo(valor[0])
        valor3=busca_tipo_variavel(valor[0])
        return render(request, self.template_name)

class AjaxNextLevel(View):
    def get(self, request):
        print('aoba')
        ocupacao = request.GET['OCUPACAO']
        opcoes = consulta_divisao(ocupacao)
        return JsonResponse({'message': 'Success', 'OPCOES': opcoes})

class AjaxNextLevel2(View):
    def get(self, request):
        print('aoba')
        subgrupo = request.GET['SUBGRUPO']
        variavel = busca_tipo_variavel(subgrupo)
        label = '3 - Informe ' + variavel + ': '
        return JsonResponse({'message': 'Success', 'LABEL': label})
    def post(self, request):
        print('aoba')
        dict_request = json.loads(request.POST.get('new_item'))
        tetea = dict_request['SUBGRUPO']
        testeb = dict_request['VARIAVEL']
        medida = dimencionamento(dict_request['SUBGRUPO'], dict_request['VARIAVEL'])
        resposta_acessos = 'Largura mínima de acessos e descargas: ' + str(medida['ESCADAS']) + ' m²'
        resposta_escadas = 'Largura mínima de escadas e rampas: ' + str(medida['ESCADAS']) + ' m²'
        resposta_portas = 'Largura mínima de portas: ' + str(medida['ESCADAS']) + ' m²'
        return JsonResponse({'message': 'Success', 'DESCARGAS': resposta_acessos, 'ESCADAS': resposta_escadas, 'PORTAS': resposta_portas})
