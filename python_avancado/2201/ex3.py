import  threading

def reserva_lugar(semaforo, lugares, lugar_escolhido):
    
    print(f"{threading.current_thread().name} escolhendo o seu lugar!")
    with semaforo:
        if 0 not in lugares:
            print(f"{threading.current_thread().name}: Não há lugares disponíveis")
            return
        elif lugares[lugar_escolhido] != 0:
            print(f"{threading.current_thread().name}: O lugar escolhido já está ocupado.")
            for i in range(len(lugares)):
                if lugares[i]==0:
                    print(f"{threading.current_thread().name}: O seu lugar agora é o {i}")
                    lugares[i] = threading.current_thread().name
                    return
        lugares[lugar_escolhido] = threading.current_thread().name
        print(f"{threading.current_thread().name}: Seu lugar foi reservado. Poltrona {lugar_escolhido}")
        
        
def main():
    semaforo = threading.Semaphore(1)
    lugares = [0,0,0,0,0]
    
    pessoa1 = threading.Thread(target=reserva_lugar, name="pessoa1", args=[semaforo, lugares, 1])
    pessoa2 = threading.Thread(target=reserva_lugar, name="pessoa2", args=[semaforo, lugares, 1])
    pessoa3 = threading.Thread(target=reserva_lugar, name="pessoa3", args=[semaforo, lugares, 2])
    pessoa4 = threading.Thread(target=reserva_lugar, name="pessoa4", args=[semaforo, lugares, 4])
    pessoa5 = threading.Thread(target=reserva_lugar, name="pessoa5", args=[semaforo, lugares, 3])
    pessoa6 = threading.Thread(target=reserva_lugar, name="pessoa6", args=[semaforo, lugares, 3])
    
    pessoa1.start() 
    pessoa2.start() 
    pessoa3.start() 
    pessoa4.start()
    pessoa5.start()
    pessoa6.start()
    
    pessoa1.join()
    pessoa2.join()
    pessoa3.join()
    pessoa4.join()
    pessoa5.join()
    pessoa6.join()
    
    print(lugares)
    
    
if __name__ == "__main__":
    main()