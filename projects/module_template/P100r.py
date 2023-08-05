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
        
        start_txt = "Exercise " + Target_List[1] + ":"
        end_txt = "Exercise " + str(int(Target_List[1]) + 1) + ":"
#        print(start_txt)                                                  # Uncomment for debugging
#        print(end_txt)                                                    # Uncomment for debugging
        return_block = []
        title_flag = False
        
        content = text.split("\n")
#        print(content)                                                   # Uncomment for debugging
        
        for line in content:
#            print(line)
            pos1 = line.find(start_txt)
            if pos1 != -1 and not title_flag:
                return_block.append(line)
                title_flag = True
            else:
                if title_flag:
                    pos2 = line.find(end_txt)
                    if pos2 != -1:
                        return_block.append(line)
                        title_flag = False
                        break
                    else:
                        return_block.append(line)
#        print(return_block)                                              # Uncomment for debugging
        return return_block

def format_then_write(textdata):
    file_path = "/home/runner/mycommonrepo/projects/module_template/outfile/temp000.py"
    
    # The following code will format the text
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%m%d%y")                     # Current date format MMDDYY
    final_recs = []
    line_code = textdata[1]
    rec00 = "#!/bin/bash"
    final_recs.append(rec00)
    
    rec01 = "#**************************************************************"
    final_recs.append(rec01)
    
    rec02 = "# Date: " + formatted_date + " (Expected Solution with " + line_code[1:3] + " Lines of Code)      *"
    final_recs.append(rec02)
    
    title = textdata[0]
    title_pos1 = title.index(":")
    space00 = 55 - len(title[title_pos1:])
    rec03 = "# Title:" + title[title_pos1 + 1:] + (" " * space00) + "*"
    final_recs.append(rec03)
    
    rec04 = "# Status: In Progress (In Progress / Testing / Working)       *"
    final_recs.append(rec04)
    
    templine, reqtdetail = ["", ""]
    char_ctr, item_ctr, word_ctr = [0, 0, 0]
    leftover = ""
    while item_ctr < (len(textdata) - 3):
        templine += (" " + textdata[item_ctr + 2])
        item_ctr += 1
    print(templine)
#    for idx, char in enumerate(templine):
#        reqtdetail += char
#        char_ctr += 1
#        if char_ctr == 59:
#            rec05 = "# " + reqtdetail + " *"
#            final_recs.append(rec05)
#            char_ctr = 0
#            reqtdetail = ""
            
    for idx, word in enumerate(templine):
        if len(reqtdetail) + len(word) < 59:
            reqtdetail += word
        else:
            rec05 = "# " + reqtdetail + "  *"
            final_recs.append(rec05)
            reqtdetail = ""
    
    rec06 = "#                                                             *"
    final_recs.append(rec06)
    
    rec07 = "# Computed Result Validated:                                  *"
    final_recs.append(rec07)
    
    rec08 = "#**************************************************************"
    final_recs.append(rec08)
    
    #print(final_recs)
    for item in final_recs:
        print(item,end="\n")

#    if os.path.exists(file_path):
#        record_exists = False
#        with open(file_path, "r") as file_record:
#            for line in file_handle:
#                if file_record in line:
#                    record_exists = True
#                    break
#        if not record_exists:
#            with open(file_path, "a") as file_handle:
#                    print(file_record, file=file_handle)
#    else:
#        with open(file_path, "w") as file_handle:
#            print(file_record, file=file_handle)

if __name__ == "__main__":
    UserPageIn = input("Enter the target page(s) & exercise number: ")
#    pdf_file_path = "/home/runner/mycommonrepo/projects/module_template/infile_replit/The Python Workbook.pdf"            # Path to your PDF file
    pdf_file_path = "/workspaces/mycommonrepo/projects/module_template/infile_replit/The Python Workbook.pdf"            # Path to your PDF file

    tmp_data = read_pdf(pdf_file_path, UserPageIn)
#    print(tmp_data)                                                      # Uncomment for debugging
    format_then_write(tmp_data)