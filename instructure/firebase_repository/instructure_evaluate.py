from domain.models.evaluation_entity import EvaluationModel
from instructure.firebase_repository.firebase_comon import save_data

async def save_evaluation( data:EvaluationModel, id:str, uid:str):
    doc_dict = data.to_dict()
    await save_data(id,"Story",doc_dict,uid)
    return data