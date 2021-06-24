from validate_docbr import CPF, CNPJ

class Documento:

    @staticmethod
    def cria_documento(documento):
        documento = str(documento)
        if len(documento) == 11:
            return Doc_cpf(documento)
        elif len(documento) == 14:
            return Doc_cnpj(documento)
        else:
            raise ValueError("quantidade de digito errada!!")

class Doc_cpf:
    def __init__(self, documento):
        if self.valida(documento):
            self.cpf = documento
        else:
            raise ValueError("cpf invalido!!")

    def  valida(self, cpf):
        validador = CPF()
        return validador.validate(cpf)

    def formatar(self):
        mascara = CNPJ()
        return mascara.mask(self.cpf)

    def __str__(self):
        return self.formatar()

class Doc_cnpj:
    def __init__(self, documento):
        if self.valida(documento):
            self.cnpj = documento
        else:
            raise ValueError("cnpj invalido!!")

    def  valida(self, cnpj):
        validador = CNPJ()
        return validador.validate(cnpj)

    def formatar(self):
        mascara = CNPJ()
        return mascara.mask(self.cnpj)

    def __str__(self):
        return self.formatar()


