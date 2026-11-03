print ("Program started")

from docling.document_converter import DocumentConverter
from docling.datamodel.base_models import InputFormat
from docling.datamodel.pipeline_options import PdfPipelineOptions
from docling.document_converter import PdfFormatOption
from docling_core.types.doc import ImageRefMode
from pathlib import Path
import os

print ("Loaded modules")

program_path=Path(os.path.dirname(os.path.realpath(os.path.abspath(__file__))))
test_folder_path=program_path/"provas"
test_paths=[Path(test_folder_path/x) for x in os.listdir(test_folder_path)]
output_md_folder_path=program_path/"provas_markdown"

print (f"Found {len(test_paths)} files to process")

print ("Starting test conversion to MD")
pipeline_options = PdfPipelineOptions()
pipeline_options.generate_picture_images = True
pipeline_options.generate_page_images = True
pipeline_options.images_scale = 1.0

converter = DocumentConverter(
    format_options={
        InputFormat.PDF: PdfFormatOption(pipeline_options=pipeline_options)
    }
)

for test_path in test_paths:
    result = converter.convert(test_path)
    result.document.save_as_markdown(
        output_md_folder_path/test_path.stem,
        image_mode=ImageRefMode.REFERENCED
    )
print ("Finished converting tests to MD")