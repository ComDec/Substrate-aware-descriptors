#!/bin/bash

#SBATCH -J A
#SBATCH -p cpu
#SBATCH -o %j.out
#SBATCH -e %j.err
#SBATCH -N 1
#SBATCH --cpus-per-task=40
#SBATCH --exclusive



CASE="N"
EXE="/lustre/home/acct-ccezwb/ccezwb/gaussian/g09/g09"

$EXE $CASE.gjf $CASE.out

CASE="N+1"
EXE="/lustre/home/acct-ccezwb/ccezwb/gaussian/g09/g09"

$EXE $CASE.gjf $CASE.out

CASE="N-1"
EXE="/lustre/home/acct-ccezwb/ccezwb/gaussian/g09/g09"

$EXE $CASE.gjf $CASE.out
