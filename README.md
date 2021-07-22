## Semantic Reasoning Evaluation Challenge (SemREC) 2021 – Submission for Task1.

Instructions for the project titled “Reasoning Challenges on Gene Variants Data”

The following files are included in the repository.

#### GVA.owl
-	Contains the Sandhi GVA T-Box
#### GVA.nt
-	Contains the GVA.owl + semantic classes for the taxonomy / hierarchies used in Sandhi GVA. 
#### Variants.nt
-	A collection of N-Triples files containing the variant graphs for 10 samples. 
These contain the A-Box for the ontology model defined in GVA.owl. 
#### reasoningapi.py
-	The python module that executes the reasoner for the Variants.nt files
#### requirements.txt
- The required libraries to run the python module.

## Dependencies
- [NumPy - Adds support for large, multi-dimensional arrays, matrices and high-level mathematical functions to operate on these arrays](https://www.numpy.org)
- [python-dateutil - Provides powerful extensions to the standard datetime module](https://dateutil.readthedocs.io/en/stable/index.html)
- [pytz - Brings the Olson tz database into Python which allows accurate and cross platform timezone calculations](https://github.com/stub42/pytz)
- [pandas - A open source data analysis tool](https://github.com/pandas-dev/pandas)

## Getting Started

1) Clone this repository using the following command
    
    ```git clone https://github.com/SWIUser1/SemanticReasoner```

2) Create a virtual environment using the following comamnd
   
    ```python3 -m venv ./venv```
 
3) Install the dependencies using the following command
     
    ``` pip3 install -r requirements.txt ```
    
4) Unzip variants.zip 


5) Run the python file using the following command

    ``` python reasoningapi.py ```
    

    
    
