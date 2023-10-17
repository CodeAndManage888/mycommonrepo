import PyPDF2
import os
import datetime

def read_pdf(file_path, page_exer_nostr):
    target_list = page_exer_nostr.split()
    page_ctr = len(target_list) - 1
    with open(file_path, 'rb') as file:
        # Create a PDF reader object
        pdf_reader = PyPDF2.PdfReader(file)

        # Get the total number of pages in the PDF
        num_pages = len(pdf_reader.pages)                                                # Do I still need this?

        # Get the text data
        idx4 = 1
        text = ""
        while page_ctr != 0:
            page = pdf_reader.pages[int(target_list[idx4])]
            page_ctr -= 1
            idx4 += 1
            text += page.extract_text()
#        print(text)                                                                     # Uncomment for debugging

        # Prepare the extraction of the target exercise only.
        content = text.split("\n")
#        print(content)                                                                  # Uncomment for debugging
        start_txt = "Exercise " + target_list[0] + ":"
        end_txt = "Exercise " + str(int(target_list[0]) + 1) + ":"
#        print(start_txt)                                                                # Uncomment for debugging
#        print(end_txt)                                                                  # Uncomment for debugging
        return_block = []
        start_pos_list = []
        end_pos_list = []

        # This line of codes will will identify the title and other starting/ending details.
        start_flag = False
        for idx1, line in enumerate(content):
            startpos = line.find(start_txt)
            if startpos != -1 and not start_flag:
                start_pos_list.append(idx1)
                start_flag = True
            endpos = line.find(end_txt)
            if endpos != -1:
                end_pos_list.append(idx1)
                break
            else:
                endpos = line.find("This copy belongs to")
                if endpos != -1 and len(target_list) == 2:
                    end_pos_list.append(idx1)
                    break

#        print(start_pos_list)                                                           # Uncomment for debugging
#        print(end_pos_list)                                                             # Uncomment for debugging

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

#        print(return_block)                                                             # Uncomment for debugging
        return return_block

def format_then_write(textdata):
#    file_path = "/workspaces/mycommonrepo/projects/module_template/outfile_cloud/gen_template.py"                   # Path to your outfile (Cloud)
#    file_path = "/workspaces/inoutfiles/projects/module_template/outfile_cloud/gen_template.py"                      # Path to your outfile (Cloud)
    file_path = "/home/runner/mycommonrepo/projects/module_template/outfile_cloud/gen_template.py"                  # Path to your outfile (Desktop)

    # The following code will format the text
    current_date = datetime.datetime.now()
    formatted_date = current_date.strftime("%m%d%y")                                     # Current date format MMDDYY
    final_recs = []
    line_code = textdata[1]
    TotCodPos = line_code.find("—")
    if TotCodPos == -1:
        TotCodPos = line_code.find("(")
#    print(textdata)                                                                     # Uncomment for debugging
#    print(line_code)                                                                    # Uncomment for debugging
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
    for idx3, readline in enumerate(textdata):
        if idx3 != 0 and idx3 != 1:
            word_list += readline.split(" ")

#    print(word_list)                                                                    # Uncomment for debugging
#    print(len(word_list))                                                               # Uncomment for debugging

    reqtdetail = ""
    for idx2, word in enumerate(word_list):
        reqtdetail += word + " "
        if idx2 != (len(word_list) - 1):
            if (len(reqtdetail) + len(word_list[idx2 + 1])) > 59:
                addspaces = 59 - (len(reqtdetail) - 1)
                rec05 = "# " + reqtdetail + (addspaces * " ") + "*"
                final_recs.append(rec05)
                reqtdetail = ""
        else:
            addspaces = 59 - (len(reqtdetail) - 1)
            rec05 = "# " + reqtdetail + (addspaces * " ") + "*"
            final_recs.append(rec05)
            reqtdetail = ""

#    reqtdetail = "                                                          "           # Uncomment for debugging
#    rec05 = "# " + reqtdetail + "  *"                                                   # Uncomment for debugging
#    final_recs.append(rec05)                                                            # Uncomment for debugging

    rec06 = "#                                                             *"
    final_recs.append(rec06)
    rec07 = "# Computed Result Validated:                                  *"
    final_recs.append(rec07)
    rec08 = "#**************************************************************"
    final_recs.append(rec08)
    rec09 = "#--------------------------------------------------------------"
    final_recs.append(rec09)
    rec10 = "def func_name(user_in):"
    final_recs.append(rec10)
    rec11 = "  return"
    final_recs.append(rec11)
    rec12 = "#--------------------------------------------------------------"
    final_recs.append(rec12)
    rec13 = 'if __name__ == "__main__":'
    final_recs.append(rec13)
    rec14 = '  print("Thank you for using this app.")'
    final_recs.append(rec14)
    rec15 = "#**************************************************************"
    final_recs.append(rec15)

    with open(file_path, "w") as file_handle:
        for item in final_recs:
            print(item)                                                                  # Uncomment for debugging
            print(item, file=file_handle)
    file_handle.close()

if __name__ == "__main__":
    UserPageIn = input("Enter the exercise number & target page(s) - EEE PPP PPP: ")
#    pdf_file_path = "/home/runner/mycommonrepo/projects/module_template/infile_replit/The Python Workbook.pdf"          # Path to your PDF file (Cloud)
    pdf_file_path = "/home/runner/mycommonrepo/projects/module_template/infile_cloud/The Python Workbook.pdf"               # Path to your PDF file (Cloud)
#   pdf_file_path = "/home/pi/Desktop/localrepo/mycommonrepo/projects/module_template/infile_cloud/The Python Workbook.pdf"  # Path to your PDF file (Desktop)
    tmp_data = read_pdf(pdf_file_path, UserPageIn)
    format_then_write(tmp_data)
