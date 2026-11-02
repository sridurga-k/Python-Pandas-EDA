# 📱 Smartphone Market Exploratory Data Analysis (EDA)

An end-to-end exploratory data analysis of modern smartphones using **Python**, **Pandas**, and **Seaborn**. This project uncovers pricing trends, hardware specifications, brand market share, and performance correlations across thousands of mobile devices.

---

## 📊 Dataset Overview
- **File:** `smartphones_cleaned_v6.csv`
- **Features Analyzed:** Price, Rating, RAM capacity, Battery capacity, 5G availability, Processor speed, and Brand name.

---

## 🔍 Key Questions Explored
1. **Pricing Structure:** How are smartphone prices distributed across different market segments?
2. **Performance vs. Cost:** How strongly do RAM and processor speed correlate with device pricing and overall rating?
3. **Connectivity Trends:** How prevalent is 5G across various pricing tiers?
4. **Brand Dominance:** Which manufacturers offer the highest volume of device variants?
5. **Battery Capacities:** How do battery sizes vary across different operating systems?

---

## 📈 Key Visualizations & Findings
The analysis generates a 6-panel visualization grid (`smartphone_eda_visualizations.png`) highlighting:
- **Right-Skewed Pricing:** The vast majority of smartphones cluster in the budget-to-mid range (< ₹50,000), with a long tail stretching into luxury flagship territory.
- **5G Adoption:** Modern 5G capabilities are standard in mid-to-high tiers, while budget phones occasionally lack 5G support.
- **RAM Impact:** RAM capacity shows a strong positive correlation ($r = 0.76$) with device ratings, highlighting memory as a primary indicator of device performance and class.

---

## 🛠️ How to Run Locally

1. Clone this repository:
   ```bash
   git clone [https://github.com/your-username/smartphone-eda.git](https://github.com/your-username/smartphone-eda.git)
