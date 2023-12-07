def calculaDobro (x):
    return x*2

def funcaoPrincipal (nums):
    for num in nums:
        print(f"O dobro de {num} é {calculaDobro(num)}")
        
funcaoPrincipal([1, 2, 3, 4, 5, 6, 7, 8, 9])