# Run Elysium And Get Json File that Can Be Deployed on Truffle

## Run Elysium on PVD
```bash
python -u exec_elysium.py > exe.log 2>&1
```

## Run Elysium on SCRD
```bash
python -u exec_elysium_scrd.py > exe_scrd.log 2>&1
```

## Get Vulnerabilities
Get pc2func file by slither printer
> 9001 /ssd/gcf/tosemr1/eth2vec/slither
```bash
python /ssd/gcf/tosemr1/eth2vec/exec_slither_forelysiumpc2func.py
```
Get vulnerable functions
```bash
python get_bugs_elysium.py
```

## Get Truffle Artifact Files
```bash
python get_truffle_json.py
```

## Get Truffle Deploy Configuration Files
```bash
python get_truffle_files.py
```