import os

def rename(dirname):
    for _, _, files in os.walk(dirname):
        for file in files:
            ori_name = file
            if os.path.splitext(file)[1] == '.txt':
                temp = os.path.splitext(file)[0]
                name = temp.split('_')[1]
                new_name = name+'-CDFT.txt'
                os.rename(ori_name, new_name)

if __name__ == '__main__':
    rename('./')