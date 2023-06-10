import os
import subprocess,time

time_consuming = 0
SCRD_path = "/bdata2/gcf/tosemr1/Elysium/SCRD"

f_c = {"0x0961375ed779Fe16435D5D430Da00A5bAC527e46":"Presale",
"0x0a630de26e5B41eaef08741e74da4018A6C2E14c":"dgame",
"0x169e59a41BA10600Fddd1b0A72921f503b31D96B":"IcoOKOToken",
"0x5027880b5A4C5BBB88D229a334Aa8F31e6e67197":'HDLContract',
"0x53CE47cbe7F2be0AEcD086a70182A98c907D024d":"EasyMineIco",
"0x6459fe2c8d7c26C0011772310D8cA0f570F1D667":"ClassyCoinAirdrop",
"0x6994699c731dd7e389C209201eC51e8aff283bF9":"tokensale",
"0x6A57883B5748Bf3631aC2E0d43BF0D6f6cBCD16b":"LescoinPreSale",
"0x79A198b2355CA2aef695d8a4987582E093911EBb":"SiringClockAuction",
"0x83B2FdC4b90706fbEe7F4aAAfb56356b6DBf25Bd":"XgoldCrowdsale",
"0x87bE69E5C196E0309CDF6957FD7141FDA1DF2B97":"SaleExtendedBCO",
"0x92033Cc5D60dE8fC01e7d4125713e05194989e1e":"HodboCrowdsale",
"0xc7d020d8C92D099B3ADE17321310b4815eF20A90":'AirDrop',
"0xc8986Ecd41Fb420268f1f4285931379357c4142B":"YobCoinCrowdsale",
"0xCB58A0bDdb9c972D1020d3F9e94C3401960A12d8":"Crowdsale",
"0xD113244B9049943D4bc6fEf3048d24EDf92dd788":"Issuer",
"0xE07E687DC4b244D574F37490948C7f4aa921D958":"ApplauseCashCrowdsale"
}

for file in os.listdir(SCRD_path):
    time_start = time.time()
    file_path = os.path.join(SCRD_path,file)
    if not file.endswith(".sol"):continue
    cmd = "python elysium.py -s {0} -c {1}".format(file_path, f_c[str(file)[:-4]])
    try:
        print(cmd)
        subprocess.run(cmd,shell=True,timeout=3600,cwd="/bdata2/gcf/tosemr1/Elysium/elysium")
    except Exception as e:
        with open('exec_elysium_scrd.log', 'a+') as fail_file:
            fail_file.write("ERROR INFO: {0} {1} \n".format(file_path,type(e)))
    time_end = time.time()
    time_consuming += round((time_end - time_start),2)
    with open('exec_elysium_scrd.log', 'a+') as fail_file:
        fail_file.write("TIME CONSUMING INFO: file:{0}, time:{1}\n".format(file_path,round((time_end - time_start),2)))

with open('exec_elysium_scrd.log', 'a+') as fail_file:
    fail_file.write("TIME CONSUMING INFO: AVERAGE {0}\n".format(time_consuming/17))


