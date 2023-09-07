# Datasets for Regression Base category on Ready Tensor

This repo contains all files related to the datasets used in algorithm evaluation for the Regression - Base category.

The `datasets` folder contains the main data files and the schema files for all the benchmark datasets under Regression - Base category. Within each dataset folder in `datasets`:

- The `raw` folder contains the original data files from the source (see attributions below).
- `processed` folder contains the processed files. These files are used in algorithm evaluations.
  - The CSV file with suffix "\_train.csv" is used for training
  - "\_test.csv" is used for testing (without the targets)
  - "\_test_key.csv" contains the targets for the test data. This test key file is used to generate scores by comparing with predictions.
  - The JSON file with suffix "\_schema.json" is the schema file for the corresponding dataset.
  - The json file with the suffix "\_infer_req.json" contains a sample JSON object with the data to make an inference request to the /infer endpoint.
  - The CSV file with the dataset name, and no other suffix, is the full data (made of both train and test sets).
- The Jupyter notebook file within each dataset folder is used to convert the raw data file(s) in `raw` folder into the processed form in `processed` folder.
- The folder `schema_cfg` contains a csv which is needed by the schema generation script (described below) .

`schema_gen` folder contains a schema gen config file (YAML) and a python script which are used to generate the JSON schema files stored in the `processed` folder for each dataset. The generated schema file conforms to the Ready Tensor specification for this category.

---

The following is the list of datasets along with a brief description for each and its attribution:

---

## Abalone

#### Alias (in scorecards): abalone

#### Domain / Industry: Biosciences

#### Description

Dataset for predicting the age of abalone from physical measurements. The age of abalone is determined by cutting the shell through the cone, staining it, and counting the number of rings through a microscope -- a boring and time-consuming task. Other measurements, which are easier to obtain, are used to predict the age.

#### Dataset characteristics

- number of samples = 4,177
- number of input features = 8
- Has categorical features = Yes
- Has missing values = Yes

#### Attribution

Data comes from this study:

Warwick J Nash, Tracy L Sellers, Simon R Talbot, Andrew J Cawthorn and Wes B Ford (1994)

"The Population Biology of Abalone (_Haliotis_ species) in Tasmania. I. Blacklip Abalone (_H. rubra_) from the North Coast and Islands of Bass Strait",
Sea Fisheries Division, Technical Report No. 48 (ISSN 1034-3288)

Dataset can be found here:
http://archive.ics.uci.edu/ml/datasets/Abalone

UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

---

## Ailerons

#### Alias (in scorecards): ailerons

#### Domain / Industry: Aerospace

#### Description

This data set addresses a control problem, namely flying a F16 aircraft. The attributes describe the status of the aeroplane, while the goal is to predict the control action on the ailerons of the aircraft.

#### Dataset characteristics

- number of samples = 13,750
- number of input features = 40
- Has categorical features = No
- Has missing values = No

#### Attribution

Data source:
https://www.openml.org/d/296
Author: Luis Torgo","Rui Camacho

---

## Auto Prices

#### Alias (in scorecards): auto_prices

#### Domain / Industry: Automotive

#### Description

This data set consists of three types of entities: (a) the specification of an auto in terms of various characteristics, (b) its assigned insurance risk rating, (c) its normalized losses in use as compared to other cars. The second rating corresponds to the degree to which the auto is more risky than its price indicates. Cars are initially assigned a risk factor symbol associated with its price. Then, if it is more risky (or less), this symbol is adjusted by moving it up (or down) the scale. Actuarians call this process "symboling". A value of +3 indicates that the auto is risky, -3 that it is probably pretty safe.

The third factor is the relative average loss payment per insured vehicle year. This value is normalized for all autos within a particular size classification (two-door small, station wagons, sports/speciality, etc...), and represents the average loss per car per year.

#### Dataset characteristics

- number of samples = 201
- number of input features = 25
- Has categorical features = Yes
- Has missing values = Yes

#### Attribution

Data comes from this study:
Kibler, D., Aha, D.W., & Albert,M. (1989). Instance-based prediction of real-valued attributes. Computational Intelligence, Vol 5, 51--57.

Dataset can be found here:
http://archive.ics.uci.edu/ml/datasets/Automobile
UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

---

## Computer Activity

#### Alias (in scorecards): computer_activity

#### Domain / Industry: Technology

#### Description

The Computer Activity databases are a collection of computer systems activity measures. The data was collected from a Sun Sparcstation 20/712 with 128 Mbytes of memory running in a multi-user university department. Users would typically be doing a large variety of tasks ranging from accessing the internet, editing files or running very cpu-bound programs. The data was collected continuously on two separate occasions. On both occassions, system activity was gathered every 5 seconds. The final dataset is taken from both occasions with equal numbers of observations coming from each collection epoch.

#### Dataset characteristics

- number of samples = 8,192
- number of input features = 21
- Has categorical features = No
- Has missing values = No

#### Attribution

Data can be found here:
https://www.dcc.fc.up.pt/~ltorgo/Regression/DataSets.html

Source:
http://www.cs.toronto.edu/~delve/
Contributed by: Michael Revow

---

## Diamond

#### Alias (in scorecards): diamond

#### Domain / Industry: Precious Metals / Industrial Metals

#### Description

Dataset is based on a case study called "Sarah Gets a Diamond". This case was presented in the first year decision analysis course at Darden School of Business (University of Virginia). The task is to predict the price of a diamond given attributes such as carat weight, cut, color, clarity, polish, symmetry and report (grading agency which reported the qualities of the diamond).

#### Dataset characteristics

- number of samples = 6,000
- number of input features = 7
- Has categorical features = Yes
- Has missing values = No

#### Attribution

This case was prepared by Greg Mills (MBA ’07) under the supervision of Phillip E. Pfeifer, Alumni Research Professor of Business Administration. Copyright (c) 2007 by the University of Virginia Darden School Foundation, Charlottesville, VA.

Dataset can be loaded from the PyCaret library as follows:

```
from pycaret.datasets import get_data
dataset = get_data('diamond')
```

---

## Energy Efficiency

#### Alias (in scorecards): energy_efficiency

#### Domain / Industry: Energy

#### Description

This dataset contains attributes that represent 12 different building shapes simulated in Ecotect. The buildings differ with respect to the glazing area, the glazing area distribution, and the orientation, amongst other parameters. The dataset creators simulated various settings as functions of the afore-mentioned characteristics to obtain 768 building shapes.

The dataset comprises 768 samples and 8 features, aiming to predict two real valued responses. The task is to predict the heating and cooling loads using the 8 features.

#### Dataset characteristics

- number of samples = 768
- number of input features = 8
- Has categorical features = Yes
- Has missing values = No
  This dataset has two targets, namely, “Heating Load” and “Cooling Load”. The variable “Heating Load” is used as the target for this algorithm category. The target choice was arbitrary. The other target variable “Cooling Load“ is dropped from the dataset.

#### Attribution

The dataset was created by Angeliki Xifara (angxifara '@' gmail.com, Civil/Structural Engineer) and was processed by Athanasios Tsanas (tsanasthanasis '@' gmail.com, Oxford Centre for Industrial and Applied Mathematics, University of Oxford, UK).

Dataset can be found here:
https://archive.ics.uci.edu/ml/datasets/energy+efficiency#
UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

---

## Heart Disease

#### Alias (in scorecards): heart_disease

#### Domain / Industry: Healthcare

#### Description

This database contains 76 attributes, but all published experiments refer to using a subset of 14 of them. In particular, the Cleveland database is the only one that has been used by ML researchers to
this date. The "goal" field refers to the presence of heart disease in the patient. It is integer valued from 0 (no presence) to 4. Experiments with the Cleveland database have concentrated on simply attempting to distinguish presence (values 1,2,3,4) from absence (value 0). In this problem category, we treat it as a regression problem to predict the values (1, 2, 3 4).

#### Dataset characteristics

- number of samples = 303
- number of input features = 13
- Has categorical features = No
- Has missing values = No

#### Attribution

Data comes from this study:
Detrano, R., Janosi, A., Steinbrunn, W., Pfisterer, M., Schmid, J., Sandhu, S., Guppy, K., Lee, S., & Froelicher, V. (1989). International application of a new probability algorithm for the diagnosis of coronary artery disease. American Journal of Cardiology, 64,304--310.

Principal investigators responsible for data collection:
Hungarian Institute of Cardiology. Budapest: Andras Janosi, M.D.
University Hospital, Zurich, Switzerland: William Steinbrunn, M.D.
University Hospital, Basel, Switzerland: Matthias Pfisterer, M.D.
V.A. Medical Center, Long Beach and Cleveland Clinic Foundation:Robert Detrano, M.D., Ph.D.

Dataset can be found here:
http://archive.ics.uci.edu/ml/datasets/Heart+Disease
UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

---

## House Prices

#### Alias (in scorecards): house_prices

#### Domain / Industry: Housing / Real Estate

#### Description

This is the popular “House prices” dataset (not the same as Boston House Prices or California Housing Dataset). There are 81 columns and 1,460 samples. The task is to predict an individual house’s sale price given various attributes related to the property such as lot area, lot frontage, year built, number of bedrooms, bathrooms, etc.

#### Dataset characteristics

- number of samples = 1,460
- number of input features = 79
- Has categorical features = Yes
- Has missing values = Yes

#### Attribution

Original source of this data is unknown.
This dataset is available through PyCaret:

```
from pycaret.datasets import get_data
data = get_data('house')
```

---

## Medical Costs

#### Alias (in scorecards): medical_costs

#### Domain / Industry: Insurance

#### Description

This dataset comes from personal medical insurance industry. The task is to use 6 input features to predict the individual medical costs billed by health insurance. Each sample represents an individual. The six predictor features are age, sex, bmi, # of children, smoking status and region in the U.S.

#### Dataset characteristics

- number of samples = 1,338
- number of input features = 6
- Has categorical features = Yes
- Has missing values = No

#### Attribution

The dataset was created by Angeliki Xifara (angxifara '@' gmail.com, Civil/Structural Engineer) and was processed by Athanasios Tsanas (tsanasthanasis '@' gmail.com, Oxford Centre for Industrial and Applied Mathematics, University of Oxford, UK).

Dataset used in paper:
A. Tsanas, A. Xifara: 'Accurate quantitative estimation of energy performance of residential buildings using statistical machine learning tools', Energy and Buildings, Vol. 49, pp. 560-567, 2012

Dataset is available in the pycaret python package. Use:

```
from pycaret.datasets import get_data
insurance = get_data('insurance') # returns pandas dataframe
```

---

## White Wine

#### Alias (in scorecards): white_wine

#### Domain / Industry: Winery / Alcoholic Beverage

#### Description

(White wine and red wine datasets)

The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

#### Dataset characteristics

- number of samples = 4,898
- number of input features = 11
- Has categorical features = No
- Has missing values = No

#### Attribution

Data source:
Paulo Cortez, University of Minho, Guimarães, Portugal, http://www3.dsi.uminho.pt/pcortez
A. Cerdeira, F. Almeida, T. Matos and J. Reis, Viticulture Commission of the Vinho Verde Region(CVRVV), Porto, Portugal @2009

Dataset can be found here:
https://archive.ics.uci.edu/ml/datasets/wine+quality
UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

---
