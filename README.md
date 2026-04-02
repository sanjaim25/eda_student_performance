# 📊 Student Performance EDA

A comprehensive Exploratory Data Analysis (EDA) project analyzing student performance across different subjects and demographic factors.

## 📋 Table of Contents
- [Overview](#overview)
- [Dataset](#dataset)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Key Insights](#key-insights)
- [Technologies Used](#technologies-used)
- [Contributing](#contributing)

## 🎯 Overview

This project performs exploratory data analysis on student performance data to uncover patterns and relationships between various factors (gender, parental education, test preparation) and academic achievement in math, reading, and writing.

## 📁 Dataset

The dataset contains 1000 student records with the following features:
- **Gender**: Student's gender (male/female)
- **Race/Ethnicity**: Student's ethnic background (Group A-E)
- **Parental Level of Education**: Highest education level of parents
- **Lunch**: Type of lunch (standard/free or reduced)
- **Test Preparation Course**: Whether student completed test prep (completed/none)
- **Math Score**: Score in mathematics (0-100)
- **Reading Score**: Score in reading (0-100)
- **Writing Score**: Score in writing (0-100)

## ✨ Features

- **Data Cleaning & Preprocessing**: Handle missing values and data types
- **Univariate Analysis**: Distribution of individual variables
- **Correlation Analysis**: Relationships between numeric variables
- **Comparative Analysis**: Performance across different demographic groups
- **Visualizations**: 
  - Histograms for score distributions
  - Correlation heatmaps
  - Box plots for group comparisons
  - Multi-panel visualizations

## 🚀 Installation

### Prerequisites
- Python 3.8 or higher
- pip package manager

### Step 1: Clone the Repository
```bash
git clone https://github.com/yourusername/student-performance-eda.git
cd student-performance-eda
```

### Step 2: Create Virtual Environment (Optional but Recommended)
```bash
# Windows
python -m venv venv
venv\Scripts\activate

# macOS/Linux
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

## 💻 Usage

### Option 1: Jupyter Notebook (Recommended)

1. **Start Jupyter Notebook:**
```bash
jupyter notebook
```

2. **Navigate to the notebook:**
   - Open `notebooks/eda_student_performance.ipynb`
   - Run cells sequentially (Shift + Enter)

### Option 2: Quick Data Preview

Run the main script for a quick data preview:
```bash
python main.py
```

### Option 3: JupyterLab

For a more modern interface:
```bash
jupyter lab
```

## 📂 Project Structure

```
student-performance-eda/
│
├── data/
│   └── StudentsPerformance (3).csv    # Dataset file
│
├── notebooks/
│   └── eda_student_performance.ipynb  # Main analysis notebook
│
├── src/
│   └── utils.py                       # Helper functions
│
├── outputs/
│   ├── plots/                         # Generated visualizations
│   └── reports/                       # Analysis reports
│
├── requirements.txt                   # Python dependencies
├── README.md                          # Project documentation
└── main.py                           # Quick preview script
```

## 🔍 Key Insights

The analysis reveals several important findings:

1. **Test Preparation Impact**: Students who completed test preparation courses show significantly higher scores across all subjects

2. **Parental Education Correlation**: Strong positive correlation between parental education level and student performance

3. **Score Relationships**: High correlation between math, reading, and writing scores (students who excel in one subject tend to excel in others)

4. **Gender Patterns**: Performance differences across subjects by gender

5. **Lunch Program**: Students with standard lunch programs tend to score higher than those with free/reduced lunch

## 🛠️ Technologies Used

- **Python 3.10+**: Core programming language
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization
- **Jupyter**: Interactive notebook environment
- **Scikit-learn**: Machine learning utilities

## 📊 Sample Visualizations

The notebook generates various visualizations including:
- Distribution histograms for all score types
- Correlation heatmap showing relationships between scores
- Box plots comparing performance across demographic groups
- Multi-panel comparative analysis

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📝 License

This project is open source and available under the MIT License.

## 👤 Author

Your Name
- GitHub: [@yourusername](https://github.com/yourusername)
- LinkedIn: [Your Name](https://linkedin.com/in/yourprofile)

## 🙏 Acknowledgments

- Dataset source: [UCI Machine Learning Repository / Kaggle]
- Inspiration from various EDA projects in the data science community

## 📧 Contact

For questions or feedback, please open an issue or contact [your.email@example.com]

---

⭐ If you found this project helpful, please consider giving it a star!
