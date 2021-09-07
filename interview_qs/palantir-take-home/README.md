# Palantir Data Engineer Challenge

## Introduction

### Purpose

The purpose of this challenge is to demonstrate my analytic and creative skillset to Palantir.
The challenge will be completed using a Jupyter Notebook and population data about the UK from 2013-2016.

### Technologies

- *Python: 3.8.10*
- *PySpark: 3.1.2*
- *Pandas 1.3.2* 
- *Seaborn: 0.11.2*
- *Jupyter: 1.0.0*

## Contents and Design

### Contents

- **population_estimates.ipynb** - Jupyter Notebook containing analytics on raw data in the **Local-Data** folder


- **Local-Data** - contains raw data and metadata files on population data about the UK from 2013-2016

### Design

- **Tech**: 
  - PySpark was used to read the raw data into a dataframe. This allowed me to
    work with PySpark's extremely powerful dataset API which combines the strengths
    of RDD's (strong typing, and powerful lambdas), with Spark SQL's execution engine.

  - Seaborn was used instead of the typical matplotlib/pandas combination because it is simpler to work with, and
    it's also a fun library that has a lot of potential. :)

  - The project was done with Jupyter Notebooks as a means of clearly communicating my results at an appropriate level
    of detail. This would hopefully make it easier to convince non-experts that my narrative is
    reliable and correct.


- **Layout**:
  - There are 10 cells, each with a comment header describing the purpose of the cell
  - There are Question and Description headers
  - Question
    - These will be directly answered in the comment, or as a result from the dataframe show()
      function after the cell is run
  - Description
    - These give a brief summary of the transformations being made on the dataframe
  - Comments are used to give a brief explanation of the result of a dataframe function chain.
    This is so non-experts can more clearly understand how the data is being transformed


## Setup

### Note

Please run in a linux environment such as Ubuntu 18.04 or 20.04. 
This would closely match my development environment (WSL 2).

### Instructions

1. Run `pip3 install pyspark, pandas, seaborn, jupyter`
2. Run `jupyter-notebook <palantir-take-home>` where <palantir-take-home> is the project directory containing the Jupyter Notebook
3. Visit `localhost:8888` and click on `population_estimates.ipynb` to view population estimates analysis.
4. Run each cell, in order from top to bottom, to see the analysis results