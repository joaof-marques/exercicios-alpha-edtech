"""
    Escolher o método certo depende muito do contexto da utilização.
    O primeiro ponto a se considerar é a legibilidade:
        Colocar um loop dentro do outro é mais comum do que colocar um map dentro de outro ou um list comprehension dentro de outro.
        Cuidar de fatores como legibilidade são decisões de qualidade de código que vão afetar diretamente a manutenabilidade e crescimento do código
    O segundo fator é a decisão da equipe.
        Se foi definido no projeto que deve-se utilizar maps aninhados, então é isso que deve ser feito. Se for decidido que é melhor manter loops (for e while) aninhados, então é o que deve ser feito.
        Padrão em projetos são comuns e são decisões tomadas baseadas em divesos fatores. Não devem ser ignorados e nem alterados sem aprovações e análises prévias.
""" 