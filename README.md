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
- Has missing values = No

#### Attribution

Data comes from this study:

Warwick J Nash, Tracy L Sellers, Simon R Talbot, Andrew J Cawthorn and Wes B Ford (1994)

"The Population Biology of Abalone (_Haliotis_ species) in Tasmania. I. Blacklip Abalone (_H. rubra_) from the North Coast and Islands of Bass Strait",
Sea Fisheries Division, Technical Report No. 48 (ISSN 1034-3288)

(a) Original owners of database:  
Marine Resources Division  
Marine Research Laboratories - Taroona  
Department of Primary Industry and Fisheries, Tasmania  
GPO Box 619F, Hobart, Tasmania 7001, Australia  
(contact: Warwick Nash +61 02 277277, wnash@dpi.tas.gov.au)

(b) Donor of database:  
Sam Waugh (Sam.Waugh@cs.utas.edu.au)  
Department of Computer Science, University of Tasmania  
GPO Box 252C, Hobart, Tasmania 7001, Australia

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

## Aquatic Toxicity (QSAR)

#### Alias (in scorecards): aquatic_toxicity

#### Domain / Industry: Environmental Chemistry / Toxicology

#### Description

This dataset was used to develop quantitative structure-activity relationship (QSAR) models to predict acute aquatic toxicity towards the fish Pimephales promelas (fathead minnow).

This dataset was used to develop quantitative regression QSAR models to predict acute aquatic toxicity towards the fish Pimephales promelas (fathead minnow) on a set of 908 chemicals.

To predict acute aquatic toxicity towards Daphnia Magna, LC50 data, which is the concentration that causes death in 50% of test D. magna over a test duration of 48 hours, was used as model response. The model comprised 8 molecular descriptors: TPSA(Tot) (Molecular properties), SAacc (Molecular properties), H-050 (Atom-centred fragments), MLOGP (Molecular properties), RDCHI (Connectivity indices), GATS1p (2D autocorrelations), nN (Constitutional indices), C-040 (Atom-centred fragments).

Details can be found in the quoted reference:  
M. Cassotti, D. Ballabio, V. Consonni, A. Mauri, I. V. Tetko, R. Todeschini (2014). Prediction of acute aquatic toxicity towards daphnia magna using GA-kNN method, Alternatives to Laboratory Animals (ATLA), 42,31:41; doi: 10.1177/026119291404200106

#### Dataset characteristics

- number of samples = 546
- number of input features = 8
- Has categorical features = No
- Has missing values = No

#### Attribution

Creators:
Davide Ballabio, Matteo Cassotti, viviana Consonni, Roberto Todeschini

Dataset can be found here:
https://archive.ics.uci.edu/dataset/505/qsar+aquatic+toxicity  
UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

---

## Auto MPG

#### Alias (in scorecards): auto_mpg

#### Domain / Industry: Automotive

#### Description

The auto-mpg dataset contains information about various car attributes, such as cylinders, horsepower, and weight, and aims to predict the miles-per-gallon (mpg) fuel efficiency of the cars. The regression task is to use these attributes to accurately predict the mpg, providing insights into the relationships between car characteristics and fuel efficiency.

"The data concerns city-cycle fuel consumption in miles per gallon, to be predicted in terms of 3 multivalued discrete and 5 continuous attributes." (Quinlan, 1993)

This dataset is a slightly modified version of the dataset provided in the StatLib library. In line with the use by Ross Quinlan (1993) in predicting the attribute "mpg", 8 of the original instances were removed because they had unknown values for the "mpg" attribute.

The third factor is the relative average loss payment per insured vehicle year. This value is normalized for all autos within a particular size classification (two-door small, station wagons, sports/speciality, etc...), and represents the average loss per car per year.

#### Dataset characteristics

- number of samples = 398
- number of input features = 7
- Has categorical features = Yes
- Has missing values = Yes

#### Attribution

Creators:  
R. Quinlan

Past Usage:  
Quinlan,R. (1993). Combining Instance-Based and Model-Based Learning. In Proceedings on the Tenth International Conference of Machine Learning, 236-243, University of Massachusetts, Amherst. Morgan Kaufmann.

Dataset can be found here:
https://archive.ics.uci.edu/dataset/9/auto+mpg  
UCI Machine Learning Repository [http://archive.ics.uci.edu/ml]. Irvine, CA: University of California, School of Information and Computer Science.

---

## Billboard Spotify Audio Features

#### Alias (in scorecards): billboard_spotify

#### Domain / Industry: Music / Entertainment

#### Description

This dataset represents a comprehensive collection of audio features for songs that made their mark on various Billboard charts spanning the years 1961 through 2022. The songs were extracted from the following Billboard charts:

- Hot Country Songs
- Hot Rock & Alternative Songs
- Hot R&B/Hip-Hop Songs
- Hot Dance/Electronic Songs
- Hot Latin Songs
- Smooth Jazz Songs

For each song listed on these charts, the corresponding audio features were sourced from the Spotify API. There were instances where certain songs from the Billboard charts could not be matched with their counterparts on Spotify. Such mismatches could be attributed to variations in song names or other discrepancies.

#### Dataset characteristics

- number of samples = 8,930
- number of input features = 13
- Has categorical features = Yes
- Has missing values = No

#### Attribution

Song data is sourced from the Spotify API. The Billboard charts (list of songs) are sourced from the Billboard website.

---

## Cancer Mortality

#### Alias (in scorecards): cancer_mortality

#### Domain / Industry: Medical / Healthcare Research

#### Description

This dataset, aggregated from sources like the American Community Survey, clinicaltrials.gov, and cancer.gov, is designed for regression tasks to predict cancer mortality rates in US counties from 2010 to 2016. It incorporates 2013 census data, including county-level features such as population, income, households, and other demographic attributes.

#### Dataset characteristics

- number of samples = 3,047
- number of input features = 31
- Has categorical features = No
- Has missing values = Yes

#### Attribution

Dataset created by Noah Rippner. It can be found here:
https://data.world/nrippner/ols-regression-challenge

---

## College Pell Grants

#### Alias (in scorecards): college_pell_grants

#### Domain / Industry: Education

#### Description

This dataset belongs to the modified version for the automl benchmark on `openml.org`. Regroups information for about 7800 different US colleges. Including geographical information, stats about the population attending and post graduation career earnings. Dataset is used to predict the percent of students with Pell Grants given various attributes regarding the college and its student population.

#### Dataset characteristics

- number of samples = 7,062
- number of input features = 42
- Has categorical features = Yes
- Has missing values = Yes

#### Attribution

Dataset source: Pieter Gijsbers. It can be found here:
https://www.openml.org/search?type=data&sort=runs&id=42727&status=active

---

## Computer Activity

#### Alias (in scorecards): computer_activity

#### Domain / Industry: Technology / Computer Science

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

## Fluid Pressure

#### Alias (in scorecards): fluid_pressure

#### Domain / Industry: Mechanical Engineering / Fluid Dynamics

#### Description

This synthetic dataset encapsulates a regression problem rooted in fluid dynamics principles, specifically Bernoulli's equation for fluid flow. Each sample in the dataset carries a unique identifier, a set of fluid properties, and a target pressure value.

The fluid properties encompass:

- Fluid density, which represents the mass of the fluid per unit volume.
- Fluid velocity, indicating the speed at which the fluid is flowing.
- Height, representing the elevation or depth at which the pressure is measured.
- A categorical feature named 'body', denoting the celestial body, like Earth, Mars, or Jupiter. This abstractly signifies the gravitational acceleration affecting the fluid.

The target value for each sample is the pressure, computed based on Bernoulli's equation. The equation accounts for kinetic energy, potential energy due to gravity, and a constant term to determine the fluid's pressure.

$$P=constant-\frac{1}{2}\rho v^2 - \rho gh$$

Where:

- P is the pressure
- $\rho$ is the fluid density
- $v$ is the fluid velocity
- $g$ is the gravitational acceleration
- $h$ is the height

To introduce complexity and simulate real-world imperfections, the dataset contains missing values. Approximately 5% of the data points across the features might be absent. This necessitates handling or imputation techniques, especially crucial for algorithms that cannot inherently manage missing data.

This dataset can be used for a regression task where the objective is to estimate fluid pressure given a set of fluid properties and conditions. The inherent physical relationships, combined with the abstract representation of gravitational forces and the presence of missing values, render it an intricate task for regression models.

#### Dataset characteristics

- number of samples = 2,400
- number of input features = 4
- Has categorical features = Yes
- Has missing values = Yes

#### Attribution

Dataset is synthetically generated by the Ready Tensor team.

---

## House Prices

#### Alias (in scorecards): house_prices

#### Domain / Industry: Housing / Real Estate

#### Description

This is the popular “House prices” dataset (not the same as Boston House Prices or California Housing Dataset). The task is to predict an individual house’s sale price given various attributes related to the property such as lot area, lot frontage, year built, number of bedrooms, bathrooms, etc.

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

## NBA Player Seasons Count

#### Alias (in scorecards): nba_seasons_count

#### Domain / Industry: Sports

#### Description

This dataset contains comprehensive statistics and information related to NBA players, specifically focusing on their performance during their debut season and its relationship to their subsequent career longevity in the NBA.

The dataset is derived from season-average statistics of NBA players. Each row represents a player's performance metrics during their first season in the NBA. These metrics are then used to predict the total number of future seasons a player will compete in the NBA, giving insights into their career longevity.

**Data Filtering and Preprocessing**:

- The dataset has been filtered to include only data from the NBA, excluding other leagues like ABA or BAA.
- Active players, especially those who played in the last five seasons (2018-19 to 2022-23), have been excluded to avoid skewed predictions due to ongoing careers.
- Players who played for multiple teams during their debut season have been removed to maintain consistency in the data.

**Primary Task**:
Using this dataset, the main objective is to predict the number of future seasons a player will play in the NBA based on their debut season's statistics. This prediction task can be approached as a regression problem, where the debut season metrics act as features, and the total seasons played (excluding the debut season) acts as the target variable.

#### Dataset characteristics

- number of samples = 3,261
- number of input features = 29
- Has categorical features = Yes
- Has missing values = Yes

#### Attribution

Original dataset sourced from:  
https://www.basketball-reference.com/

Final dataset created by Ready Tensor team by applying the filtering and preprocessing described above.

---

## NeuralSimReg

#### Alias (in scorecards): neural_sim_reg

#### Domain / Industry: N/A (Synthetic Dataset)

#### Description

This synthetic dataset represents a regression problem, simulating a scenario where data is generated by an unknown real-world process, represented here by a neural network. The dataset contains 10,000 samples. Each sample in the dataset has a unique identifier, a set of 16 features, and a continuous target value.

The features, originally 16-dimensional data points, are generated from a standard normal distribution (mean = 0 and standard deviation = 1). These features can be conceptualized as random inputs fed into a neural network, which simulates our unknown data generation process, producing a target output.

The neural network modeling this process comprises three layers: an input layer of 16 neurons, a first hidden layer of 8 neurons with a ReLU activation, and a second hidden layer of 4 neurons, also with a ReLU activation. The output layer has a single neuron without any activation function, generating a continuous target value for each input sample.

Post this neural network generation, as an additional artifact to mirror real-world complications, approximately 2% of the feature values have been made missing, represented as NaN values. This simulates scenarios where datasets might have gaps or missing entries, not due to the data generation process but as a result of data collection, storage, or other external factors.

The target value for each sample is the output from this neural network given the original 16-dimensional input features, reflecting the true value produced by our simulated data generation process. The central task is a regression problem, aiming to predict this true target value based on the features, even with their missing entries.

The unique challenge posed by this dataset arises from the intricacies introduced by the neural network. With the weights and biases of this neural network initialized randomly from a normal distribution (mean = 0 and standard deviation = 1), the relationship between the input features and the target value is intricate and potentially highly non-linear.

This dataset can be used as a regression challenge where the objective is to predict the output of an intricate, simulated data generation process based on given input features. The non-linear transformations executed by the neural network, combined with high-dimensionality and introduced missing values in the input, amplify the challenge for regression algorithms.

#### Dataset characteristics

- number of samples = 10,000
- number of input features = 16
- Has categorical features = No
- Has missing values = Yes

#### Attribution

Dataset is synthetically generated by the Ready Tensor team.

---

## Sine Waves

#### Alias (in scorecards): sine_waves

#### Domain / Industry: N/A (Synthetic Dataset)

#### Description

This synthetic dataset presents a regression problem based on time steps from a sine wave and a continuous target value. Each sample in the dataset has a unique identifier, a set of time steps (or epochs), and a target value.

The time steps represent sequential observations of a sine function. These observations are continuous values resulting from the sine function, which can range between -1 and 1.

The target value for each sample is the sine value of the point immediately following the last time step. This forms a regression problem, where the task is to predict the next sine value based on the given time steps.

The intervals between the time steps can either be constant for all samples (equidistant intervals) or can vary between samples. When we refer to "varying between samples," it means that the interval length is specific to each sample, but remains constant within that sample. The interval is randomly chosen between (𝜋/8 ) and (𝜋/4 ) for such samples. This introduces variability in the data and poses challenges in capturing the sequential nature of the sine wave.

To add complexity to the dataset, Gaussian noise is added to each observation, perturbing the sine values and making the prediction task more challenging.

Furthermore, approximately 5% of the data points in each time step might be replaced with missing values. This simulates real-world scenarios where sequential data might have gaps or missing entries. Handling these missing values becomes crucial for predictive modeling.

The identifiers for the samples are sequential integers, starting from 0. They are used to uniquely identify each sample in the dataset.

In summary, this dataset presents a regression problem, where the task is to predict the next sine value based on given observations from a sine wave. The known mathematical relationship between the time steps, combined with noise and missing values, makes it a challenging task for regression algorithms.

#### Dataset characteristics

- number of samples = 250
- number of input features = 10
- Has categorical features = No
- Has missing values = Yes

#### Attribution

Dataset is synthetically generated by the Ready Tensor team.

---

## Smoke Test Regression

#### Alias (in scorecards): smoke_test_regression

#### Domain / Industry: N/A (Synthetic Dataset)

#### Description

This synthetically generated dataset is used for smoke testing models in the regression category. The purpose is to verify that the algorithms are functioning correctly and can produce outputs as per the required specifications.

This dataset is generated from a combination of random samples of numbers and colors. Each sample in the dataset comprises:

- **ID**: A unique identifier.
- **Number**: A random value between 0 and 10.
- **Color**: A categorical attribute chosen randomly from the set { 'Red', 'Green', 'Blue' }.

The target value for each sample is derived using the equation:

$$target=a×number+b×number^2 $$

With adjustments:

- An additional 50 is added for samples where the color is 'Green'.
- An added value of 100 for samples with the color 'Blue'.

Dataset is set with $a$ is 1 and $b$ is 2.

Furthermore, the dataset introduces elements of unpredictability:

- Roughly 10% of the samples might lack either the number or color attribute.
- Specifically, the first data entry is guaranteed to have a missing value, either in the number or color column.

In essence, this dataset serves as a smoke test, aiming to assess algorithms' functionality, especially when encountering missing data and intricate non-linear relationships.

#### Dataset characteristics

- number of samples = 200
- number of input features = 2
- Has categorical features = Yes
- Has missing values = Yes

#### Attribution

Dataset is synthetically generated by the Ready Tensor team.
