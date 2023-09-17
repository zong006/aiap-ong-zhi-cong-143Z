# aiap-ong-zhi-cong-143Z
For AISG 2023 technical assessment

## a. NAME AND EMAIL

Ong Zhi Cong, ongzhicong@gmail.com

## b. Overview of the submitted folder and the folder structure.

- aiap-ong-zhi-cong-143z
    - .github
        - workflows
            - manual.yml
    - data
        - cruise_post.db
        - cruise_pre.db
    - src
        - algo.py
        - data_extraction.py
        - data_preprocessing.py
        - main.py
        - __init__.py
    - eda.ipynb
    - README.md
    - requirements.txt
    - run.sh


## c. Instructions for executing the pipeline and modifying any parameters.

## d. Description of logical steps/flow of the pipeline.

1. The raw data consists of two .db files, cruise_pre.db and cruise_post.db.
2. Data extraction from .db files are performed by the script data_extraction.py. This combines the two .db files and gives a single pandas dataframe as an output.
3. The dataframe is then fed into the script data_preprocessing.py, where data preprocessing is done. The data is cleaned and feature engineering is performed. This script outputs the processed dataframe.
4. The processed dataframe is fed into algo.py containing machine learning algorithms which print classification reports for the classification task and outputs the classifier for each algorithm in this script.

## e. Overview of key findings from the EDA conducted in Task 1.

1. Blastoise cruise travels for longer distances, and thus is exepcted to be a longer duration cruise compared to Lapras. In general, people who rate ease of online booking, embarkation/disembarkation time, cabin service, cabin comfort and online check-in with a higher importance tend to go for the Blastoise cruise.
2. The preferences of passengers shift slightly toward luxury tickets as the level of importance of gate location, baggage handling, onboard service as well as the factors mentioned in point 1 (except for embarkation/disembarkation time) rises. For embarkation/disembarkation time, the preference shifts toward deluxe tickets instead.
3. There are equal proportions of people who are satisfied and dissatisfied with wifi, dining and entertainment across various perceived levels of importance of these services, cruise types and ticket types.
4. The proportion of male to female passengers are quite equal.
5. Most passengers book tickets or heard about the company from direct marketing means, via either the company website or through emails.
6. The target variable "Ticket Type" is highly unbalanced, with passengers going for deluxe tickets forming only a small minority of the dataset. We should take care to stratify the train/test sets to ensure that there are sufficient data points for training and evaluating the model on this category.

## f. Describe how the features in the dataset are processed

| Description of Data Pre-processing |
|:--------|
|Convert the information on DOB to age (in years) of the passenger. ~3% of the entries indicate that the passenger is over 122 years old (the oldest human who ever lived survived till 122 years old, anyone older than that likely doesnt exist, so these are erroneous entries). Replace these entries as well as missing values in this column with the mean of the subset of entries in this column that are <122. Effectively, this is equivalent to removing entries that are >122).|
|"Ext_Intcode" identifies every passenger, but in both pre-trip and post-trip datasets, only about 97% of the entries are unique.
We can attribute the ~3% non-uniqueness to errors in data entry, and drop this column.|
|Convert all the entries in columns whose ratings are on the scale 1 to 5 in the pre-trip survey, 1 being "Not at all important" and 5 being "Extremely important", with the string format into their corresponding numerical values based on the scale. Fill the missing entries with their respective medians.|
|Since "Logging" just shows when a passenger's information was logged, it is safe to drop this piece of information.|
|One-hot encode "Gender" and "Source of Traffic".|
|Map ticket types to numerical values.|
|Clean up cruise names into either of these two categories: blastoise or lapras. One-hot encode "Cruise Name", since it is a nominal categorical.|
|There are cruise distance entries with miles and km. Convert all units to km, and leave only the numerical value. Also, ~6% of the data for cruise distance are negative values. Treat them as errors, and replace with the mean of the respective cruise types (after excluding all negative values).
 Do the same for missing values.|
|As for missing values for "Cruise Distance" that also have missing values for "Cruise Type", we can treat missing cruise types as a 3rd cruise category and fill these missing distances with the mean of this new category.|
|One-hot encode the column "Cruise Name" and relabel missing values as 0. Then proceed to fill in the remaining missing values for "Cruise Distance" (these also have missing "Cruise Name") as mentioned.|
|To fill in the missing values in the target variable, we use the mode of each cruise type. Again there will be missing data for ticket types with missing cruise type data. Treat those with missing cruise names as a 3rd cruise type, and use the mode of this to fill missing ticket type data with cruise type also missing.|
|Replace missing values for "WiFi" and "Entertainment" with 2, and one-hot encode these and "Dining". These are ordinal categorical variables, with ~40% missing data for both "WiFi" and "Entertainment". We cannot simply drop the missing data, nor input missing entries with a number other than 1 or 0 due to its ordinality. The next best option will be to one-hot encode them.

## g. Explanation of your choice of models for each machine learning task.

Three machine learning algorithms are chosen and implemented in algo.py: support vector machine, logistic regression, and decision tree.

1. SVM: SVM (linear kernel) performs well in high-dimensional spaces with easy to interpret hyperplanes to interpret the relative importance of features. It is also robust to the distribution of the data. Though it performs well, it is computationally expensive.
2. Logistic regression: It is computationally efficiency and reliability. At the same time, it is also a simple and interpretable model, where its coefficients give an intuitive understanding of the relative importance of features. Specify a "sag" solver with penalty "L2" for a faster convergence.
3. Decision Tree: Decision tree allows for an easy gauge of the relative importance of the features. It also has no assumptions about the distributions of the data. It also does not require feature scaling.

## h. Evaluation of the models developed.

From EDA, we know there this is a dataset where the target variable "Ticket Type" has unbalanced classes, where only a minority of passengers purchased a deluxe ticket. A more appropriate metric in this context will be the F1 score, since it gives equal weight to both precision and recall, making it sensitive to the minority class.
Furthermore, in the event that this company derives a greater proportion of its profits from deluxe tickets, a good F1 score for deluxe tickets will then allow the company to more effectively target potential customers who tend to purchase these tickets.

Examining the top (positive) coefficients of the logistic regression model, we see that the top features (ignoring features that reference missing data) that impacting the predictive outcomes for deluxe tickets are, in order: age, social media marketing, perception of the importance of onboard entertainment, and direct email marketing. From EDA, social media marketing takes up the smallest percentage (<10%) of the company's marketing efforts, while email marketing stands at ~40%. To increase the likelihood of people purchasing deluxe tickets, the company can put more effort into their social media marketing campaign.
For the other two ticket types (luxury and standard) which forms the majority of ticket sales however, actual satisfaction with the onboard wifi are one of the top features impacting ticket sales. Satisfaction with wifi service is at a higher importance in luxury tickets compared to standard ones. To entice more people to purchase luxury tickets instead of standard, the company can do more to improve the onboard wifi service, since people who perceived wifi service to be more important also tend to go more for luxury tickets.

## i. Other considerations for deploying the models developed.



