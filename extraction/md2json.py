print ("Program started")

from pathlib import Path
from openai import OpenAI
from prompts import system_prompt_md2json,prompt_template_md2json
from pydantic import BaseModel,Field
from typing import Literal

import os
import re
import json

print ("Loaded modules")

MODEL_NAME="deepseek-flash"

program_path=Path(os.path.dirname(os.path.realpath(os.path.abspath(__file__))))
md_folder_path=program_path/"provas_markdown"
md_paths=[Path(md_folder_path/x) for x in os.listdir(md_folder_path)]
#md_paths=[Path(x) for x in [
#    r"C:\Users\joaol\c4_2026\open-vest\extraction\provas_markdown\2023_GB_impresso_D1_CD1.md",
#    r"C:\Users\joaol\c4_2026\open-vest\extraction\provas_markdown\2023_GB_impresso_D2_CD5.md",
#    r"C:\Users\joaol\c4_2026\open-vest\extraction\provas_markdown\2023_PV_impresso_D1_CD1.md",
#    r"C:\Users\joaol\c4_2026\open-vest\extraction\provas_markdown\2023_PV_impresso_D2_CD5.md",
#    r"C:\Users\joaol\c4_2026\open-vest\extraction\provas_markdown\2024_GB_impresso_D1_CD1.md",
#    r"C:\Users\joaol\c4_2026\open-vest\extraction\provas_markdown\2024_GB_impresso_D2_CD5.md",
#    r"C:\Users\joaol\c4_2026\open-vest\extraction\provas_markdown\2024_PV_impresso_D1_CD1.md",
#    r"C:\Users\joaol\c4_2026\open-vest\extraction\provas_markdown\2024_PV_impresso_D2_CD5.md"
#]]
output_json_folder_path=program_path/"provas_json"

print (f"Found {len(md_paths)} files to process")

print ("Starting test conversion to JSON")

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

for md_path in md_paths:
    final_json=[]
    if md_path.is_file():
        if "PV" in md_path.stem:
            if os.path.exists(output_json_folder_path/(md_path.stem+".json")):
                print (f"Found {output_json_folder_path/(md_path.stem+".json")} already there. Skipping conversion.")
            else:
                print (f"Processing {md_path}")
                with open(md_path,"r",encoding="utf-8") as file_obj:
                    file_contents="".join(file_obj.readlines())

                with open(str(md_path).replace("PV","GB"),"r",encoding="utf-8") as file_obj:
                    key_file_contents="".join(file_obj.readlines())
                
                pattern=r"#\s*QUESTÃO\s+\d+"
                matches=[(m.start(0), m.group()) for m in re.finditer(pattern, file_contents)]
                matches.append((-1,""))

                questions=[]

                for idx,(mstart,mgroup) in enumerate(matches[:-1]):
                    nmstart,nmgroup=matches[idx+1]

                    questions.append(file_contents[mstart:nmstart])

                for idx,question in enumerate(questions):
                    print (f"Processing question number {idx}")

                    # Use structured decoding and adjust prompt to guarantee right form of output
                    
                    prompt=prompt_template_md2json.replace("{0}",md_path.stem).replace("{1}",key_file_contents).replace("{2}",question)

                    print("Sending model request")
                    response = client.responses.parse(
                        model=MODEL_NAME,
                        instructions=system_prompt_md2json,
                        input=prompt,
                        max_output_tokens=2**17,
                        text_format=ResponseSchema,
                        reasoning={"effort": "none"}
                    )

                    json_contents_str=response.output_text

                    json_contents=json.loads(json_contents_str)

                    print(f"Received back json for question: {str(json_contents)}")

                    final_json.append(json_contents)

                final_json_str=json.dumps(final_json)
                with open(output_json_folder_path/(md_path.stem+".json"),"w",encoding="utf8") as file_obj:
                    file_obj.writelines(final_json_str)

print ("Finished converting tests to JSON")