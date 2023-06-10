import os
import subprocess,time
import csv

time_consuming = dict()
pvd_path = "/bdata2/gcf/tosemr1/Elysium/PVD"

pvd_address_path = "/bdata2/gcf/tosemr1/Elysium/PVD_address.csv"
filename_contractname = dict()
with open(pvd_address_path,"r",encoding="utf-8") as f:
    pvd_address = csv.reader(f)
    for line in pvd_address:
        if line[2]!="" and line[1]!="":
            filename_contractname[line[1]] = line[2]
print(filename_contractname)

f_c = {"2018-12025-3":"UselessEthereumToken",
"2018-12230":"RemiCoin",
"BECToken":"BecToken",
"parity_wallet_bug_2":"WalletLibrary",
"WalletLibrary":"WalletLibrary",
"modifier_reentrancy_fixed":"ModifierEntrancy",
"modifier_reentrancy":"ModifierEntrancy",
"spank_chain_payment":"LedgerChannel"
}

for root,dirs,files in os.walk(pvd_path):
    for dir in dirs:
        time_start = time.time()
        dir_path = os.path.join(root,dir)
        files = os.listdir(dir_path)
        files.sort()
        print(files)
        for file in files:
            if not file.endswith(".sol"):continue
            file_path = os.path.join(dir_path,file)
            if str(file)[:-4] in filename_contractname.keys():
                cmd = "python elysium.py -s {0} -c {1}".format(file_path, filename_contractname[str(file)[:-4]])
            elif str(file)[:-4] in f_c.keys():
                cmd = "python elysium.py -s {0} -c {1}".format(file_path, f_c[str(file)[:-4]])
            else:
                cmd = "python elysium.py -s {0}".format(file_path)
            try:
                print(cmd)
                subprocess.run(cmd,shell=True,timeout=3600,cwd="/bdata2/gcf/tosemr1/Elysium/elysium")
            except Exception as e:
                with open('exec_elysium.log', 'a+') as fail_file:
                    fail_file.write("ERROR INFO: {0} {1} \n".format(file_path,type(e)))
        time_end = time.time()
        time_consuming[str(dir)]=round((time_end - time_start),2)
        print("vulnerability:{0}, time:{1}\n".format(dir,round((time_end - time_start),2)))

print(time_consuming)


