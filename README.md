# Kickstarter ML Classifier

## Project Overview
This repository contains a comprehensive machine learning analysis of Kickstarter campaign data to predict project success. The project was developed as part of INSY662 (Business Intelligence and Analytics) at McGill University, focusing on understanding the key factors that contribute to successful Kickstarter campaigns.

## Project Structure
```
kickstarter-ml-classifier/
├── data/                  # Data files
│   ├── Kickstarter.xlsx          # Original Kickstarter dataset (training data)
│   └── kickstarter_grading.xlsx  # Grading dataset (test data)
├── notebook/             # Jupyter notebooks
│   ├── Individual_Project-Yash-Sethi.ipynb    # Main analysis notebook with complete ML pipeline
│   └── Sethi_Yash_Individual_Project_v1.ipynb # Initial exploratory analysis
├── Project Report.pdf    # Final project report with detailed findings
├── Problem Statement.pdf # Project requirements and guidelines
└── README.md            # Project documentation
```

## Project Description

### Objective
The primary goal of this project is to develop a machine learning classifier that can predict whether a Kickstarter campaign will be successful or failed based on various project characteristics and features.

### Key Features Analyzed
- **Project Goals**: Funding targets and their impact on success rates
- **Temporal Features**: Creation, launch, and deadline dates and their timing patterns
- **Categorical Features**: Project categories, countries, currencies
- **Content Features**: Project name length, blurb length, and text characteristics
- **Media Features**: Presence of videos and feature images
- **Campaign Duration**: Time between project creation and launch

### Machine Learning Approach

#### 1. Classification Model
- **Algorithm**: Gradient Boosting Classifier
- **Target Variable**: Binary classification (1 = successful, 0 = failed)
- **Feature Engineering**: 
  - Temporal feature extraction (weekday, month, year from dates)
  - Duration calculations (months between creation and launch)
  - Categorical encoding (one-hot encoding for categories, countries, etc.)
  - Goal conversion to USD for standardization

#### 2. Clustering Model
- **Algorithm**: K-Means Clustering
- **Purpose**: Identify distinct project segments based on characteristics
- **Features**: Numerical features including goal amounts, durations, and media presence

### Data Preprocessing
1. **Data Cleaning**: Removed missing values and forward-looking predictors
2. **Feature Selection**: Eliminated non-informative features (e.g., disable_communication)
3. **Temporal Processing**: Extracted meaningful time-based features
4. **Categorical Encoding**: Applied one-hot encoding for categorical variables
5. **Feature Scaling**: Standardized numerical features for clustering

### Key Findings
- **Goal Amount**: Lower funding goals tend to have higher success rates
- **Timing**: Projects launched on Tuesdays and with deadlines on Thursdays show better performance
- **Categories**: Certain categories (Documentary, Apparel, Video Games) show distinct success patterns
- **Media Presence**: Projects with videos and feature images have higher success rates
- **Geographic Factors**: Projects from certain countries show varying success patterns

## Data Sources
- **Training Data**: `Kickstarter.xlsx` - Contains historical Kickstarter campaign data
- **Test Data**: `kickstarter_grading.xlsx` - Used for model evaluation and grading

## Setup and Installation

### Prerequisites
- Python 3.7+
- Jupyter Notebook or JupyterLab
- Required Python packages (see below)

### Installation Steps
1. Clone this repository:
   ```bash
   git clone https://github.com/yourusername/kickstarter-ml-classifier.git
   cd kickstarter-ml-classifier
   ```

2. Install required dependencies:
   ```bash
   pip install pandas numpy scikit-learn matplotlib seaborn openpyxl
   ```

3. Launch Jupyter Notebook:
   ```bash
   jupyter notebook
   ```

4. Open the main analysis notebook: `notebook/Individual_Project-Yash-Sethi.ipynb`

### Required Dependencies
- **pandas**: Data manipulation and analysis
- **numpy**: Numerical computing
- **scikit-learn**: Machine learning algorithms and utilities
- **matplotlib**: Data visualization
- **seaborn**: Statistical data visualization
- **openpyxl**: Excel file reading/writing

## Usage

### Running the Analysis
1. Ensure the data files are in the `data/` directory
2. Open the main notebook: `Individual_Project-Yash-Sethi.ipynb`
3. Run cells sequentially to:
   - Load and preprocess the data
   - Perform exploratory data analysis
   - Train the classification model
   - Evaluate model performance
   - Apply clustering analysis

### Model Evaluation
The project includes comprehensive model evaluation metrics:
- **Accuracy**: Overall prediction accuracy
- **Precision**: True positive rate among predicted positives
- **Recall**: True positive rate among actual positives
- **F1-Score**: Harmonic mean of precision and recall

## Project Deliverables
- **Classification Model**: Gradient Boosting classifier for success prediction
- **Clustering Analysis**: K-means clustering for project segmentation
- **Feature Importance Analysis**: Identification of key success factors
- **Comprehensive Report**: Detailed findings and recommendations

## Author
**Yash Sethi** - INSY662 Student at McGill University

## Course Information
- **Course**: INSY662 - Business Intelligence and Analytics
- **Institution**: McGill University
- **Project Type**: Individual Project

## License
This project is part of academic coursework at McGill University. Please refer to the course guidelines for usage permissions.

## Acknowledgments
- Kickstarter for providing the dataset
- McGill University for academic guidance
- Course instructors for project supervision
