from domain.models.evaluation_entity import EvaluationModel
from instructure.firebase_repository.firebase_comon import save_data, save_data_with_id
from domain.models.question_evaluate import QuestionEvaluateModel

async def save_evaluation( data:EvaluationModel, id:str, uid:str):
    doc_dict = data.to_dict()
    await save_data(id,"Evaluation",doc_dict,uid)
    return data

async def save_question_evalaute(data:QuestionEvaluateModel, id:str, uid_evaluations:str):
    await save_data_with_id(id,f"Evaluation/{uid_evaluations}/Question",data.to_dict())
    return data