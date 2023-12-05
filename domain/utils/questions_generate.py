from domain.utils.chat_gpt import ChatGpt
from domain.utils.decript_text import decript_evaluate, decript_questions
from domain.models.question_entity import QuestionModel

def generate_question( paragrafts:list[str], cantidad:int, type:str, reference:list[int]) ->list[QuestionModel]:
    if (type == 'literal'):
        chat = ChatGpt("QUESTION_PARAGRAFT_LITERAL")
        response = chat.hadleMsgChat(f'parrafo={paragrafts}. deveuveme las {cantidad} preguntas y respuestas')
    elif (type == 'inferencial'):
        chat = ChatGpt("QUESTION_PARAGRAFT_INFERENCIAL")
        response = chat.hadleMsgChat(f'parrafo={paragrafts}. deveuveme las {cantidad} preguntas y respuestas')
    elif (type == 'critico'):
        chat = ChatGpt("QUESTION_PARAGRAFT_CRITICO")
        response = chat.hadleMsgChat(f'parrafo={paragrafts}. deveuveme las {cantidad} preguntas y respuestas')
    else:
        raise Exception("type not valid")
    print(response)
    questions_raw = decript_questions(response)
    questions=[]
    for question in questions_raw:
        question_temp = QuestionModel(reference, question["question"], question["response"], type)
        questions.append(question_temp)
    return questions

def validate_type(type:str):
    if (type == 'literal'):
        return True
    elif (type == 'inferencial'):
        return True
    elif (type == 'critico'):
        return True
    else:
        raise Exception("type not valid")
    
def generate_evaluation_question(cuento:list[str]):
    chat = ChatGpt("EVALUATE_QUESTIONS")
    response = chat.hadleMsgChat(f'text={cuento}. deveuveme las preguntas y opciones de las respuestas')
    questions= decript_evaluate(response)
    return questions

def commpare_text_response(response:str, correct_response:str):
    chat = ChatGpt("COMPARE_RESPONSE")
    respuesta = chat.hadleMsgChat(f'repuesta={response} respuestaCorrecta={correct_response}. ')
    return respuesta