import re

def decript_text_introduccion(text:str) -> list[str]:
    introduction_raw = re.search(r'Inicio:(.*?)Nudo:', text, re.DOTALL)
    if introduction_raw :
        introduction_string = introduction_raw.group(1).strip()
        introduction = introduction_string.split('\n\n')
        return introduction
    else:
        raise Exception(text)

def decript_text_middle(text:str) ->list[str]:
    middle_raw = re.search(r'Nudo:(.*?)Desenlace:', text, re.DOTALL)
    if middle_raw :
        middle_string = middle_raw.group(1).strip()
        middle = middle_string.split('\n\n')
        return middle
    else:
        raise Exception(text)

def decript_text_end(text:str) -> list[str]:
    end_raw = re.search(r'Desenlace:\s*(.*)', text, re.DOTALL)
    if end_raw :
        end_string = end_raw.group(1)
        end = end_string.split('\n\n')
        return end
    else:
        raise Exception(text)

def decript_text_tittle(text:str) -> str:
    tittle_raw = re.search(r'Título:\s*(.*)', text)
    if tittle_raw :
        tittle = tittle_raw.group(1)
        return tittle
    else:
        raise Exception(text)