print ("Program started")

from pathlib import Path
from openai import OpenAI
from prompts import system_prompt_md2json,prompt_template_md2json
import os

print ("Loaded modules")

MODEL_NAME="openrouter/free"

program_path=Path(os.path.dirname(os.path.realpath(os.path.abspath(__file__))))
json_folder_path=program_path/"provas_json"
json_paths=[Path(json_folder_path/x) for x in os.listdir(json_folder_path)]
output_json_folder_path=program_path/"provas_json_comentadas"

print (f"Found {len(md_paths)} files to process")

print ("Starting test commenting")

client = OpenAI(
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1",
)

for json_path in json_paths:
    if json_path.is_file():
        with open(json_path,"r") as file_obj:
            file_contents="".join(file_obj.readlines())
        
        prompt=prompt_template_question_enrichment+file_contents

        response = client.responses.create(
            model=MODEL_NAME,
            instructions=system_prompt_json_commenting,
            input=prompt,
            max_output_tokens=2**17
        )

        json_contents=response.output_text

        with open(output_json_folder_path/(json_path.stem),"w") as file_obj:
            file_obj.writelines(json_contents)

print ("Finished converting tests to JSON")