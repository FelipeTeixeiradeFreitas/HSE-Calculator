from django.db import models

# Create your models here.


class TbDimSaida(models.Model):
    tb_dim_saida_id = models.AutoField(primary_key=True)
    tb_dim_saida_id_grupo = models.ForeignKey('TbLocalOcupacao', models.DO_NOTHING, db_column='tb_dim_saida_id_grupo', blank=True, null=True)
    tb_dim_saida_capacidade = models.TextField()
    tb_dim_saida_variavel = models.TextField()
    tb_dim_saida_formula = models.TextField()
    tb_dim_saida_descargas = models.IntegerField()
    tb_dim_saida_escadas = models.IntegerField()
    tb_dim_saida_portas = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tb_dim_saida'


class TbLgMinima(models.Model):
    tb_lg_minima_id = models.AutoField(primary_key=True)
    tb_lg_minima_n_min = models.IntegerField(blank=True, null=True)
    tb_lg_minima_n_max = models.IntegerField(blank=True, null=True)
    tb_lg_minima_valor = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'tb_lg_minima'


class TbLocalOcupacao(models.Model):
    tb_local_ocupacao_id = models.AutoField(primary_key=True)
    tb_local_ocupacao_grupo = models.TextField()
    tb_local_ocupacao_ocupacao = models.TextField()
    tb_local_ocupacao_divisao = models.TextField()
    tb_local_ocupacao_descricao = models.TextField()
    tb_local_ocupacao_exemplos = models.TextField()

    class Meta:
        managed = False
        db_table = 'tb_local_ocupacao'
