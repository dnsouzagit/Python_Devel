paises = {'br':'Brasil', 'py': 'Pagaguai', 'ag':'Argentina,', 'ur':'Uruguai'}

pais= paises.get((input('digite o a sigla do pais:' )), 'Pais não econtrado na base de dados')

print(pais)
