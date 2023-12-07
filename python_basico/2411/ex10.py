#Primeiramente o interpretador procura por módulos nativos
#Se não for encontrado, então ele procura por um arquivo em uma lista de diretórios dados pelo sys.path
#O sys.path utiliza a seguinte ordem:
    #primeiramente procura no diretório onde está o script sendo executado
    #segundamente no PYTHONPATH: variável de ambiente que é usada pelo python para especificar uma lista de diretórios dos quais os módulos podem ser importados
    #terceiramente o python busca no site-packages, que é onde ficam os módulos instalados pelo usuário