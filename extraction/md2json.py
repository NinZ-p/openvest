print ("Program started")

from pathlib import Path
from openai import OpenAI
from prompts import system_prompt_md2json,prompt_template_md2json
import os

print ("Loaded modules")

MODEL_NAME="openrouter/free"

program_path=Path(os.path.dirname(os.path.realpath(os.path.abspath(__file__))))
md_folder_path=program_path/"provas_markdown"
md_paths=[Path(md_folder_path/x) for x in os.listdir(md_folder_path)]
output_json_folder_path=program_path/"provas_json"

print (f"Found {len(md_paths)} files to process")

print ("Starting test conversion to JSON")

client = OpenAI(
    api_key=os.environ["OPENROUTER_API_KEY"],
    base_url="https://openrouter.ai/api/v1",
)

for md_path in md_paths:
    if md_path.is_file():
        if "PV" in md_path.stem:
            with open(md_path,"r") as file_obj:
                file_contents="".join(file_obj.readlines())

            with open(md_path.replace("PV","GB"),"r") as file_obj:
                key_file_contents="".join(file_obj.readlines())
            
            prompt=prompt_template_md2json+file_contents+"\n\n"+key_file_contents

            response = client.responses.create(
                model=MODEL_NAME,
                instructions=system_prompt_md2json,
                input=prompt,
                max_output_tokens=2**17
            )

            json_contents=response.output_text

            with open(output_json_folder_path/(md_path.with_suffix(".json").stem),"w") as file_obj:
                file_obj.writelines(json_contents)

print ("Finished converting tests to JSON")