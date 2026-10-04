<div align="center">

# 📊 Pandas Analyzer & Data Visualization

### 🚀 A beginner-friendly Python project for exploring, analyzing, and visualizing sales data

<img src="https://readme-typing-svg.demolab.com?font=Fira+Code&size=22&pause=1000&center=true&vCenter=true&width=700&lines=Analyze+Sales+Data+with+Python;Explore+Data+with+Pandas;Create+Charts+with+Matplotlib+%26+Seaborn;Turn+Raw+Data+into+Meaningful+Insights!" alt="Typing animation" />

<br/>

<img src="https://img.shields.io/badge/Python-3.x-3776AB?style=for-the-badge&logo=python&logoColor=white" />
<img src="https://img.shields.io/badge/Pandas-Data%20Analysis-150458?style=for-the-badge&logo=pandas&logoColor=white" />
<img src="https://img.shields.io/badge/Matplotlib-Visualization-11557C?style=for-the-badge" />
<img src="https://img.shields.io/badge/Seaborn-Visualization-4C72B0?style=for-the-badge" />

<br/><br/>

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=120&section=footer" alt="Animated wave" />

</div>

---

## 🌟 About the Project

**Pandas Analyzer & Data Visualization** is a Python-based sales data analysis project built to practice practical data-analysis concepts.

The project takes a CSV sales dataset and provides a simple menu-driven program to:

- 📂 Load a dataset
- 🔎 Explore rows, columns and data information
- 🧮 Perform DataFrame operations
- 🧹 Handle missing values
- 📋 Generate descriptive statistics
- 📊 Create different visualizations
- 💾 Save generated charts as PNG files

> **Raw Data → Analysis → Visualization → Insights**

---

## 🎬 Demo Video

🎥 **Full project demonstration:**

**🔗 [Add your Google Drive demo video link here](YOUR_GOOGLE_DRIVE_VIDEO_LINK_HERE)**

The demo can show dataset loading, exploration, statistics, chart generation and saving visualizations.

---

## ✨ Features

| Feature | Description |
|---|---|
| 📂 Dataset Loading | Load CSV files using Pandas |
| 🔎 Data Exploration | View rows, columns and basic information |
| 🧮 DataFrame Operations | Perform common Pandas operations |
| 🧹 Missing Data | Detect and handle missing values |
| 📋 Descriptive Statistics | Generate count, mean, std, quartiles and max |
| 📊 Bar Chart | Compare values across categories |
| 📈 Line Chart | Show changes and trends |
| 🔵 Scatter Plot | Analyze relationships between numerical columns |
| 🥧 Pie Chart | Show category-wise sales distribution |
| 📊 Histogram | Understand sales distribution |
| 🏗️ Stack Plot | Compare cumulative values |
| 💾 Save Visualization | Export charts as PNG files |

---

## 🛠️ Tech Stack

```text
Python
├── Pandas       → Data loading & analysis
├── Matplotlib   → Data visualization
└── Seaborn      → Statistical visualization
```

---

## 📁 Project Structure

```text
Pandas-Analyzer-Data-Visualization/
│
├── 📂 data/
│   └── sales_data.csv
│
├── 📂 output/
│   ├── sales_bar_chart.png
│   ├── sales_line_chart.png
│   ├── profit_vs_sales_scatter.png
│   └── sales_category_pie.png
│
├── 📂 src/
│   ├── 📂 visualizations/
│   │   └── visualization.py
│   │
│   └── analyzer.py
│
├── 📄 README.md
└── 📄 .gitignore
```

---

## 🗃️ Dataset

The dataset contains sales information about products, categories, regions, sales, profit, quantity, discount and dates.

| Column | Meaning |
|---|---|
| `SalesID` | Unique ID for each sales record |
| `Date` | Transaction date |
| `Product` | Product sold |
| `Category` | Product category |
| `Region` | Sales region |
| `Sales` | Sales amount |
| `Profit` | Profit generated |
| `Quantity` | Quantity sold |
| `Discount` | Discount applied |
| `Year` | Transaction year |
| `Month` | Transaction month |

---

# 📊 Visualizations

The project supports **6 visualization types**.

## 1️⃣ Bar Chart

**Purpose:** Compare values between categories.

Example: `Product → Sales`

Questions it can help answer:
- Which product has the highest sales?
- Which product has the lowest sales?
- How do products compare?

**Saved output:** `output/sales_bar_chart.png`

![Sales Bar Chart](output/sales_bar_chart.png)

---

## 2️⃣ Line Chart 📈

**Purpose:** Show changes and trends across records.

Example: `SalesID → Sales`

**Saved output:** `output/sales_line_chart.png`

![Sales Line Chart](output/sales_line_chart.png)

---

## 3️⃣ Scatter Plot 🔵

**Purpose:** Understand the relationship between two numerical variables.

Example: `Sales → Profit`

This helps answer:

> Does higher sales generally result in higher profit?

**Saved output:** `output/profit_vs_sales_scatter.png`

![Profit vs Sales](output/profit_vs_sales_scatter.png)

---

## 4️⃣ Pie Chart 🥧

**Purpose:** Show the proportion of sales across categories.

Example: `Category → Sales`

**Saved output:** `output/sales_category_pie.png`

![Sales Category Pie Chart](output/sales_category_pie.png)

---

## 5️⃣ Histogram 📊

**Purpose:** Understand the distribution of sales values, including concentration, spread and high-value observations.

---

## 6️⃣ Stack Plot 🏗️

**Purpose:** Visualize cumulative values and compare contributions from multiple groups.

---

# 🎞️ Animated Project Preview

For an animated README, add a short GIF at:

```text
assets/project-demo.gif
```

Then add:

```html
<div align="center">
<img src="assets/project-demo.gif" width="850" alt="Animated project demo">
</div>
```

### 💡 Best GIF idea

Record a short 5–10 second sequence:

```text
Run Program
    ↓
Load Dataset
    ↓
Choose Visualization
    ↓
Chart Appears
    ↓
Save Visualization
```

This is more meaningful than adding a random GIF.

---

# 🚀 How to Run

## 1. Clone the repository

```bash
git clone https://github.com/PalAnghan/pandas-analyzer-data-visualization.git
```

## 2. Open the project

```bash
cd pandas-analyzer-data-visualization
```

## 3. Create a virtual environment

```bash
python -m venv .venv
```

### Windows

```bash
.venv\Scripts\activate
```

## 4. Install dependencies

```bash
pip install pandas matplotlib seaborn
```

## 5. Run the project

```bash
python src/analyzer.py
```

---

# 🖥️ How the Program Works

The program provides a menu-driven interface:

```text
========== Data Analysis & Visualization Program ==========

1. Load Dataset
2. Explore Data
3. Perform DataFrame Operations
4. Handle Missing Data
5. Generate Descriptive Statistics
6. Data Visualization
7. Save Visualization
8. Exit
```

### Example Workflow

```text
1️⃣ Load Dataset
       ↓
2️⃣ Explore Data
       ↓
3️⃣ Analyze Data
       ↓
4️⃣ Generate Statistics
       ↓
5️⃣ Create Visualization
       ↓
6️⃣ Save Chart
```

---

# 📋 Descriptive Statistics

The analyzer can generate:

- Count
- Mean
- Standard deviation
- Minimum
- 25th percentile
- Median
- 75th percentile
- Maximum

This gives a quick numerical summary of the dataset.

---

# 🎯 What I Learned

### 🐼 Pandas
- Reading CSV files
- DataFrame operations
- Selecting columns
- Grouping data
- Pivot tables
- Descriptive statistics
- Handling missing data

### 📊 Matplotlib
- Bar charts
- Line charts
- Scatter plots
- Pie charts
- Histograms
- Stack plots
- Titles, labels and legends
- Saving figures

### 🎨 Seaborn
- Statistical visualization
- Distribution visualization
- Cleaner chart styling

### 🧠 Python
- Classes and objects
- Functions
- Conditional statements
- Loops
- Error handling
- Menu-driven programs
- Project organization

---

# 🔮 Future Improvements

- [ ] 📊 Add more advanced visualizations
- [ ] 📅 Add date-based sales analysis
- [ ] 🏆 Add top-selling product analysis
- [ ] 💰 Add profit analysis by region
- [ ] 📈 Add monthly sales trends
- [ ] 🤖 Add basic predictive analysis
- [ ] 🌐 Build a web dashboard
- [ ] 📤 Export analysis reports
- [ ] 🎛️ Add interactive filters
- [ ] 📊 Add interactive Plotly charts

---

# 💡 Data Analysis Workflow

```text
RAW DATA
   ↓
CLEAN DATA
   ↓
EXPLORE DATA
   ↓
ANALYZE DATA
   ↓
VISUALIZE DATA
   ↓
UNDERSTAND INSIGHTS
```

> **Data visualization makes numbers easier to understand and helps turn raw data into useful insights.**

---

# 📌 Project Highlights

⭐ Beginner-friendly Python project  
⭐ Menu-driven data analysis system  
⭐ CSV processing with Pandas  
⭐ Multiple visualization techniques  
⭐ Statistical analysis  
⭐ Chart export functionality  
⭐ Organized project structure  
⭐ Practical hands-on learning project

---

# 👨‍💻 Author

<div align="center">

## **Pal Anghan**

**Python • Data Analysis • AI/ML • Web Development**

[![LinkedIn](https://img.shields.io/badge/LinkedIn-Connect-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white)](YOUR_LINKEDIN_URL_HERE)
[![GitHub](https://img.shields.io/badge/GitHub-Follow-181717?style=for-the-badge&logo=github&logoColor=white)](https://github.com/PalAnghan)

</div>

---

# ⭐ Support

If you found this project useful:

⭐ Star the repository  
🍴 Fork the repository  
💬 Share your feedback

---

<div align="center">

### 🚀 Keep Learning • Keep Building • Keep Growing

<img src="https://capsule-render.vercel.app/api?type=waving&color=gradient&height=100&section=footer" alt="Footer animation" />

</div>
