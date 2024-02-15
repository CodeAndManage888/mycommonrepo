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
