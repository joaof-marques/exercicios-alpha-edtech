import asyncio,time, csv
import concurrent.futures as cf
from functools import partial


def operacao_IO(executante):
    print(f"Inicio da operação IO no {executante}..")
    inicio = time.time()
    dados = []
    with open(f"pessoas_{executante}.txt", "r") as arquivo:
        csv_reader = csv.reader(arquivo)
        
        for linha in csv_reader:
            dados.append(linha)
        
        with open(f"escrever_{executante}.txt", "w") as arquivo_escrita:
            for linha in dados:
                arquivo_escrita.writelines(linha)
                
    fim = time.time()
    print(f"Fim da operação IO no {executante}. Duração: {(fim-inicio):.2f}")
    
def operacao_intensa_CPU(executante):
    print(f"Inicio da operação CPU no {executante}")
    inicio = time.time()
    resultado = 0
    for i in range(90000000):
        resultado += 1
    fim = time.time()
    print(f"Fim da operação CPU no {executante}. Duração: {(fim-inicio):.2f}")
    


async def main ():
    
    loop = asyncio.get_event_loop()

    
    # print("ProcessPoolExecutor")        
    pool = cf.ProcessPoolExecutor()
    io_multi = loop.run_in_executor(pool, partial(operacao_IO, "ProcessPoolExecutor"))
    cpu_multi = loop.run_in_executor(pool, partial(operacao_intensa_CPU, "ProcessPoolExecutor"))
    
    # print("Threading")
    th_pool = cf.ThreadPoolExecutor()
    io_task = loop.run_in_executor(th_pool, partial(operacao_IO, "Threading"))
    cpu_task = loop.run_in_executor(th_pool, partial(operacao_intensa_CPU, "Threading"))
    
    await asyncio.gather(io_task, cpu_task, io_multi, cpu_multi)

        
if __name__ == "__main__":
    asyncio.run(main())