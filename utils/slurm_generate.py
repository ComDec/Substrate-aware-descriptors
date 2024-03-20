import os

def slurm_create(workname):
    filename = './gjf/' + workname
    with open (filename, "w+") as f:
        f.write('#!/bin/bash\n')
        line1 = '#SBATCH -J ' + os.path.splitext(workname)[0]
        f.write(line1)
        f.write('\n')
        f.write('#SBATCH -p cpu\n#SBATCH -o %j.out \n#SBATCH -e %j.err \n#SBATCH -N 1 \n#SBATCH '
                '--cpus-per-task=20 \n#SBATCH --exclusive \n')
        f.write('\n'*2)
        line2 = 'CASE=\"'+ os.path.splitext(workname)[0] + '\"'
        f.write(line2)
        f.write('\n'*2)
        f.write('EXE="/lustre/home/acct-ccezwb/ccezwb/gaussian/g09/g09" \n$EXE $CASE.gjf $CASE.out')

def generate(path):
    slurms = []
    for root, dirs, files in os.walk(path):
        for file in files:
            if os.path.splitext(file)[1] == '.gjf':
                filename = os.path.splitext(file)[0] + '.slurm'
                print("Generate {}.slurm".format(os.path.splitext(file)[0]))
                slurm_create(filename)
                slurms.append(filename)
    with open('./gjf/batch_slurm.sh', 'w+') as f:
        for i in range(0, len(slurms)):
            f.write("sbatch " + slurms[i])
            f.write('\n')

if __name__ == "__main__":
    generate('./gjf')