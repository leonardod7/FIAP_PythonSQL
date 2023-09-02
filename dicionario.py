# lista
telefones = ['1234-5678', '9999-9999', '8765-4321', '8877-7788']

# tupla
contato = ('Yan', '1234-5678')

# lista de tuplas
contatos_lista = [('Yan', '1234-5678'), ('Pedro', '9999-9999'),
                    ('Ana', '8765-4321'), ('Marina', '8877-7788')]


# Ok! Se quisermos acessar o número de telefone da Marina, podemos fazer:

print(contatos_lista[3][1])

# E se quisermos o telefone do Pedro? Qual é mesmo a posição do Pedro na lista?

contatos = dict(contatos_lista)
print(contatos)

"""
print(contatos['Ana'])

print(contatos['João'])

print(contatos.get('Yan', 'Contato não encontrado'))
print(contatos.get('João', 'Contato não encontrado'))

print('Yan' in contatos)

print('9999-9999' in contatos)

print('9999-9999' in contatos.values())
"""