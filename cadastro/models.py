from django.db import models

# Create your models here.

class Clinicas(models.Model):
    logradouro = models.CharField(max_length=50)
    CEP = models.CharField(max_length=9)  
    numero = models.CharField(max_length=10, blank=True, null=True)  
    numero_consultorios = models.PositiveIntegerField() 


class Especialidade(models.Model):
    nome = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.nome

class Profissional(models.Model):
    class ClasseChoices(models.TextChoices):
        MEDICO = 'MED', 'Médico'
        ENFERMEIRO = 'ENF', 'Enfermeiro'
        PSICOLOGO = 'PSI', 'Psicologo'
        PSIQUIATRA = 'PSQ', 'Psiquiatra'
        TERAPEUTA_OCUPACIONAL = 'T.O', 'Terapeuta_Ocupacional'
        FISIOTERAPEUTA = 'FIS', 'Fisioterapeuta'
        FONOAUDIOLOGO = 'FON', 'Fonoaudiologo'
        RADIOLOGISTA = 'RAD', 'Radiologista'
        PATOLOGISTA = 'PAT', 'Patologista'
        BIOMEDICO = 'BIO', 'BioMedico'
        NUTRICIONISTA = 'NUT', 'Nutricionista'
        DENTISTA = 'DEN', 'Dentista'

    classe = models.CharField(
        max_length=3,  
        choices=ClasseChoices.choices,
        default=ClasseChoices.MEDICO  
    )
    nome_completo = models.CharField(max_length=100)
    CPF = models.CharField(max_length=11, unique=True)
    especialidade = models.ForeignKey(Especialidade, on_delete=models.CASCADE)
    numero_do_registro = models.CharField(max_length=10) 
    classe_do_registro = models.CharField(max_length=10)
    locais_de_trabalho = models.ManyToManyField(Clinicas)

class Paciente(models.Model):
    nome = models.CharField(max_length=50)
    CPF = models.CharField(max_length=11, unique=True)
    data_nascimento = models.DateField()
    CNS = models.CharField(max_length=15, unique=True)
    prontuario = models.AutoField(primary_key=True)
    telefone_contato = models.CharField(max_length=20, blank=True, null=True)
    logradouro = models.CharField(max_length=50)
    CEP = models.CharField(max_length=9) 
    numero_casa = models.CharField(max_length=10, blank=True, null=True)
    complemento = models.CharField(max_length=20, blank=True)
    def __str__(self):
        return self.nome
    
 

