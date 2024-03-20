import os
import shutil


def chk_copying(path):

    for root, dirs, Files in os.walk(path):
        for files in Files:
            objects = os.path.splitext(files)[0]
            # print(files)
            # print(os.path.splitext(files)[1])
            if os.path.splitext(files)[1] == '.chk':
                print("Current Tacking with {}".format(files))
                dirname = "./temp_chk_2/MPI_" + objects
                if not os.path.isdir(dirname):
                    os.makedirs(dirname)

                source_file = os.path.join(path, files)
                des_file_1 = os.path.join(dirname, 'N.chk')

                shutil.copy(source_file, des_file_1)

                for root, dirs, Files in os.walk('./scripts_MPI'):
                    for files in Files:
                        filename = './scripts_MPI/' + files
                        shutil.copy(filename, dirname)

            else:
                continue

if __name__ == '__main__':
    chk_copying('./gjf')