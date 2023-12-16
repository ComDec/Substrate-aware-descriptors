#!/bin/bash

for i in *.txt
do
en=`more ${i} | grep 'Chemical potential'| tail -n 1 | cut -c 54-64`
echo "${i} ${en}" >> Chemical-potential.log
done

for i in *.txt
do
en=`more ${i} | grep 'Hardness'| tail -n 1 | cut -c  54-64`
echo "${i} ${en}" >> Hardness.log
done

for i in *.txt
do
en=`more ${i} | grep 'Electrophilicity index'| tail -n 1 | cut -c 48-59`
echo "${i} ${en}" >> Electrophilicity-index.log
done

for i in *.txt
do
en=`more ${i} | grep 'Nucleophilicity index'| tail -n 1 | cut -c 48-59`
echo "${i} ${en}" >> Nucleophilicity-index.log
done

