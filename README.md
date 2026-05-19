# 🍔 Food Delivery Pattern Analysis using Data Mining & BERT

<div align="center">

# 🚀 Data Mining Project
### Association Rules • Graph Analysis • BERT • Recommendation System

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/Pandas-150458?style=for-the-badge&logo=pandas&logoColor=white)
![NumPy](https://img.shields.io/badge/NumPy-013243?style=for-the-badge&logo=numpy&logoColor=white)
![Machine Learning](https://img.shields.io/badge/Machine-Learning-orange?style=for-the-badge)
![BERT](https://img.shields.io/badge/BERT-NLP-blueviolet?style=for-the-badge)
![NetworkX](https://img.shields.io/badge/NetworkX-000000?style=for-the-badge)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)

---

### 📊 Exploring Customer Ordering Behavior Using:
✨ Association Rule Mining  
✨ Graph-Based Analysis  
✨ Deep Learning (BERT)  
✨ Recommendation Systems  

</div>

---

# 📌 Project Overview

This project focuses on analyzing customer food ordering behavior using advanced Data Mining and Machine Learning techniques.

The project combines:
- Web Mining
- Association Rule Mining
- Link Analysis
- Deep Learning
- Recommendation Systems

The main goal is to extract meaningful insights from food delivery data and customer reviews in order to improve customer experience and generate intelligent meal recommendations.

This project simulates real-world food delivery platforms such as:
- Talabat
- Uber Eats
- Deliveroo

---

# 🎯 Project Objectives

The main objectives of this project are:

✔ Discover frequent meal combinations ordered together  
✔ Analyze customer ordering patterns  
✔ Rank popular meals using PageRank algorithm  
✔ Perform sentiment analysis using BERT  
✔ Build an intelligent recommendation system  
✔ Visualize customer behavior and network relationships  
✔ Generate insights for decision making  

---

# 🧠 Techniques & Algorithms Used

| Technique | Purpose |
|---|---|
| Apriori Algorithm | Discover frequent itemsets |
| FP-Growth | Generate association rules |
| PageRank | Rank popular meals |
| Graph Analysis | Analyze meal relationships |
| BERT | Sentiment classification |
| Recommendation System | Suggest meal combinations |

---

# 🛠 Technologies Used

This project was implemented using:

- Python
- Pandas
- NumPy
- Matplotlib
- Seaborn
- NetworkX
- Scikit-learn
- Transformers (BERT)
- mlxtend
- Jupyter Notebook

---

# 📂 Project Structure

```bash
Project Final DM/
│
├── Project__Finall_Data_Mining_ipynb.ipynb
├── app.py
├── food_delivery_pattern_analysis_1000_rows.csv
├── frequent_itemsets.csv
├── best_meal_combinations.csv
├── meal_graph_analysis.csv
├── final_recommendations.csv
├── README.md
├── requirements.txt
└── .gitignore
```

---

# 📊 Dataset Description

The dataset contains information related to customer orders from food delivery platforms.

### Dataset Features:
- Meal Names
- Meal Categories
- Customer Ratings
- Customer Reviews
- Order Transactions
- Meal Combinations

Each transaction represents meals ordered together by customers.

The dataset was cleaned and processed before applying data mining algorithms.

---

# 🔍 Project Workflow

# 1️⃣ Data Collection & Preprocessing

The first stage focused on preparing the dataset for analysis.

### Steps:
- Handling missing values
- Removing duplicates
- Cleaning text data
- Formatting transactions
- Preparing graph relationships
- Feature extraction

### Tools Used:
- Pandas
- NumPy

---

# 2️⃣ Association Rule Mining

Association Rule Mining was applied to discover relationships between meals frequently ordered together.

### Algorithms Used:
- Apriori
- FP-Growth

### Purpose:
- Identify popular meal combinations
- Discover customer preferences
- Generate recommendation rules

### Example Rules:
- Burger ➜ Fries
- Pizza ➜ Cola
- Shawarma ➜ Pepsi
- Pasta ➜ Garlic Bread

### Output:
- Frequent Itemsets
- Confidence Scores
- Support Values
- Lift Values

---

# 3️⃣ Graph Analysis using PageRank

A graph network was constructed where:

- Nodes → Meals
- Edges → Meals ordered together

The PageRank algorithm was applied to identify the most influential meals.

### Purpose:
✔ Rank important meals  
✔ Analyze meal relationships  
✔ Detect highly connected food items  

### Graph Analysis Features:
- Meal popularity ranking
- Network connectivity
- Relationship strength
- Customer behavior patterns

---

# 4️⃣ BERT Sentiment Analysis

BERT was used to analyze customer reviews and classify customer sentiment.

### Sentiment Classes:
😊 Positive  
😐 Neutral  
😡 Negative  

### Purpose:
- Analyze customer satisfaction
- Understand customer opinions
- Improve recommendation quality
- Detect customer feedback trends

### Deep Learning Model:
- Pretrained BERT Transformer
- NLP-based sentiment classification

---

# 🤖 Recommendation System

A recommendation system was built based on:
- Association rules
- Popular meal rankings
- Customer ordering behavior
- Graph relationships

### Recommendation Features:
✔ Recommend meals commonly ordered together  
✔ Suggest popular combinations  
✔ Improve customer experience  
✔ Generate personalized meal suggestions  

---

# 📈 Data Visualization

Several visualizations were generated to better understand the dataset and extracted insights.

### Visualizations Included:
- Association Rules Visualization
- Meal Network Graph
- Sentiment Distribution Charts
- Frequent Itemsets Charts
- Meal Ranking Graphs
- Recommendation Results

### Libraries Used:
- Matplotlib
- Seaborn
- NetworkX

---

# 📌 Project Results

The project successfully identified:

✅ Best-selling meals  
✅ Frequent meal combinations  
✅ Customer sentiment trends  
✅ Most influential meals  
✅ Popular ordering behaviors  
✅ Customer preferences  

### Key Insights:
- Customers frequently order fast-food combinations together
- Certain meals dominate the ordering network
- Positive reviews significantly impact meal popularity
- Recommendation systems improve user engagement

---

# 🚀 How to Run the Project

# 1️⃣ Clone the Repository

```bash
git clone https://github.com/your-username/Food-Delivery-Pattern-Analysis.git
```

---

# 2️⃣ Navigate to Project Folder

```bash
cd Food-Delivery-Pattern-Analysis
```

---

# 3️⃣ Install Required Libraries

```bash
pip install -r requirements.txt
```

---

# 4️⃣ Open Jupyter Notebook

```bash
jupyter notebook
```

Open:

```bash
Project__Finall_Data_Mining_ipynb.ipynb
```

---

# 📸 Sample Outputs

The project generates:
- Frequent itemsets tables
- Meal recommendation lists
- Graph visualizations
- Sentiment analysis results
- Ranking charts

---

# 📄 Files Description

| File Name | Description |
|---|---|
| Project__Finall_Data_Mining_ipynb.ipynb | Main notebook |
| app.py | Main application file |
| food_delivery_pattern_analysis_1000_rows.csv | Main dataset |
| frequent_itemsets.csv | Frequent itemsets output |
| best_meal_combinations.csv | Best meal combinations |
| meal_graph_analysis.csv | Graph analysis results |
| final_recommendations.csv | Recommendation outputs |

---

# 🔮 Future Improvements

Future enhancements may include:

✨ Real-time recommendation system  
✨ Deploying as a web application  
✨ Integrating live APIs  
✨ Advanced deep learning recommendation models  
✨ Personalized customer recommendations  
✨ Real-time sentiment tracking  

---


# 👨‍💻 Team Members

<div align="center">

| Name | Role |
|---|---|
| Yasmin Ramadan | Team Leader |
| Omnia Ayman | Team Member |
| Ibrahim Galal | Team Member |
| Youssef Saeed | Team Member |
| Mazen Reda | Team Member |

</div>

---

<div align="center">

# ⭐ Thank You For Visiting Our Project ⭐

### If you like this project, don't forget to star the repository ❤️

</div>
