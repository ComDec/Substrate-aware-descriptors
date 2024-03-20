import os

def submit_jobs(path):
    for root, dirs, Files in os.walk(path):
        for subdir in dirs:
            print('submit in {}'.format(subdir))
            dirname = os.path.join(path, subdir)
            os.system("cd " + dirname)
            os.system("sbatch run_hpc.slurm")
            os.system("cd ..")
            os.system("cd ..")

if __name__ == "__main__":
    submit_jobs('./temp_chk')