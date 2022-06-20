import lexnlp.extract.en.entities.nltk_re
def getText(path):
    text=""
    with open(path,encoding="utf8") as file:
        for line in file:
            text+=line
    return text
path=r"C:\\Users\\somne\\Programming\\Internship\\data\\amtd-digital-inc_dated-december-19-2019-maoyan-entertainment-and_Filed_20-05-2021_Contract.docx"
print(list(lexnlp.extract.en.entities.nltk_re.get_entities.nltk_re.get_companies(text1)))
