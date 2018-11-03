# Asteroids_Nasa

This project aims to classify, based on morphological and physical attributes, the Nasa's monitored asteroids hazardousness. This binary classification project was made in python 3.6.

-------------------------

# Project Structure - Directories

* __Data:__ _datasets_ directory;
* __Scripts:__ _python_ scripts directory;
* __reports:__ _pyplots_, _docs_ and _reports_.

-------------------------

# Python Modules

* __pandas:__ `pip install pandas`;
* __sklearn:__ `pip install sklearn`.

-------------------------

# Sklearn Models

* __Random Forest.__
    * __model arguments:__
        * __n_arguments:__ 100;
        * __rest:__ default.
        
-------------------------

# Results

#### Models Accuracy
1. The Random Forest model assertiveness rate was: 99.89 %.
2. The dumb algorithm assertiveness rate was 18.55 %. - _independent of attributes, the model always infers True_.

#### Confusion Matrix
|                | Hazardous | Not Hazardous|
|----------------|-----------|--------------|
| Hazardous      |      764  |            0 |
| Not Hazardous  |        1  |          173 |

-------------------------
