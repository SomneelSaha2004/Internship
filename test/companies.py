import lexnlp.extract.en.entities.nltk_re
import getText as g
textpaths=['C:/Users/somne/Programming/Internship/data/amtd-digital-inc_dated-december-19-2019-maoyan-entertainment-and_Filed_20-05-2021_Contract.txt', 'C:/Users/somne/Programming/Internship/data/cboe-global-markets-inc_cboe-global-markets-inc-long-term-incentive-plan_Filed_19-02-2021_Contract.txt', 'C:/Users/somne/Programming/Internship/data/ContractKen_Word_Addin_Testing_ContractDoc_1.txt', 'C:/Users/somne/Programming/Internship/data/ContractKen_Word_Addin_Testing_ContractDoc_2.txt', 'C:/Users/somne/Programming/Internship/data/ContractKen_Word_Addin_Testing_ContractDoc_2.txt', 'C:/Users/somne/Programming/Internship/data/ISDA-Example.txt', 'C:/Users/somne/Programming/Internship/data/intelligent-systems-corp_master-professional-services-agreement-by-and-the_Filed_04-05-2021_Contract.txt']
for path in textpaths:
    print(path)
    print(list(lexnlp.extract.en.entities.nltk_re.get_entities.nltk_re.get_companies(g.text(path))))
