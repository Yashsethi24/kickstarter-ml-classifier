## Developing the model ###

# Load Libraries
from sklearn.tree import DecisionTreeClassifier
import pandas

# Import data
kickstarter_df = pandas.read_excel("Kickstarter.xlsx")

# Pre-Processing
kickstarter_df = kickstarter_df.dropna()

# Setup the variables
X = kickstarter_df[["name_len","blurb_len"]]
y = kickstarter_df["state"]

# Split the data
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33, random_state = 5)

# Build the model
decisiontree = DecisionTreeClassifier(max_depth=3)
model = decisiontree.fit(X_train, y_train)

# Using the model to predict the results based on the test dataset
y_test_pred = model.predict(X_test)

# Calculate the mean squared error of the prediction
from sklearn.metrics import accuracy_score
accuracy_score(y_test, y_test_pred)


## Grading ##

# Import Grading Data
kickstarter_grading_df = pandas.read_excel("Kickstarter-Grading.xlsx")

# Pre-Process Grading Data
kickstarter_grading_df = kickstarter_grading_df.dropna()

# Setup the variables
X_grading = kickstarter_grading_df[["name_len","blurb_len"]]
y_grading = kickstarter_grading_df["state"]

# Apply the model previously trained to the grading data
y_grading_pred = model.predict(X_grading)

# Calculate the accuracy score
accuracy_score(y_grading, y_grading_pred)