import PyPDF2
import os
import datetime

def read_pdf(file_path, PageExerNoStr):
    Traget_List = []
    Target_List = PageExerNoStr.split()
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the total number of pages in the PDF
        num_pages = len(pdf_reader.pages)                                 # Do I still need this?

        # Get the text data
        page = pdf_reader.pages[int(Target_List[0])]
        text = page.extract_text()      
#        print(text)                                                       # Uncomment for debugging

        # Prepare the extraction of the target exercise only.
        content = text.split("\n")
#        print(content)                                                    # Uncomment for debugging
        start_txt = "Exercise " + Target_List[1] + ":"
        end_txt = "Exercise " + str(int(Target_List[1]) + 1) + ":"
#        print(start_txt)                                                  # Uncomment for debugging
#        print(end_txt)                                                    # Uncomment for debugging
        return_block = []
        start_pos_list = []
        end_pos_list = []

        # This line of codes will will identify the title and other starting/ending details.
        for idx1, line in enumerate(content):
            startpos = line.find(start_txt)
            if startpos != -1:
                start_pos_list.append(idx1)
            endpos = line.find(end_txt)
            if endpos != -1:
                end_pos_list.append(idx1)
                break
        
#        print(start_pos_list)                                             # Uncomment for debugging
#        print(end_pos_list)                                               # Uncomment for debugging

        line_ctr = start_pos_list[0]
        end_ctr = len(end_pos_list) - 1
        add_pos = len(start_pos_list) - 1
        while (line_ctr + add_pos) < end_pos_list[end_ctr]:
            if line_ctr == 0:
                num_start_dtls = len(start_pos_list)
                if num_start_dtls == 2 and line_ctr == 0:
                    return_block.append(content[line_ctr + add_pos])
                elif num_start_dtls == 2 and line_ctr == 1:
                    return_block.append(content[line_ctr + add_pos])
            else:
                return_block.append(content[line_ctr + add_pos])
            line_ctr += 1

#        print(return_block)                                              # Uncomment for debugging
        return return_block

def format_then_write(textdata):
    file_path = "/home/runner/mycommonrepo/projects/module_template/outfile/temp000.py"
    # The following code will format the text
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%m%d%y")                     # Current date format MMDDYY
    final_recs = []
    line_code = textdata[1]
    TotCodPos = line_code.find("—")
#    print(textdata)                                                     # Uncomment for debugging
#    print(line_code)                                                    # Uncomment for debugging
    rec00 = "#!/bin/bash"
    final_recs.append(rec00)
    rec01 = "#**************************************************************"
    final_recs.append(rec01)
    rec02 = "# Date: " + formatted_date + " (Expected Solution with " + line_code[TotCodPos + 1:TotCodPos + 3] + " Lines of Code)      *"
    final_recs.append(rec02)
    title = textdata[0]
    title_pos1 = title.index(":")
    space00 = 55 - len(title[title_pos1:])
    rec03 = "# Title:" + title[title_pos1 + 1:] + (" " * space00) + "*"
    final_recs.append(rec03)
    rec04 = "# Status: In Progress (In Progress / Testing / Working)       *"
    final_recs.append(rec04)

    word_list = []
    word_ctr, item_ctr, reqtdetail = (0, 2, "")
    while item_ctr <= (len(textdata) - 2):
        word_list += textdata[item_ctr].split(" ")
        item_ctr += 1
    print(word_list)
    print(len(word_list))

    while word_ctr <= len(word_list):
        if len(reqtdetail) < 59:
            popped_word = word_list.pop(word_ctr)
            reqtdetail += popped_word + " "
            if (len(reqtdetail) + len(word_list[word_ctr + 1])) > 59:
                rec05 = "# " + reqtdetail + "  *"
                final_recs.append(rec05)
        word_ctr += 1
    
    rec06 = "#                                                             *"
    final_recs.append(rec06)
    rec07 = "# Computed Result Validated:                                  *"
    final_recs.append(rec07)
    rec08 = "#**************************************************************"
    final_recs.append(rec08)

    for item in final_recs:                                               # Uncomment for debugging
        print(item)                                                       # Uncomment for debugging
    
if __name__ == "__main__":
    UserPageIn = input("Enter the target page(s) & exercise number: ")
#   pdf_file_path = "/home/runner/mycommonrepo/projects/module_template/infile_replit/The Python Workbook.pdf"           # Path to your PDF file (Cloud)
    pdf_file_path = "/workspaces/mycommonrepo/projects/module_template/infile_replit/The Python Workbook.pdf"            # Path to your PDF file (Cloud)
    tmp_data = read_pdf(pdf_file_path, UserPageIn)
    format_then_write(tmp_data)