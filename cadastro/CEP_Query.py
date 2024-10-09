from abc import ABC, abstractmethod
import json
import requests


class CEP_QUERY_Interface(ABC):
    @abstractmethod
    def Consultar(parametro):
        pass
    @abstractmethod
    def FormatarDict(parametro):
        pass

class CEP_QUERY_VIA_CEP(CEP_QUERY_Interface): 
    def __init__(self) -> None:
        self.via_cep_URL = f"https://viacep.com.br/ws"

    def Consultar(self, _cep:str, _retorno:str):
        url = self.via_cep_URL + f"/{_cep}/{_retorno}"
        response = requests.get(url)
    
        if response.status_code != 200:
            raise Exception(f"Erro na consulta do CEP: {response.status_code} - {response.text}")
    
        return response.text
    
    def FormatarDict(parametro):
        return json.loads(parametro)


     