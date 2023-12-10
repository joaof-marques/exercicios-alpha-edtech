from typing import List

def get_user_words() -> str:
    """
    Receives a string from user
    This is a pure function

    Returns:
        str: The input from the user with no modifications
    """
    return input("Insira a frase a ser analisada: ")

def count_x_ocurrences(words: str) -> int:    
    """
    Count X (or x) ocurrencies on the string given by the user
    This is a pure function because it doesn't alter the original string

    Args:
        words (str): The input received in get_user_words

    Returns:
        int: the count of X (or x) in the string
    """
    return words.lower().count("x")        

def inform_average(avg:int):
    """
    This function prints the X (or x) ocurrencies on the string
    This is a pure function because it just prints a info, not altering anything on the original value
    Args:
        avg (int): Receives the count from count_x_ocurrences
    """
    print(f"The average X count is {avg}")
    
words = get_user_words()
Xcount = count_x_ocurrences(words)
inform_average(Xcount)