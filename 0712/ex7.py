"""
O problema com tipos mutáveis é que dependendo do fluxo do código, quando os tipos não são fortemente controlados, é que alterações inesperadas podem surgir e quebrar o código em algum momento.
Se não houver um cuidado com os tipos e operações efetuadas, podemos acabar recebendo um tipo não esperado e o código travar, necessitando de alguma manutenção.

Por exemplo, se passarmos uma string para uma função que calcula média de valores, esse código vai gerar erros pois não é possível somar e subtrair strings e valores numéricos.

"""