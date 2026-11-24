print ("Loading modules")
from sentence_transformers import SentenceTransformer
from pathlib import Path
import torch
import veclite
import json
import os
print ("Loaded modules")

#Create monolith
program_path=Path(os.path.dirname(os.path.realpath(os.path.abspath(__file__))))
json_folder_path=program_path/"provas_json_comentadas"
json_paths=[Path(json_folder_path/x) for x in os.listdir(json_folder_path)]
markdown_folder_path=program_path/"provas_markdown"
markdown_paths=[Path(markdown_folder_path/x) for x in os.listdir(markdown_folder_path)]
image_folder_path=program_path/"provas_imagens"
db_folder_path=program_path/"vecdb"
db_path = db_folder_path/"db.vec"

#Create image monolith
image_paths=[]
for p in markdown_paths:
    if p.is_dir():
        for pt in os.listdir(p):
            image_paths.append(Path(p/pt))

image_aliases={}
crr_count=0
for p in image_paths:
    image_aliases[p.stem]=f"pimg{crr_count}.png"
    crr_count+=1

#Create json monolith

def preprocess_image_refs(ref):

#REVISAR ISSO: CONSIDERE QUE DÁ PA VE OS BAGUI DE MARKDOWN NO DIOXUS

    #Add selective image extraction from md to separate folder
    md_img_regex=r"^!\[([\w\d\s']+)\]\(([\w\d\-\.\/]+)\)"

    md_img_path_regex = re.compile(
        r'^!\[[^\]]*\]'
        r'\(((?![a-z][a-z0-9+.\-]*://|//|data:).+?)'
        r'(?:\s+(?:"[^"]*"|\'[^\']*\'|\([^)]*\)))?\)'
    )

    img_paths=[x.group(1) for x in md_img_path_regex.finditer(ref)]
    for p in img_paths:
        new_path=image_folder_path/image_aliases[p.stem]
        p.rename(new_path)


    return re.sub(md_img_regex,r'<img src="$2" alt="$1" />"',ref)

json_monolith_raw=[]

for p in json_paths:
    with open(p,"r") as file_obj:
        questoes_prova=json.loads("".join(file_obj.readlines()))
    for question in questoes_prova:
        nq=question.copy()
        nq["enunciado"]=preprocess_image_refs(nq["enunciado"])
        for x in range(len(nq["alternativas"])):
            nq["alternativas"][x]=preprocess_image_refs(nq["alternativas"][x])
        json_monolith_raw.append(nq)

with open(db_folder_path/"monolith.json","w") as file_obj:
    file_obj.writelines(json.dumps(json_monolith_raw))

#Do embeddings with refs to monolith

print ("Loading model")
MODEL_ID = "google/embeddinggemma-2"

model = SentenceTransformer(
    MODEL_ID,
    config_kwargs={"vision_config": None, "audio_config": None},
    model_kwargs={"dtype": torch.float32}
)
print ("Finished loading model")

print ("Creating/loading DB")
db = veclite.VecLite(db_path)
print ("Finished creating/loading DB")

print ("Embedding questions")

for idx,question in enumerate(json_monolith_raw):
    str_question=json.dumps(question)
    embedding = model.encode(str_question, prompt_name="Document",truncate_dim=256,normalize_embeddings=True)
    db.insert(idx, embedding)

print ("Finished embedding questions")