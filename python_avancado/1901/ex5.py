import asyncio
import time


#Agora, ao invés de começar a carne e o arroz juntos, vamos esperar o arroz cozinhar um pouco para depois começar a fritar a carne. Assim impedimos que a carne esteja fria quando tudo ficar pronto!
async def preparar_arroz(iniciar_carne, inicio_preparo):
    print("Iniciando o cozimento do arroz...")
    await asyncio.sleep(3)
    iniciar_carne.set()
    await asyncio.sleep(5)
    
    print(f"Cozimento do arroz finalizado aos {(time.time() - inicio_preparo):.2f} segundos")
    
    return "Arroz cozido soltinho"

async def fritar_carne(iniciar_carne, inicio_preparo):
    await iniciar_carne.wait()
    print(f"Começando a fritar a carte... Começou aos {(time.time() - inicio_preparo):.2f} segundos")
    await asyncio.sleep(5)
    print(f"Terminou de fritar a carne aos {(time.time() - inicio_preparo):.2f} segundos")
    
    return "Bife acebolado delicioso"

async def preparar_suco(inicio_preparo):
    print("Começou a espremer as laranjas...")
    # Comentei a contagem das laranjas apenas para diminuir os prints do programa e facilitar o entendimento das saídas
    # for i in range(4):
    #     await asyncio.sleep(1)
    #     print(f"Espremeu a {i+1}ª laranja")
    await asyncio.sleep(4)
    print(f"Suco pronto aos {(time.time() - inicio_preparo):.2f} segundos")
    
    return "Suco de laranja geladinho"

async def almocar():
    inicio_preparo = time.time()
    print("Iniciou o preparo do almoço!")
    
    iniciar_carne = asyncio.Event()
        
    tarefa_arroz = asyncio.create_task(preparar_arroz(iniciar_carne, inicio_preparo))
    tarefa_carne = asyncio.create_task(fritar_carne(iniciar_carne, inicio_preparo))
    tarefa_suco = asyncio.create_task(preparar_suco(inicio_preparo))
    
    arroz = await tarefa_arroz
    carne = await tarefa_carne
    suco = await tarefa_suco
    
    fim_preparo = time.time()
    duracao_preparo = fim_preparo - inicio_preparo
    print(f"\nAlmoço pronto! Demorou {duracao_preparo:.2f} para fazer tudo!")
    print(f"\nO almoço de hoje é {arroz}, {carne} e {suco}")
    
if __name__ == "__main__":
    asyncio.run(almocar())