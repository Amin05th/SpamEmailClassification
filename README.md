# SpamEmailClassification: Project Overview
- Created a tool that classifies spamemails to help people recognize them
- Downloaded Dataset from archive.ics.uci.edu
- Optimized LogisticRegression, GaussianNB, MultinomialNB, BernoulliNB, IsolationForest using GridSearchCV
- Built a client facing API using flask

## Code and Resources Used

**Python Version**: 3.10
**Packages:** pandas, numpy, sklearn, matplotlib, seaborn, sqlite3, flask, flask_restx, flask_sqlalchemy
** Dataset: ** [https://archive.ics.uci.edu/ml/datasets/spambase](https://archive.ics.uci.edu/ml/datasets/spambase)

## Dataset

With each sample following features were delivered:

- word_freq_make
- word_freq_address
- word_freq_all
- word_freq_3d
- word_freq_our
- word_freq_over
- word_freq_remove
- word_freq_make
- word_freq_address
- word_freq_all
- word_freq_3d
- word_freq_our
- word_freq_over
- word_freq_remove
- word_freq_internet
- word_freq_order
- word_freq_mail
- word_freq_receive
- word_freq_will
- word_freq_people
- word_freq_report
- word_freq_addresses
- word_freq_free
- word_freq_business
- word_freq_email
- word_freq_you
- word_freq_credit
- word_freq_your
- word_freq_font
- word_freq_000
- word_freq_money
- word_freq_hp
- word_freq_hpl
- word_freq_george
- word_freq_650
- word_freq_lab
- word_freq_labs
- word_freq_telnet
- word_freq_857
- word_freq_data
- word_freq_415
- word_freq_85
- word_freq_technology
- word_freq_1999
- word_freq_parts
- word_freq_pm
- word_freq_direct
- word_freq_cs
- word_freq_meeting
- word_freq_original
- word_freq_project
- word_freq_re
- word_freq_edu
- word_freq_table
- word_freq_conference

## EDA

I looked at the distributions of the data and the value counts for the various categorical variables.

## Model Building

First, I transformed the categorical variables into dummy variables. I also split the data into train and tests sets with a test size of 20%.

I tried 5 different Models and evaluated accuracy, recall, precision, r2. I tried every metric to see which one performs best.

This are the following Models:

- ** LogisticRegression: ** Becouse thought weighted class will perform good
- ** GaussianNB: ** Tried it out
- ** MultinomialNB: ** Tried it out
- ** BernoulliNB: ** Tried it out
- ** IsolationForest: ** Tried it out

## Productionization

In this step, I built a flask API endpoint that was hosted on a local webserver by following along with the TDS tutorial in the reference section above. The Api endpoint takes in a request with a list of values from a email list and returns if it is a spam email or not.
