from docx import Document
import re

doc = Document('./so.docx')
pattern = '\d+'
new_file = open('new_file.docx', 'a')
this_res = set()
for pra in doc.paragraphs:
    res = pra.text
    final_res = re.findall(pattern=pattern, string=res)
    for i in final_res:
        replace = re.sub(pattern=pattern, repl=i[::-1], string=res)
        this_res.add(replace)

for j in this_res:
    print(j)