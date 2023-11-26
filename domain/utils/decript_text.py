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
        title = tittle_raw.group(1)
        return title
    else:
        raise Exception(text)

def concat_text_array(text_array:list[str]) -> str:
    text = ""
    for text_line in text_array:
        text = text + text_line + " "
    return text

def decript_prompt( text:str):
    parts=text.split("Prompt:")
    part_prompt= parts[1]
    return part_prompt

def decript_questions(text:str) -> list[dict]:
    question_match= re.findall(r'- .*',text)
    responses_match= re.findall(r'\* .*',text)
    questions=[]
    for quest, res in zip(question_match,responses_match):
        temp_quest = quest.split("- ")[1]
        temp_res = res.split("* ")[1]
        questions.append({
            "question":temp_quest,
            "response":temp_res
        })
    return questions
