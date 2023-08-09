import docx

def getText(filename):
    doc = docx.Document(filename)
    fullText = []
    for para in doc.paragraphs:
        fullText.append(para.text)
    return '\n'.join(fullText) #form the single string with all the text from the paragraphs

print(getText('C:\\Users\\guilh\\Udemy courses\\1_Automate-Boring-Python\\4_Excel, Word, and PDF\\45. Reading and Editing Word Documents\\demo.docx'))
