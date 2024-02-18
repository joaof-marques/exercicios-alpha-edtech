import asyncio
import time

async def fritar_ovo ():
    print("Começou a fritar o ovo")
    await asyncio.sleep(3)
    print("Terminou de fritar o ovo")
    
    return "Ovo frito"

async def fazer_cafe ():
    print("Iniciou a coar o café")
    await asyncio.sleep(5)
    print("Terminou de coar o café")
    
    return "Café quentinho"

async def main ():    
    inicio = time.time()
    
    cafe_task = asyncio.create_task(fazer_cafe())
    ovo_task = asyncio.create_task(fritar_ovo())    
    
    ovo_frito = await ovo_task
    cafe = await cafe_task
    
    fim = time.time()    
    decorrido = fim - inicio
    
    print(f"Meu café da manhã é {ovo_frito} com {cafe}")
    print(f"Duração: {decorrido:.2f}")

if __name__ == "__main__":
    asyncio.run(main())