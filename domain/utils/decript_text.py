import re

def decript_text_introduccion(text:str) -> list[str]:
    introduction_raw = re.search(r'Inicio:(.*?)Nudo:', text, re.DOTALL)
    introduction_string = introduction_raw.group(1).strip()
    introduction = introduction_string.split('\n\n')
    return introduction

def decript_text_middle(text:str) ->list[str]:
    middle_raw = re.search(r'Nudo:(.*?)Desenlace:', text, re.DOTALL)
    middle_string = middle_raw.group(1).strip()
    middle = middle_string.split('\n\n')
    return middle

def decript_text_end(text:str) -> list[str]:
    end_raw = re.search(r'Desenlace:\s*(.*)', text, re.DOTALL)
    end_string = end_raw.group(1)
    end = end_string.split('\n\n')
    return end

def decript_text_tittle(text:str) -> str:
    tittle_raw = re.search(r'Título:\s*(.*)', text)
    tittle = tittle_raw.group(1)
    return tittle