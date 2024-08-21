import PyPDF2
import os
import datetime

def read_pdf(file_path, page_exer_nostr):
    target_list = page_exer_nostr.split()
    pages_to_read = [int(page) for page in target_list[1:]]

    with open(file_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = "".join([pdf_reader.pages[page].extract_text() for page in pages_to_read])

    return extract_exercise_text(text, target_list[0])

def extract_exercise_text(text, exercise_number):
    content = text.split("\n")
    start_txt = f"Exercise {exercise_number}:"
    end_txt = f"Exercise {int(exercise_number) + 1}:"

    start_pos = next((idx for idx, line in enumerate(content) if start_txt in line), None)
    end_pos = next((idx for idx, line in enumerate(content) if end_txt in line), None)

    if start_pos is None or end_pos is None:
        end_pos = next((idx for idx, line in enumerate(content) if "This copy belongs to" in line), None)

    if start_pos is not None and end_pos is not None:
        return content[start_pos:end_pos]

    return []

def format_then_write(textdata):
    file_path = "/home/runner/mycommonrepo/projects/module_template/outfile_cloud/gen_template.py"
    current_date = datetime.datetime.now().strftime("%m%d%y")
    title = textdata[0]
    line_code = textdata[1]

    TotCodPos = line_code.find("—")
    if TotCodPos == -1:
        TotCodPos = line_code.find("(")

    final_recs = [
        "#!/bin/bash",
        "#**************************************************************",
        f"# Date: {current_date} (Expected Solution with {line_code[TotCodPos + 1:TotCodPos + 3]} Lines of Code)      *",
        f"# Title:{title.split(':')[1]} {' ' * (55 - len(title.split(':')[1]))}*",
        "# Status: In Progress (In Progress / Testing / Working)       *"
    ]

    word_list = " ".join(textdata[2:]).split()
    formatted_lines = format_lines(word_list, 59)
    final_recs.extend(formatted_lines)

    final_recs.extend([
        "#                                                             *",
        "# Computed Result Validated:                                  *",
        "#**************************************************************",
        "#--------------------------------------------------------------",
        "def func_name(user_in):",
        "  return",
        "#--------------------------------------------------------------",
        'if __name__ == "__main__":',
        '  print("Thank you for using this app.")',
        "#**************************************************************"
    ])

    with open(file_path, "w") as file_handle:
        for item in final_recs:
            print(item)  # Uncomment for debugging
            print(item, file=file_handle)

def format_lines(words, line_length):
    lines = []
    current_line = ""

    for word in words:
        if len(current_line) + len(word) + 1 > line_length:
            lines.append(f"# {current_line}{' ' * (line_length - len(current_line))}*")
            current_line = word
        else:
            current_line += f" {word}"

    if current_line:
        lines.append(f"# {current_line}{' ' * (line_length - len(current_line))}*")

    return lines

if __name__ == "__main__":
    UserPageIn = input("Enter the exercise number & target page(s) - EEE PPP PPP: ")
    pdf_file_path = "/home/runner/mycommonrepo/projects/module_template/infile_cloud/The Python Workbook.pdf"
    tmp_data = read_pdf(pdf_file_path, UserPageIn)
    format_then_write(tmp_data)