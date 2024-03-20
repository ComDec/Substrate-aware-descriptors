import os
import pandas as pd

def readSMILES(path):
    df = pd.read_csv(path, encoding='gbk')
    index = df['index'].tolist()
    smiles = df['SMILES'].tolist()
    return index, smiles

def convert(smi, index:list, smiles:list):
    smi_idx = smiles.index(smi)
    smi_idx = index[smi_idx]
    name_1 = smi_idx + ".smi"
    name_2 = smi_idx + ".gjf" + ".old"
    name_3 = smi_idx + ".gjf"
    name_4 = smi_idx + ".chk"
    with open(name_1, 'w+') as f:
        f.write(smi)
    command = "obabel " + name_1 + " -ismi --gen3d -o gjf -xk \"# opt freq m062x def2svp\" > " + name_2
    os.system(command)
    with open(name_2, "r") as f:
        old_line = f.readlines()
    if not os.path.isdir('gjf'):
        os.makedirs('gjf')
    with open("./gjf/" + name_3, "w+") as f:
        f.write("%nprocshared=20\n")
        f.write("%mem=80GB\n")
        f.write("%chk="+name_4+"\n")
        f.write(old_line[0]+"\n")
        f.write('Title Card Required\n')
        f.write("\n")
        for i in range(4, len(old_line)):
            f.write(old_line[i])
        f.write("\n")
    os.system("rm -rf " + name_1)
    os.system("rm -rf " + name_2)
if __name__ == "__main__":

    index, smiles = readSMILES('./test.CSV')
    for smi in smiles:
        convert(smi, index, smiles)