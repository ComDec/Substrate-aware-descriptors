#!/bin/bash

for i in *.txt
do
en=`more ${i} | grep 'Molecule weight:'| tail -n 1 | cut -c 24-34`
echo "${i} ${en}" >> MW.log
done

for i in *.txt
do
en=`more ${i} | grep 'HOMO, energy:'| tail -n 1 | cut -c 41-55`
echo "${i} ${en}" >> HOMO.log
done

for i in *.txt
do
en=`more ${i} | grep 'LUMO, energy:'| tail -n 1 | cut -c 41-55`
echo "${i} ${en}" >> LUMO.log
done

for i in *.txt
do
en=`more ${i} | grep 'Magnitude of molecular dipole moment'| tail -n 1 | cut -c 57-66`
echo "${i} ${en}" >> dipole.log
done

for i in *.txt
do
en=`more ${i} | grep 'Volume:'| tail -n 1 | cut -c 10-29`
echo "${i} ${en}" >> Volume.log
done

for i in *.txt
do
en=`more ${i} | grep 'Overall surface area:'| tail -n 1 | cut -c 31-48`
echo "${i} ${en}" >> Surface.log
done

for i in *.txt
do
en=`more ${i} | grep 'Molecular polarity index'| tail -n 1 | cut -c 29-41`
echo "${i} ${en}" >> MPI.log
done

for i in *.txt
do
en=`more ${i} | grep 'Nonpolar surface area'| tail -n 1 | cut -c 50-69`
echo "${i} ${en}" >> Nonpolar-Surface.log
done

for i in *.txt
do
en=`more ${i} | grep 'Polar surface area (|ESP| > 10 kcal/mol)'| tail -n 1 | cut -c 50-69`
echo "${i} ${en}" >> Polar-Surface.log
done









