import pytest
from domain.utils.chat_gpt import ChatGpt
from domain.utils.decript_text import (decript_questions, decript_text_end,
    decript_text_introduccion, decript_text_middle, decript_text_tittle)


def test_queue_correctCreate():
    chat =  ChatGpt("QUESTION_PARAGRAFT_LITERAL")
    assert chat.queue != []


def test_message_is_string():
    chat =  ChatGpt("QUESTION_PARAGRAFT_LITERAL")
    with pytest.raises(Exception) as error_info:
        chat.hadleMsgChat(1234)
    assert str(error_info.value) != None

def test_result_introduction_regex():
    with open("tests/static/result_test.txt",encoding="utf-8") as result_raw:
        result_text = result_raw.read()
        introduction = decript_text_introduccion(result_text)
        assert introduction == ["Había una vez en un pequeño pueblo, una niña llamada Caperucita Roja. Era conocida por todos debido a su capa roja brillante que siempre llevaba puesta. Un día, su madre le pidió que llevara una canasta de golosinas a su abuela enferma que vivía al otro lado del bosque."]

def test_result_middle_regex():
    with open("tests/static/result_test.txt",encoding="utf-8") as result_raw:
        result_text = result_raw.read()
        middle = decript_text_middle(result_text)
        assert middle == ["Caperucita Roja se adentró en el frondoso bosque, siguiendo el camino que conocía tan bien. Mientras caminaba, se encontró con un astuto lobo que la detuvo. El lobo, con una sonrisa maliciosa, le preguntó a dónde iba. Caperucita Roja, inocentemente, le dijo que iba a visitar a su abuela y le mostró la canasta de golosinas.", "El lobo, con malas intenciones, le sugirió tomar un atajo a través del bosque para llegar más rápido. Sin sospechar nada, Caperucita Roja siguió sus consejos y tomó el nuevo camino. Mientras tanto, el lobo planeaba llegar primero a la casa de la abuela y hacerse pasar por Caperucita."]

def test_decript_text_no_middle():
    text = "Esto es el texto sin nudo."
    with pytest.raises(Exception):
        decript_text_middle(text)

def test_result_end_regex():
    with open("tests/static/result_test.txt",encoding="utf-8") as result_raw:
        result_text = result_raw.read()
        end = decript_text_end(result_text)
        assert end == ["Mientras Caperucita Roja seguía el atajo, la astuta abuela se dio cuenta de que el lobo no era su nieta. Cuando el lobo llegó a la casa, la abuela lo confrontó y logró asustarlo lo suficiente para que huyera. Mientras tanto, Caperucita Roja, habiendo sospechado algo extraño, regresó al camino principal y llegó a la casa de su abuela a tiempo para salvarla.","Finalmente, Caperucita Roja y su abuela compartieron un delicioso picnic con las golosinas que había llevado, agradecidas de que estuvieran a salvo. Aprendieron a no confiar en extraños y a seguir siempre el camino conocido.", "Así, Caperucita Roja y su abuela vivieron felices y seguras, sabiendo que la astucia del lobo no pudo vencer su inteligencia y precaución."]

def test_decript_text_no_end():
    text = "Esto es el texto final."
    with pytest.raises(Exception):
        decript_text_end(text)

def test_result_tittle_regex():
    with open("tests/static/result_test.txt",encoding="utf-8") as result_raw:
        result_text = result_raw.read()
        tittle = decript_text_tittle(result_text)
        assert tittle == "Caperucita Roja y el Lobo Amigo"



def test_decript_questions():
    data= "- ¿Quién es el personaje principal de la historia?\n* respuesta\n- ¿Cuál es la tarea que le encargan a Caperucita Roja?\n* respuesta\n- ¿Qué disfraz utiliza el lobo para engañar a Caperucita Roja?\n* respuesta\n- ¿Quiénes acuden en ayuda de Caperucita Roja cuando ella grita por ayuda?\n* respuesta"
    assert decript_questions(data) == [
        {
            "question":"¿Quién es el personaje principal de la historia?",
            "response":"respuesta"
        },
        {
            "question":"¿Cuál es la tarea que le encargan a Caperucita Roja?",
            "response":"respuesta"
        },
        {
            "question":"¿Qué disfraz utiliza el lobo para engañar a Caperucita Roja?",
            "response":"respuesta"
        },
        {
            "question":"¿Quiénes acuden en ayuda de Caperucita Roja cuando ella grita por ayuda?",
            "response":"respuesta"
        }
    ]

def test_ceunto_generate():
    chat =  ChatGpt("PROMPT_CREATE_CUENTO")
    
    assert chat.hadleMsgChat("Hola") != None