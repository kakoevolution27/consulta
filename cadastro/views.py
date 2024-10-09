from django.shortcuts import render
from django.http import HttpResponse, HttpResponseBadRequest, JsonResponse
from django.http import HttpRequest
from .models import Paciente
from .validators import Validator
from .CEP_Query import CEP_QUERY_VIA_CEP

validator = Validator()

# Create your views here.

def cadastro(request):
    if request.method == "POST":
        _nome = request.POST.get('name')
        _CPF = request.POST.get("CPF")
        _data_nascimento = request.POST.get("Data_de_Nascimento")
        _CNS = request.POST.get("CNS")
        _telefone_contato = request.POST.get("Telefone")

        if validator.Validar_CPF(_CPF.strip()):
            if validator.Validar_CNS(_CNS.strip()):
                cadastrar(_nome,_CPF,_data_nascimento,_CNS,_telefone_contato)
            else: 
                return HttpResponseBadRequest("CNS INVALIDO!")
        else:
        
                return HttpResponseBadRequest("CPF INVALIDO!")
        

        
    return render(request, 'index.html')

def cadastrar(_nome, _CPF, _Data_Nascimento, _CNS, _Telefone):
    paciente = Paciente(
        nome=_nome,
        CPF= _CPF,
        data_nascimento=_Data_Nascimento,
        CNS=_CNS,
        telefone_contato=_Telefone
        )
    paciente.save()


def pesquisarCep(request, cep): 
    consultor = CEP_QUERY_VIA_CEP()  
    try:
        response = consultor.Consultar(str(cep), "json")
        return JsonResponse(response) 
    except Exception as e:
        return JsonResponse({'error': str(e)}, status=500)