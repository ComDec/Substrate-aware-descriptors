#!/usr/bin/python

import os
import numpy as np
import pandas as pd
import math
import argparse

def modifyFile(path):
    # modify files
    f_new = open(path + '.new', 'w')
    with open(path) as f:
        line = f.readline()
        while line:
            line = line.replace("   ", ' ')
            line = line.replace("  ", ' ')
            f_new.write(line)
            line = f.readline()

def getLog_inf(logfile):
    # get information from .log file
    rawdata = pd.read_csv(logfile, header=None, sep=' ')
    numdata = rawdata.iloc[:, 1].values
    numdata = numdata.tolist()
    nameindex = rawdata.iloc[:, 0].values
    nameindex = nameindex.tolist()
    return numdata, nameindex

def getDir(path, dataful):
    # read .log file
    filelist = os.listdir(path)
    for file in filelist:
        file_path = os.path.join(path, file)
        if os.path.splitext(file_path)[1]=='.log':
            # modifyFile(file_path)
            # file_path_new = file_path + '.new'
            # numdata, nameindex = getLog_inf(file_path_new)
            numdata, nameindex = getLog_inf(file_path)
            dataname = os.path.splitext(file)[0]
            chooseColumn(dataname, numdata, dataful)

    for i in range(len(nameindex)):
        nameindex[i] = nameindex[i].replace('.txt', '')
    dataful.loc[:, 'index'] = nameindex

def chooseColumn(columnName, data, dataful):
    columnDict = {'HOMO': 'EHOMO(a.u.)',
                  'LUMO': 'ELUMO(a.u.)',
                  'dipole': 'Magnitude of molecular dipole moment(a.u.)',
                  'MW': 'Molecular Weight',
                  'Surface': 'Surface Area (Bohr^2)',
                  'Volume': 'Volume (Bohr^3)',
                  'Polar-Surface': 'Polar Surface Area (Angstrom^2)',
                  'Nonpolar-Surface': 'Non-Polar Surface Area (Angstrom^2)',
                  'MPI': 'MPI index (eV)',
                  'Chemical-potential': 'Chemical potential (eV)',
                  'Hardness': 'Hardness (eV)',
                  'Electrophilicity-index': 'Electrophilicity index (eV)',
                  'Nucleophilicity-index': 'Nucleophilicity index (eV)'}
    index = columnDict[columnName]
    dataful.loc[:, index] = data

def getArg():
    parser = argparse.ArgumentParser(description='Script argparse setting')
    parser.add_argument('-c', dest='CDFT', default='./CDFT', help='Path to CDFT folder, default is ./CDFT')
    parser.add_argument('-m', dest='MPI', default='./MPI', help='Path to MPI folder, default is ./MPI')
    parser.add_argument('-o', dest='output', default='./mol_data.csv', help='Path to output file, default is ./mol_data.csv')
    args = parser.parse_args()
    CDFT, MPI, output = args.CDFT, args.MPI, args.output

    return CDFT, MPI, output

def grepInf(path, type='CDFT'):
    if type == 'CDFT':
        log1 = open(path + '/Chemical-potential.log', 'w')
        log2 = open(path + '/Electrophilicity-index.log', 'w')
        log3 = open(path + '/Hardness.log', 'w')
        log4 = open(path + '/Nucleophilicity-index.log', 'w')

        filelist = os.listdir(path)
        for file in filelist:
            file_path = os.path.join(path, file)
            if os.path.splitext(file_path)[1] == '.txt':
                with open(file_path) as f:
                    line = f.readline()
                    while line:
                        if ' Chemical potential:' in line:
                            result1 = (line[53:].strip()).replace('\n', '')
                        elif ' Electrophilicity index:' in line:
                            result2 = (line[49:].strip()).replace('\n', '')
                        elif ' Hardness (=fundamental gap):' in line:
                            result3 = (line[53:].strip()).replace('\n', '')
                        elif ' Nucleophilicity index:' in line:
                            result4 = (line[48:].strip()).replace('\n', '')

                        line = f.readline()

                log1.write(file.replace('CDFT_', '') + ' ' + result1 + '\n')
                log2.write(file.replace('CDFT_', '') + ' ' + result2 + '\n')
                log3.write(file.replace('CDFT_', '') + ' ' + result3 + '\n')
                log4.write(file.replace('CDFT_', '') + ' ' + result4 + '\n')

        log1.close()
        log2.close()
        log3.close()
        log4.close()


    elif type == 'MPI':
        log1 = open(path + '/dipole.log', 'w')
        log2 = open(path + '/HOMO.log', 'w')
        log3 = open(path + '/LUMO.log', 'w')
        log4 = open(path + '/MPI.log', 'w')
        log5 = open(path + '/MW.log', 'w')
        log6 = open(path + '/Nonpolar-Surface.log', 'w')
        log7 = open(path + '/Polar-Surface.log', 'w')
        log8 = open(path + '/Surface.log', 'w')
        log9 = open(path + '/Volume.log', 'w')

        filelist = os.listdir(path)
        for file in filelist:
            file_path = os.path.join(path, file)
            if os.path.splitext(file_path)[1] == '.txt':
                with open(file_path) as f:
                    line = f.readline()
                    while line:
                        if ' Magnitude of molecular dipole moment (a.u.&Debye):' in line:
                            result1 = (line[56:67].strip()).replace('\n', '')
                        elif 'HOMO, energy:' in line:
                            result2 = (line[40:56].strip()).replace('\n', '')
                        elif 'LUMO, energy:' in line:
                            result3 = (line[40:56].strip()).replace('\n', '')
                        elif ' Molecular polarity index (MPI):' in line:
                            result4 = (line[34:42].strip()).replace('\n', '')
                        elif ' Molecule weight:' in line:
                            result5 = (line[23:36].strip()).replace('\n', '')
                        elif ' Nonpolar surface area (|ESP| <= 10 kcal/mol):' in line:
                            result6 = (line[49:68].strip()).replace('\n', '')
                        elif ' Polar surface area (|ESP| > 10 kcal/mol):' in line:
                            result7 = (line[49:68].strip()).replace('\n', '')
                        elif ' Overall surface area:' in line:
                            result8 = (line[30:49].strip()).replace('\n', '')
                        elif ' Volume:' in line:
                            result9 = (line[9:28].strip()).replace('\n', '')

                        line = f.readline()

                log1.write(file + ' ' + result1 + '\n')
                log2.write(file + ' ' + result2 + '\n')
                log3.write(file + ' ' + result3 + '\n')
                log4.write(file + ' ' + result4 + '\n')
                log5.write(file + ' ' + result5 + '\n')
                log6.write(file + ' ' + result6 + '\n')
                log7.write(file + ' ' + result7 + '\n')
                log8.write(file + ' ' + result8 + '\n')
                log9.write(file + ' ' + result9 + '\n')

        log1.close()
        log2.close()
        log3.close()
        log4.close()
        log5.close()
        log6.close()
        log7.close()
        log8.close()
        log9.close()



def main(CDFT, MPI, output):
    """
    main function
    :param CDFT: path of CDFT folder
    :param MPI: path of MPI folder
    :param output: output path
    :return:
    """
    dataFul = pd.DataFrame(columns=['index',
                                    'EHOMO(a.u.)',
                                    'ELUMO(a.u.)',
                                    'Magnitude of molecular dipole moment(a.u.)',
                                    'Molecular Weight',
                                    'Surface Area (Bohr^2)',
                                    'Volume (Bohr^3)',
                                    'Ovality',
                                    'Polar Surface Area (Angstrom^2)',
                                    'Non-Polar Surface Area (Angstrom^2)',
                                    'MPI index (eV)',
                                    'Chemical potential (eV)',
                                    'Hardness (eV)',
                                    'Electrophilicity index (eV)',
                                    'Nucleophilicity index (eV)'])

    getDir(CDFT, dataFul)
    getDir(MPI, dataFul)

    Ovality = dataFul.loc[:, 'Surface Area (Bohr^2)'].values/(4*math.pi*(3*dataFul.loc[:, 'Volume (Bohr^3)'].values/4/math.pi)**(2/3))
    dataFul.loc[:, 'Ovality'] = Ovality.tolist()
    dataFul.to_csv(output, index=False)


CDFT, MPI, output = getArg()
grepInf(CDFT, 'CDFT')
grepInf(MPI, 'MPI')
main(CDFT, MPI, output)
print("complited!")

