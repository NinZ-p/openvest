from pathlib import Path

from sentence_transformers import SentenceTransformer
import torch
import veclite

import json

import numpy as np

db = veclite.VecLite(r"C:\Users\joaol\c4_2026\open-vest\extraction\provas_final\tstast_db.vec")

with open(r"C:\Users\joaol\c4_2026\open-vest\extraction\provas_final\tstast_monolith.json","r") as file_obj:
    file_contents="".join(file_obj.readlines())
monolith=json.loads(file_contents)

MODEL_ID = "google/embeddinggemma-2"

model = SentenceTransformer(
    MODEL_ID,
    config_kwargs={"vision_config": None, "audio_config": None},
    model_kwargs={"dtype": torch.float32}
)

while True:
    querry=input("Type your querry:")
    vec=model.encode(querry, prompt_name="SearchQuery",truncate_dim=768,normalize_embeddings=True)

    results = db.search(vec, 64)

    scores=[]
    print("Search results:")
    for result in results:
        doc_id, score, _ = result
        scores.append([score,doc_id])
    scores=sorted(scores)[::-1]

    prscores=[[scores[i][0]-scores[i+1][0],scores[i][1]] for i in range(len(scores)-1)]
    
    midx=len(prscores)-1
    while midx>=0 and prscores[midx][0]<0.0075:
        midx-=1
    
    for r in prscores[:midx+1]:
        score, doc_id = r

        print(f" - Match: {doc_id} (Score: {score:.4f}) - Question {monolith[int(doc_id)]["numero_exercicio"]} - Test {monolith[int(doc_id)]["id_prova"]}")
