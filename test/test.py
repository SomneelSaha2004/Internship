import aspose.words as aw
import lexnlp
import lexnlp.extract.en.dates
import lexnlp.extract.en.money
import lexnlp.extract.en.copyright
import lexnlp.extract.en.geoentities
import lexnlp.extract.en.acts
import lexnlp.extract.en.urls
def convert(path):
    doc=aw.Document(path)
    newpath=path.replace(".docx",".txt")
    doc.save(newpath)
    return newpath
paths=[r"C:\\Users\\somne\\Programming\\Internship\\data\\amtd-digital-inc_dated-december-19-2019-maoyan-entertainment-and_Filed_20-05-2021_Contract.docx",r"C:\\Users\somne\\Programming\\Internship\\data\\cboe-global-markets-inc_cboe-global-markets-inc-long-term-incentive-plan_Filed_19-02-2021_Contract.docx",r"C:\\Users\somne\\Programming\\Internship\\data\\ContractKen_Word_Addin_Testing_ContractDoc_1.docx",r"C:\\Users\somne\\Programming\\Internship\\data\\ContractKen_Word_Addin_Testing_ContractDoc_2.docx"]
datapath=[]
for path in paths:
    datapath.append(convert(path))
def getText(path):
    text=""
    with open(path,encoding="utf8") as file:
        for line in file:
            text+=line
    return text

text1=getText(datapath[0])
text2=getText(datapath[1])
#print(text1)
# f=open("Text1"
print("Contract 1")
print("\nDates\n")
print(list(lexnlp.extract.en.dates.get_dates(text1)))
print("\nMonetary Amounts\n")
print(list(lexnlp.extract.en.money.get_money(text1)))
print("\nCopyrights\n")
print(list(lexnlp.extract.en.copyright.get_copyright(text1)))
print("\nActs\n")
print(lexnlp.extract.en.acts.get_act_list(text1))
print("\nLinks\n")
print(list(lexnlp.extract.en.urls.get_urls(text1)))
print("\n\nContract 2")
print("\nDates\n")
print(list(lexnlp.extract.en.dates.get_dates(text2)))
print("\nMonetary Amounts\n")
print(list(lexnlp.extract.en.money.get_money(text2)))
print("\nCopyrights\n")
print(list(lexnlp.extract.en.copyright.get_copyright(text2)))
print("\nActs\n")
print(lexnlp.extract.en.acts.get_act_list(text2))
print(lexnlp.extract.en.acts.get_act_list(text1))
print("\nLinks\n")