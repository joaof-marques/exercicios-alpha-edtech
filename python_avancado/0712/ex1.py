from typing import List

def get_user_words() -> str:
    return input("Insira a frase a ser analisada: ")

def count_x_ocurrences(words: str) -> int:    
    return words.lower().count("x")        

def inform_average(avg:int):
    print(f"The average X count is {avg}")
    
words = get_user_words()
Xcount = count_x_ocurrences(words)
inform_average(Xcount)