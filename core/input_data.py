#from .models import TbLocalOcupacao
from .models import *
import pandas as pd
from sympy import sympify, symbols


def input_data_ocupacao():
    excel_file = 'C:\\Tabelaço\\core\\templates\\Pasta1.xlsx'
    try:
        df = pd.read_excel(excel_file)
        for index, row in df.iterrows():
            nova_query = TbLocalOcupacao(tb_local_ocupacao_ocupacao=row['Ocupação /Uso'],
                                         tb_local_ocupacao_grupo=row['Grupo'],
                                         tb_local_ocupacao_descricao=row['Descrição'],
                                         tb_local_ocupacao_divisao=row['Divisão'],
                                         tb_local_ocupacao_exemplos=row['Exemplos'])
            nova_query.save()
    except Exception as e:
        print(e)


def input_data_dim_saida():
    excel_file = 'C:\\Tabelaço\\core\\templates\\Pasta2.xlsx'
    try:
        df = pd.read_excel(excel_file)
        t2=df.columns
        for index, row in df.iterrows():
            id_ocupacao=TbLocalOcupacao.objects.get (tb_local_ocupacao_divisao=row['Ocupação'])

            nova_query = TbDimSaida(tb_dim_saida_id_grupo=id_ocupacao,
                                    tb_dim_saida_capacidade=row['Capacidade da U de passagem'],
                                    tb_dim_saida_variavel=row['Variavel'],
                                    tb_dim_saida_formula=row['Formula'],
                                    tb_dim_saida_descargas=row['Acesso e descargas'],
                                    tb_dim_saida_escadas=row['Escadas'],
                                    tb_dim_saida_portas=row['Portas'])
            nova_query.save()
    except Exception as e:
        print(e)



def dimencionamento(codigo, valor_v):
    id_codigo=TbLocalOcupacao.objects.get(tb_local_ocupacao_descricao=codigo).pk
    dimencionamento = TbDimSaida.objects.get(tb_dim_saida_id_grupo=id_codigo)
    formula_str = dimencionamento.tb_dim_saida_formula
    descargas = dimencionamento.tb_dim_saida_descargas
    escadas = dimencionamento.tb_dim_saida_escadas
    portas = dimencionamento.tb_dim_saida_portas
    v = symbols('v')
    formula = sympify(formula_str)
    populacao = formula.subs(v, valor_v)
    n_descargas = float(populacao / descargas)
    n_escadas = float(populacao / escadas)
    n_portas = float(populacao / portas)
    busca_descargas=TbLgMinima.objects.filter(tb_lg_minima_n_max__gt=n_descargas,
                                               tb_lg_minima_n_min__lt=n_descargas).first()
    if busca_descargas:
        resultado_descargas = busca_descargas.tb_lg_minima_valor
    busca_escadas = TbLgMinima.objects.filter(tb_lg_minima_n_max__gt=n_escadas,
                                                 tb_lg_minima_n_min__lt=n_escadas).first()
    if busca_escadas:
        resultado_escadas = busca_escadas.tb_lg_minima_valor
    busca_portas = TbLgMinima.objects.filter(tb_lg_minima_n_max__gt=n_portas,
                                                 tb_lg_minima_n_min__lt=n_portas).first()
    if busca_portas:
        resultado_portas = busca_portas.tb_lg_minima_valor
    return {'DESCARGAS': resultado_descargas, 'ESCADAS': resultado_escadas, 'PORTAS': resultado_portas}



def consulta_divisao(ocupacao):
    opcoes = []
    id_codigos = TbLocalOcupacao.objects.filter(tb_local_ocupacao_ocupacao=ocupacao)
    for i in id_codigos:
        opcoes.append(i.tb_local_ocupacao_descricao)
    return opcoes


def busca_codigo(descricao):
    id_codigo = TbLocalOcupacao.objects.filter(tb_local_ocupacao_descricao=descricao).first()
    if id_codigo:
        resultado = id_codigo.tb_local_ocupacao_divisao
        return resultado


def busca_tipo_variavel(descricao):
    id_codigo = TbLocalOcupacao.objects.filter(tb_local_ocupacao_descricao=descricao).first()
    tipo_variavel = TbDimSaida.objects.get(tb_dim_saida_id_grupo=id_codigo).tb_dim_saida_variavel
    return tipo_variavel