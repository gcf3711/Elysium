import csv,os,json
import pandas as pd
pvd_path = "/bdata2/gcf/tosemr1/Elysium/PVD"

bug_type_cor = {"iou":["underflow","overflow"],
                "ren":["reentrancy"],
                "txo":["transaction origin"],
                "ucr":["unhandled exception"],
                "usi":["suicidal"]}

bugs = list()
head = ["file_name","function","tool","pc","type","opcode"]
for root,dirs,files in os.walk(pvd_path):
    for dir in dirs:
        dir_path = os.path.join(root,dir)
        files = os.listdir(dir_path)
        files.sort()

        for file in files:
            if not file.endswith(".bugs.json"):continue
            file_path = os.path.join(dir_path,file)
            file_name = str(file)[:-10].replace("bugs.json","sol")
            with open(file_path,"r",encoding="utf-8") as f:
                bug_data = json.load(f)
                # print(type(bug_data))
            if len(bug_data) != 0:
                for bug in bug_data:
                    if "opcode" not in bug.keys():bug["opcode"]=""
                    if bug["pc"] =="":continue
                    bug["function"]=""
                    with open(str(file_path)[:-10].replace("bugs.json","sol")+".pc2func.json","r",encoding="utf-8") as f:
                        pc2vec = json.load(f)
                        for con in pc2vec[file_name].keys():
                            for fun in pc2vec[file_name][con].keys():
                                if bug["pc"] in pc2vec[file_name][con][fun]:
                                    bug["function"] = str(fun)
                    if bug["type"] in bug_type_cor[dir]:
                        bugs.append([str(file)[:-10],bug["function"],bug["tool"],bug["pc"],bug["type"],bug["opcode"]])

df = pd.DataFrame(data=bugs,columns=head)
df.to_csv("get_bugs_elysium.csv",index=False)     
                
            