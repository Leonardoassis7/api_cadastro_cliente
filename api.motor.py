from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from pymongo import MongoClient

# Conexão com MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client["meu_banco"]
collection = db["empresas"]

app = FastAPI()

# Modelo de entrada
class ServicoInput(BaseModel):
    empresa_id: str
    municipio: str
    login: str
    senha: str
    certificado: bool

@app.post("/empresas/servicos")
def add_servico(servico: ServicoInput):
    empresa = collection.find_one({"_id": servico.empresa_id})

    if not empresa:
        # Cria empresa nova se não existir
        nova_empresa = {
            "_id": servico.empresa_id,
            "nome_empresa": f"Empresa {servico.empresa_id}",
            "servicos": {}
        }
        collection.insert_one(nova_empresa)
        empresa = nova_empresa

    # Serviço estruturado por município
    novo_servico = {
        "login": servico.login,
        "senha": servico.senha,
        "certificado": servico.certificado
    }

    # Atualiza ou insere o serviço dentro do município
    collection.update_one(
        {"_id": servico.empresa_id},
        {"$set": {f"servicos.{servico.municipio}": novo_servico}}
    )

    return {"message": f"Serviço para município {servico.municipio} adicionado/atualizado com sucesso"}
