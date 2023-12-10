from typing import Optional

def soma_ou_multiplica(a: int, b:int, c:Optional[bool]=None) -> int:
    if c: return a*b
    else: return a+b
    
"""informar bool no 3 parâmetro para multilplicar ao invés de somar
Note que o False tem o mesmo comportamento da omissão do parâmetro"""

print(soma_ou_multiplica(2, 4))
print(soma_ou_multiplica(2, 4, True))
print(soma_ou_multiplica(2, 4, False))
