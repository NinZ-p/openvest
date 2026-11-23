print ("Program started")
from pathlib import Path
from PIL import Image,ImageChops,ImageCms,ImageOps
import os
import pymupdf
import io
print ("Loaded modules")

def extract_imgs_from_pdf(pdf_path,img_dir):
    if not os.path.exists(img_dir):
        os.makedirs(img_dir)
    
    doc = pymupdf.open(pdf_path)

    print (f"Found {len(doc)} pages in {pdf_path}")

    for page_num, page in enumerate(doc):
        images=page.get_images(full=True)
        img_count=0
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


            img_name=f"pg{page_num}img{img_count}.{ext}"
            try:
                img.save(str(img_dir/img_name))
            except:
                pass
            img_count+=1

program_path=Path(os.path.dirname(os.path.realpath(os.path.abspath(__file__))))
test_folder_path=program_path/"provas"
test_paths=[Path(test_folder_path/x) for x in os.listdir(test_folder_path)]
output_md_folder_path=program_path/"provas_markdown"

print (f"Found {len(test_paths)} files to process")

print ("Starting test conversion to MD")

for test_path in test_paths:
    extract_imgs_from_pdf(test_path,output_md_folder_path/f"{test_path.stem}_artifacts")

print ("Finished converting tests to MD")