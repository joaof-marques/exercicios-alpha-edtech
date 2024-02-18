import asyncio

async def funcao_complexa(semaforo, nome_task):
    async with semaforo:
        print(f"{nome_task} starting")
        await asyncio.sleep(2)
        print(f"{nome_task} finishing")
        
async def main():
    semaforo = asyncio.Semaphore(3)
    tasks = [asyncio.create_task(funcao_complexa(semaforo, f"task{i}")) for i in range(8)]
    await asyncio.gather(*tasks)
    
if __name__ == "__main__":
    asyncio.run(main())