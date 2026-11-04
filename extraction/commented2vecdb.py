print ("Loading modules")
from sentence_transformers import SentenceTransformer
from pathlib import Path
import torch
import veclite
import json
import os
print ("Loaded modules")

print ("Loading model")
MODEL_ID = "google/embeddinggemma-2"

model = SentenceTransformer(
    MODEL_ID,
    config_kwargs={"vision_config": None, "audio_config": None},
    model_kwargs={"dtype": torch.float32}
)
print ("Finished loading model")

print ("Creating/loading DB")
db_path = "vecdb/db.vec"
db = veclite.VecLite(db_path)
print ("Finished creating/loading DB")

print ("Embedding questions")
program_path=Path(os.path.dirname(os.path.realpath(os.path.abspath(__file__))))
json_folder_path=program_path/"provas_json_comentadas"
json_paths=[Path(json_folder_path/x) for x in os.listdir(json_folder_path)]

for json_path in json_paths:
    with open(json_path,"r") as file_obj:
        file_contents="".join(file_obj.readlines())
    
    parsed_file_contents=json.loads(file_contents)

    for question in parsed_file_contents:
        str_question=json.dumps(question)
        embedding = model.encode(str_question, prompt_name="Document",truncate_dim=256,normalize_embeddings=True)
        db.insert(str_question, embedding)

print ("Finished embedding questions")
