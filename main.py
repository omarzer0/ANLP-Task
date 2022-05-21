# -*- coding: utf-8 -*-
# encoding declaration in python
# decode("unicode-escape") -->
# importing unicode-literals must be the first thing to import
# from __future__ import unicode_literals

import nltk
import unicodedata as ud
import pandas as pd
from tkinter import *
from tashaphyne.stemming import ArabicLightStemmer
from tashaphyne import arabicstopwords
import string

punc=list(string.punctuation)

text = "!هنالك العديد من الأنواع المتوفرة لنصوص لوريم إيبسوم، ولكن الغالبية تم تعديلها بشكل ما عبر إدخال بعض النوادر أو الكلمات العشوائية إلى النص. إن كنت تريد أن تستخدم نص لوريم إيبسوم ما، عليك أن تتحقق أولاً أن ليس هناك أي كلمات أو عبارات محرجة أو غير لائقة مخبأة في هذا النص. بينما تعمل جميع مولّدات نصوص لوريم إيبسوم على الإنترنت على إعادة تكرار مقاطع من نص لوريم إيبسوم نفسه عدة مرات بما تتطلبه الحاجة، يقوم مولّدنا هذا باستخدام كلمات من قاموس يحوي على أكثر من 200 كلمة لا تينية، مضاف إليها مجموعة من الجمل النموذجية، لتكوين نص لوريم إيبسوم ذو شكل منطقي قريب إلى النص الحقيقي. وبالتالي يكون النص الناتح خالي من التكرار، أو أي كلمات أو عبارات غير لائقة أو ما شابه. وهذا ما يجعله أول مولّد نص لوريم إيبسوم حقيقي على. الإنترنت."


# Tokenize
def tokenize(txt):
    tokens = nltk.word_tokenize(txt)
    return tokens


def stopwordRemoving(tokensText):
    stopWordList = open("stopwords.txt", encoding="utf-8").read().splitlines()
    SWCleanText = []
    for token in tokensText:
        if token not in stopWordList:
            SWCleanText.append(token)
    resultText = ' '.join(SWCleanText)
    return SWCleanText

def punctuationsRemoving(txt):
    result=[]
    for word in txt:
        if word not in punc:
            result.append(word)
    return ''.join(result)

def ISRI_Stemmer(txt):
    st = nltk.ISRIStemmer()
    tokensText = txt.split(' ')
    resultStem = ' '.join([st.stem(w) for w in tokensText])
    return resultStem


def lightStemmer(txt):
    stemCleanText = []
    lightStem = ArabicLightStemmer()

    tokensText = txt.split(' ')
    for token in tokensText:
        stem = lightStem.light_stem(token)
        stemCleanText.append(stem)

    resultText = ' '.join(stemCleanText)
    print(resultText)
    return resultText


def printToFile(textToPrint):
    file = open(file='output.txt', mode='w', encoding="utf-8")
    file.write(textToPrint)


def doAllGUI():
    inputText = inputTextArea.get("1.0", "end-1c")
    print("dsadasd " + inputText)
    tokenizedText = tokenize(inputText)
    print(tokenizedText)
    removedStopText = stopwordRemoving(tokenizedText)
    print(removedStopText)
    removedPunkText = punctuationsRemoving(removedStopText)
    print(removedPunkText)
    stemedText = ISRI_Stemmer(removedPunkText)
    print(stemedText)
    outputTextArea.delete(1.0, 'end')
    outputTextArea.insert(END,stemedText)
    printToFile(stemedText)

# ----------GUI-----------
root = Tk()
root.title('Arabization')
root.geometry('720x480')
root.maxsize(720, 480)
root.minsize(720, 480)

inputTextLabel = Label(root, text="Enter text", font=('verdana', 18, 'bold'))
inputTextLabel.place(x=50, y=70)

inputTextArea = Text(root, width=40, height=5, borderwidth=2, relief=RIDGE)
inputTextArea.place(x=250, y=50)

outTextLabel = Label(root, text="Result", font=('verdana', 18, 'bold'))
outTextLabel.place(x=50, y=170)

outputTextArea = Text(root, width=40, height=5, borderwidth=2, relief=RIDGE)
outputTextArea.place(x=250, y=150)

# tokenize_button = Button(root, text="Tokenize", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'),
#                          cursor="hand2", command=tokenizeGUI)
# tokenize_button.place(x=50, y=420)
#
# stopWords_button = Button(root, text="Remove stop words", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'),
#                           cursor="hand2")
# stopWords_button.place(x=150, y=420)
#
# lightStem_button = Button(root, text="Light-Stem", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'),
#                           cursor="hand2")
# lightStem_button.place(x=350, y=420)
#
# lightStem_button = Button(root, text="Root-Stem", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'),
#                           cursor="hand2")
# lightStem_button.place(x=500, y=420)

doAll = Button(root, text="Do all operations", relief=RIDGE, borderwidth=3, font=('verdana', 10, 'bold'),
               cursor="hand2", command=doAllGUI)
doAll.place(x=300, y=350)

root.mainloop()
