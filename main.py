# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import mysql.connector
from PyPDF2 import PdfReader
import re

def read_abs_file_content(abs_filepath, keyword):
    reader = PdfReader(abs_filepath)
    for page_num, page in enumerate(reader.pages, start=1):
        content = page.extract_text()
        if keyword in content:
            #print(f"Keyword '{keyword}' found on page {page_num}.")
            #print(content.count("穿衣指数"))
            reader.get_form_text_fields().items()
            
        # if keyword not in content:
            # print(f"Keyword '{keyword}' not found in the content.")
            # print(content)





pattern = re.compile(r'^(?!.*利息).*$')
test_strings = [
    "这是一段正常的文本",
    "这里面包含利息这个词",
    "不含有利息的内容"
]

for s in test_strings:
    if pattern.match(s):
        print(f'"{s}" 匹配成功')
    else:
        print(f'"{s}" 匹配失败')

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # Assuming '/path/to/your/file.txt' is a placeholder for an absolute path
    keyword_to_search = "穿衣指数"
    read_abs_file_content('C:/Users/Catherine/Nutstore/1/Nutstore/Travel/路书/非洲/Egypt/埃及202501/马蜂窝阿斯旺（第一版）.pdf', keyword_to_search)

    print_hi('world! ')
    
    
    

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


