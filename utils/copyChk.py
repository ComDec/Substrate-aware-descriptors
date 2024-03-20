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
                dirname = "./temp_chk/CDFT_" + objects
                if not os.path.isdir(dirname):
                    os.makedirs(dirname)

                source_file = os.path.join(path, files)
                des_file_1 = os.path.join(dirname, 'N.chk')
                des_file_2 = os.path.join(dirname, 'N+1.chk')
                des_file_3 = os.path.join(dirname, 'N-1.chk')

                shutil.copy(source_file, des_file_1)
                shutil.copy(source_file, des_file_2)
                shutil.copy(source_file, des_file_3)

                for root, dirs, files in os.walk('./gjf'):
                    for file in files:
                        # print(file)
                        if os.path.splitext(file)[1] == '.gjf' and os.path.splitext(file)[0] == objects:
                            scr_file = os.path.join('./gjf', file)
                            # print(os.path.join(dirname, file))
                            shutil.copy(scr_file, os.path.join(dirname, file))

                for root, dirs, Files in os.walk('./scripts'):
                    for files in Files:
                        filename = './scripts/' + files
                        shutil.copy(filename, dirname)

            else:
                continue

if __name__ == '__main__':
    chk_copying('./gjf')