# Substrate-aware-descriptors

This repository contains the data and codes for ''Machine Learning for Reaction Performance Prediction in Allylic Substitution Enhanced by Automatic Extraction of Substrate-Aware Descriptor''.

![fig1](fig1.png)

## Important environment dependency

```shell
pip install rdkit
pip install -U scikit-learn
pip install autogluon
pip install xgboost
```

## Dataset

The data used in the paper are in the **data** folder. Convenient scripts of batching calculations about data cleaning, DFT and so on are available in **tools** folder.

## Quick Start

A running example is given in `demo.ipynb`.