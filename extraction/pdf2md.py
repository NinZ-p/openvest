print ("Program started")
from pathlib import Path
from PIL import Image,ImageChops,ImageCms,ImageOps
import os
import pymupdf
import io
import base64

from prompts import pdf2md_prompt
from openai import OpenAI

print ("Loaded modules")

def extract_imgs_from_pdf(pdf_path,img_dir):
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    
    doc = pymupdf.open(pdf_path)

    print (f"Found {len(doc)} pages in {pdf_path}")

    for page_num, page in enumerate(doc):
        pwidth,pheight=page.rect.width,page.rect.height

        images=page.get_images(full=True)
        img_count=0

        #Extract images
        for image in images:
            xref = image[0]
            smask = image[1]
            image_dict = doc.extract_image(xref)
            ext = image_dict["ext"]

            pix = pymupdf.Pixmap(doc, xref)

            try:
                pix = pymupdf.Pixmap(pymupdf.csRGB, pix)
            except:
                pass

            img = Image.open(io.BytesIO(pix.tobytes("png")))

            rects=page.get_image_rects(xref)
            rect=rects[0]
            x0,y0,x1,y1=rect.x0,rect.y0,rect.x1,rect.y1
            x0,x1=int(x0/pwidth*1000),int(x1/pwidth*1000)
            y0,y1=int(y0/pheight*1000),int(y1/pheight*1000)

            img_name=f"pg{page_num}img{img_count}_x0_{x0}_y0_{y0}_x1_{x1}_y1_{y1}.{ext}"
            img.save(str(img_dir/img_name))
            img_count+=1
        
    doc.close()

def convert_pdf2md(client,pdf_path,out_md_path,img_dir,temp_path):
    if os.path.exists(out_md_path):
        print (f"Found {out_md_path} already there. Skipping conversion.")
        return

    if not os.path.exists(img_dir):
        os.makedirs(img_dir)

    img_list=os.listdir(img_dir)

    doc = pymupdf.open(pdf_path)

    print (f"Found {len(doc)} pages in {pdf_path}")

    total_md=""

    for page_num, page in enumerate(doc):
        print (f"Processing page {page_num+1}/{len(doc)}")
        page_figure_list=list(filter(lambda x: f"pg{page_num}img" in x,img_list))
        print (f"Found {len(page_figure_list)} images in page")
        print (page_figure_list)
        zoom = 4
        mat = pymupdf.Matrix(zoom, zoom)
        pix = page.get_pixmap(matrix = mat)

        page_path=str(temp_path/f"{pdf_path.stem}_page_{page_num}.png")
        pix.save(page_path)

        #Get response
        print ("Sending message to chat model")

        with open(page_path, "rb") as f:
            b64 = base64.b64encode(f.read()).decode("utf-8")

        response = client.chat.completions.create(
            model="deepseek-flash",
            messages=[
                {
                    "role": "user",
                    "content": [
                        {
                            "type": "text",
                            "text": pdf2md_prompt.replace("{0}",str(page_figure_list))
                        },
                        {
                            "type": "image_url",
                            "image_url": {"url": f"data:image/jpeg;base64,{b64}"},
                        },
                    ]
                }
            ],
            reasoning_effort="none",
            extra_body={
                "detail": "high"
            }
        )


        print ("Received response from chat model")

        processed_md=str(response.choices[0].message.content)
        print (f"Received response: {processed_md}")
        total_md+=processed_md
        if total_md[-1]!="\n": total_md+="\n"
        total_md+="\n"
    with open(out_md_path,"w", encoding="utf-8") as file_obj:
        file_obj.writelines(total_md)

program_path=Path(os.path.dirname(os.path.realpath(os.path.abspath(__file__))))
test_folder_path=program_path/"provas"
test_paths=[Path(test_folder_path/x) for x in os.listdir(test_folder_path)]
output_md_folder_path=program_path/"provas_markdown"
temp_folder_path=program_path/"temp"

print (f"Found {len(test_paths)} files to process")

print ("Starting test conversion to MD")

#Extract images from PDF

"""
for test_path in test_paths:
    extract_imgs_from_pdf(test_path,output_md_folder_path/f"{test_path.stem}_artifacts")
"""

#Call VLM with PDF and prompt, saving result to corresponding file

client = OpenAI(api_key=os.getenv("DEEPSEEK_API_KEY"), base_url="https://api.deepseek.com")

for test_path in sorted(test_paths)[::-1]:
    convert_pdf2md(client,test_path,output_md_folder_path/f"{test_path.stem}.md",output_md_folder_path/f"{test_path.stem}_artifacts",temp_folder_path)

print ("Finished converting tests to MD")