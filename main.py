from cpf_cnpj import Documento

cpf = 12529892962
cnpj = 99436262000160

ob_cpf = Documento.cria_documento(cpf)
ob_cnpj = Documento.cria_documento(cnpj)

print(ob_cpf)
print(ob_cnpj)