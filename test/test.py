import aspose.words as aw
import lexnlp.extract.en.distances
def convert(path):
    doc=aw.Document(path)
    newpath=path.replace(".docx",".txt")
    doc.save(newpath)
    return newpath
paths=[r"C:\\Users\\somne\\Programming\\Internship\\data\\amtd-digital-inc_dated-december-19-2019-maoyan-entertainment-and_Filed_20-05-2021_Contract.docx",r"C:\\Users\\somne\\Programming\\Internship\\data\\cboe-global-markets-inc_cboe-global-markets-inc-long-term-incentive-plan_Filed_19-02-2021_Contract.docx",r"C:\\Users\\somne\\Programming\\Internship\\data\\ContractKen_Word_Addin_Testing_ContractDoc_1.docx",r"C:\\Users\\somne\\Programming\\Internship\\data\\ContractKen_Word_Addin_Testing_ContractDoc_2.docx","C:\\Users\\somne\\Programming\\Internship\\data\\ContractKen_Word_Addin_Testing_ContractDoc_2.txt","C:\\Users\\somne\\Programming\\Internship\\data\\ISDA-Example.docx"]
datapath=[]
for path in paths:
    datapath.append(convert(path))
def getText(path):
    text=""
    with open(path,encoding="utf8") as file:
        for line in file:
            text+=line
    return text

for path in datapath:
    text=getText(path)
    print(list(lexnlp.extract.en.amounts.get_amounts(text)))
    print("\\n\\n\\n\\n\\ ")
