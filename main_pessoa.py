from Pessoa import Pessoa
from PessoaFisica import PessoaFisica
from PessoaJuridica import PessoaJuridica

Pessoa = Pessoa("João", "12345", "2024-01-01", True)
print("Instância da classe Pessoa:")
print(Pessoa.imprimir_valores())

pessoa_fisica = PessoaFisica("Ana", "67890", "2024-02-01", False, "1990-05-15", "000.111.222-33", "123456789")
print("\nInstância da classe PessoaFisica:")
print(pessoa_fisica.imprimir_valores())

pessoa_juridica = PessoaJuridica("Empresa X", "54321", "2024-03-01", True, "2020-06-01", "00.000.000/0001-00")
print("\nInstância da classe PessoaJuridica:")
print(pessoa_juridica.imprimir_valores())