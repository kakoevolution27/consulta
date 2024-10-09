import re

class Validator():
    def Validar_CPF(self, _CPF:str) -> bool:
        cpf_regex = r'^\d{3}\.\d{3}\.\d{3}-\d{2}$'
        #formata o cpf para o padrao esperado
        formatted_cpf = f"{_CPF[:3]}.{_CPF[3:6]}.{_CPF[6:9]}-{_CPF[9:11]}"
        if re.match(cpf_regex, formatted_cpf):
            return True
        else:
            return False
    def Validar_CNS (self,_CNS: str) -> bool:
        # se CNS for um digito ou seu comprimento menor que 15
        if not _CNS.isdigit() or len(_CNS) != 15:
            return False

        # CNS começando com 1 ou 2 segue a regra de validação com dígito verificador
        if _CNS.startswith('1') or _CNS.startswith('2'):
            soma = sum(int(_CNS[i]) * (15 - i) for i in range(15))
            return soma % 11 == 0

        # CNS começando com 7, 8 ou 9 é proveniente de INSS
        elif _CNS.startswith('7') or _CNS.startswith('8') or _CNS.startswith('9'):
            soma = sum(int(_CNS[i]) * (15 - i) for i in range(15))
            return soma % 11 == 0
 
        return False

