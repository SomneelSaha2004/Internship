import docx2txt as d2txt
def convert(docpath,textpath):
    MY_TEXT = d2txt.process(docpath)
    #print(MY_TEXT)
    with open(textpath, 'w+',encoding="utf-8") as f:
       f.write(MY_TEXT)
docpaths=[r"C:/Users/somne/Programming/Internship/data/amtd-digital-inc_dated-december-19-2019-maoyan-entertainment-and_Filed_20-05-2021_Contract.docx",r"C:/Users/somne/Programming/Internship/data/cboe-global-markets-inc_cboe-global-markets-inc-long-term-incentive-plan_Filed_19-02-2021_Contract.docx",r"C:/Users/somne/Programming/Internship/data/ContractKen_Word_Addin_Testing_ContractDoc_1.docx",r"C:/Users/somne/Programming/Internship/data/ContractKen_Word_Addin_Testing_ContractDoc_2.docx","C:/Users/somne/Programming/Internship/data/ContractKen_Word_Addin_Testing_ContractDoc_2.docx","C:/Users/somne/Programming/Internship/data/ISDA-Example.docx","C:/Users/somne/Programming/Internship/data/intelligent-systems-corp_master-professional-services-agreement-by-and-the_Filed_04-05-2021_Contract.docx"]
textpaths=['C:/Users/somne/Programming/Internship/data/amtd-digital-inc_dated-december-19-2019-maoyan-entertainment-and_Filed_20-05-2021_Contract.txt', 'C:/Users/somne/Programming/Internship/data/cboe-global-markets-inc_cboe-global-markets-inc-long-term-incentive-plan_Filed_19-02-2021_Contract.txt', 'C:/Users/somne/Programming/Internship/data/ContractKen_Word_Addin_Testing_ContractDoc_1.txt', 'C:/Users/somne/Programming/Internship/data/ContractKen_Word_Addin_Testing_ContractDoc_2.txt', 'C:/Users/somne/Programming/Internship/data/ContractKen_Word_Addin_Testing_ContractDoc_2.txt', 'C:/Users/somne/Programming/Internship/data/ISDA-Example.txt', 'C:/Users/somne/Programming/Internship/data/intelligent-systems-corp_master-professional-services-agreement-by-and-the_Filed_04-05-2021_Contract.txt']
for i in range(0,len(docpaths)):
    convert(docpaths[i],textpaths[i])

