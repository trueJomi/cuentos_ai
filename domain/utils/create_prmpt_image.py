from domain.utils.chat_gpt import ChatGpt
from copy import copy
from domain.utils.decript_text import concat_text_array, decript_prompt

def create_prompt(text:list[str]) -> str:
    gpt= ChatGpt("PROMPT_IMAGE_PROMPT")
    generate_prompt=copy(gpt)
    data = concat_text_array(text)
    prompt_cripted =generate_prompt.hadleMsgChat(f'contenido = {data}, respondeme con el prompt de este texto')
    is_prompt = True
    while is_prompt :
        try:
            prompt = decript_prompt(prompt_cripted)
            is_prompt = False
        except IndentationError as e:
            is_prompt = True
    return prompt