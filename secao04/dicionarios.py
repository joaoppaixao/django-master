pessoa = {'nome': 'João', 
          'idade': 20, 
          'profissao': 'Dev'
          }

print(f"Olá, {pessoa['nome']}! Você tem {pessoa['idade']} anos, e é um {pessoa['profissao']}!")

# para retornar as chaves do dicionario
print(pessoa.keys())

# para retornar os values 
print(pessoa.values())

# utilizando o get (melhor método)
print(pessoa.get('nome'))

# adicionando novos dados no dicionário
pessoa['ano_nascimento'] = 2005

print(pessoa)