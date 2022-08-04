def text(path):
    text=""
    with open(path,"r",encoding="utf8") as file:
        for line in file:
            text+=line
    return text