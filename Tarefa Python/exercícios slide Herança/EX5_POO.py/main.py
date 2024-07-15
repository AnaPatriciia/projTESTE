from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

# Pessoa Física
pessoa_fisica = PessoaFisica("Ana", "987654321", "Ana@email.com", "Rua das Flores, 123", "123.456.789-00")
print(f"Nome: {pessoa_fisica.nome}\n CPF: {pessoa_fisica.cpf}")

pessoa_fisica.negociar()
pessoa_fisica.apresentar_documento()

print("___"*9)

# Pessoa Jurídica
pessoa_juridica = PessoaJuridica("Empresa ABC", "123456789", "empresa@email.com", "Av. Principal, 456", "12345678910")
print(f"Nome: {pessoa_juridica.nome}\n CNPJ: {pessoa_juridica.cnpj}")

pessoa_juridica.negociar()
pessoa_juridica.apresentar_documento()
