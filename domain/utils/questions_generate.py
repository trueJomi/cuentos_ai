from domain.utils.chat_gpt import ChatGpt
from domain.utils.decript_text import decript_evaluate, decript_questions
from domain.models.question_entity import QuestionModel

def generate_question( paragrafts:list[str], cantidad:int, type:str, reference:list[int]) ->list[QuestionModel]:
    if (type == 'literal'):
        chat = ChatGpt("QUESTION_PARAGRAFT_LITERAL")
        response = chat.hadleMsgChat(f'parrafo={paragrafts}. entregame las {cantidad} preguntas y respuestas')
    elif (type == 'inferencial'):
        chat = ChatGpt("QUESTION_PARAGRAFT_INFERENCIAL")
        response = chat.hadleMsgChat(f'parrafo={paragrafts}. entregame las {cantidad} preguntas y respuestas')
    elif (type == 'critico'):
        chat = ChatGpt("QUESTION_PARAGRAFT_CRITICO")
        response = chat.hadleMsgChat(f'parrafo={paragrafts}. entregame las {cantidad} preguntas y respuestas')
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
    
def generate_evaluation_question(cuento:list[str]) ->list[QuestionModel]:
    chat = ChatGpt("EVALUATE_QUESTIONS")
    response = chat.hadleMsgChat(f'texto={cuento}. entregame las 7 preguntas y respuestas')
    questions= decript_evaluate(response)
    total_questions =[]
    for question_literal in questions["liteal"]:
        temp_question = QuestionModel(list(range(len(cuento))), question_literal["question"], question_literal["response"], "literal")
        total_questions.append(temp_question)
    for question_inferencial in questions["inferencial"]:
        temp_question = QuestionModel(list(range(len(cuento))), question_inferencial["question"], question_inferencial["response"], "inferencial")
        total_questions.append(temp_question)
    for question_critico in questions["critico"]:
        temp_question = QuestionModel(list(range(len(cuento))), question_critico["question"], question_critico["response"], "critico")
        total_questions.append(temp_question)
    return total_questions