import asyncio
import time

async def preparar_arroz():
    print("Iniciando o cozimento do arroz...")
    await asyncio.sleep(8)
    print("Cozimento do arroz finalizado!")
    
    return "Arroz cozido soltinho"

async def fritar_carne():
    print("Começando a fritar a carte...")
    await asyncio.sleep(5)
    print("Terminou de fritar a carne!")
    
    return "Bife acebolado delicioso"

async def preparar_suco():
    print("Começou a espremer as laranjas...")
    for i in range(4):
        await asyncio.sleep(1)
        print(f"Espremeu a {i+1}ª laranja")
        
    print("Suco pronto!")
    
    return "Suco de laranja geladinho"

async def almocar():
    inicio_preparo = time.time()
    print("Iniciou o preparo do almoço!")
    await asyncio.sleep(1)
    
    tarefas_almoço = asyncio.gather(preparar_arroz(), fritar_carne(), preparar_suco())
    arroz, carne, suco = await tarefas_almoço
    
    fim_preparo = time.time()
    duracao_preparo = fim_preparo - inicio_preparo
    print(f"\nAlmoço pronto! Demorou {duracao_preparo:.2f} para fazer tudo!")
    print(f"\nO almoço de hoje é {arroz}, {carne} e {suco}")
    
if __name__ == "__main__":
    asyncio.run(almocar())