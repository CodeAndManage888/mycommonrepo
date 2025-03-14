import subprocess
import os

def convert_docx_to_pdf(input_path, output_path=None):
    if output_path is None:
        output_path = os.path.splitext(input_path)[0] + ".pdf"

    command = ["libreoffice", "--headless", "--convert-to", "pdf", input_path, "--outdir", os.path.dirname(output_path)]
    
    subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    
    if os.path.exists(output_path):
        print(f"Conversion complete: {output_path}")
    else:
        print("Conversion failed.")

# Example usage:
file_input = input("Enter Filename: ")
convert_docx_to_pdf(file_input)
