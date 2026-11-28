print ("Program started")

from pathlib import Path
from openai import OpenAI
from prompts import prompt_template_question_enrichment,system_prompt_json_commenting
from pydantic import BaseModel,Field
from typing import Literal

import os
import json

print ("Loaded modules")

MODEL_NAME="deepseek-flash"

program_path=Path(os.path.dirname(os.path.realpath(os.path.abspath(__file__))))
json_folder_path=program_path/"provas_json"
json_paths=[Path(json_folder_path/x) for x in os.listdir(json_folder_path)]
output_json_folder_path=program_path/"provas_json_comentadas"

print (f"Found {len(json_paths)} files to process")

print ("Starting test commenting")

client = OpenAI(
    api_key=os.environ["DEEPSEEK_API_KEY"],
    base_url="https://api.deepseek.com",
)

class ResponseSchema(BaseModel):
    id_prova: str
    numero_exercicio: int
    enunciado: str
    alternativas:  list[str] = Field(min_length=5, max_length=5)
    gabarito: Literal[-1, 0, 1, 2, 3, 4]
    comentarios:  list[str] = Field(min_length=5, max_length=5)
    materias: list[str]
    conteudos: list[str]
    dica: str

for json_path in json_paths:
    if json_path.is_file():
        if os.path.exists(output_json_folder_path/(json_path.stem+".json")):
            print (f"Found {output_json_folder_path/(json_path.stem+".json")} already there. Skipping conversion.")
        else:
            with open(json_path,"r",encoding="utf-8") as file_obj:
                file_contents="".join(file_obj.readlines())
            
            questions=json.loads(file_contents)

            final_json=[]

            for idx,question in enumerate(questions):
                prompt=prompt_template_question_enrichment.replace("{0}",json.dumps(question))

                print (f"Sending question {idx+1}/{len(questions)} to model.")
                
                for trcnt in range(4):
                    try:
                        response = client.responses.parse(
                            model=MODEL_NAME,
                            instructions=system_prompt_json_commenting,
                            input=prompt,
                            max_output_tokens=2**17,
                            text_format=ResponseSchema,
                            reasoning={"effort": "none"}
                        )
                        break
                    except:
                        pass

                json_contents_str=response.output_text
                json_contents=json.loads(json_contents_str)

                print (f"Received model answer: {str(json_contents)}")

                final_json.append(json_contents)

            final_json_str=json.dumps(final_json)
            with open(output_json_folder_path/(json_path.stem+".json"),"w",encoding="utf-8") as file_obj:
                file_obj.writelines(final_json_str)

print ("Finished converting tests to JSON")