import asyncio

async def fazer_cafe():
    print("Iniciando a coagem do café")
    await asyncio.sleep(3)
    print("Coagem do café finalizada")
    
    return "Café coado quentinho"

def callback_generico (future):
    print("Estou no callback!")
    # result = future.result
    print(future.result())

async def main():
    task_cafe = asyncio.create_task(fazer_cafe())
    task_cafe.add_done_callback(callback_generico)
    cafe = await task_cafe
    
    print(cafe)

if __name__ == "__main__":
    asyncio.run(main())