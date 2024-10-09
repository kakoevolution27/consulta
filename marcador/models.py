from django.db import models
from cadastro.models import Clinicas, Profissional, Paciente, Especialidade

# Create your models here.

class Consultas(models.Model):
    id_consulta = models.AutoField(primary_key=True)
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas')
    profissional_executante = models.ForeignKey(Profissional, on_delete=models.CASCADE)
    data_da_consulta = models.DateField()
    hora_da_consulta = models.TimeField()
    local_da_consulta = models.ForeignKey(Clinicas, on_delete=models.CASCADE)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
