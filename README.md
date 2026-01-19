# Assignment-1
## Part 1
## Introduction
Topsis which refers to Technique for Order Preference by Similarity to Ideal Solution is a Multi-Criteria Decision Making (MCDM) technique used to rank alternatives based on their distance from an ideal best and an ideal worst solution.

# Methodology
## 1.Decision Matrix
A decision matrix is an input csv with first column as non-numeric(names) while rest are numeric values.
## 2.Normalization
All values are reduced between 0-1 to eliminate effect of different units using formula:
\[
r_{ij} = \frac{x_{ij}}{\sqrt{\sum_{i=1}^{n} x_{ij}^2}}
\]
## 3.Weighted Normalized Matrix
Each normalized value is multiplied by its corresponding weight:

\[
v_{ij} = r_{ij} \times w_j
\]
## 4.Ideal Best and Ideal Worst
- **Ideal Best (A⁺):** Best values of each criterion  
- **Ideal Worst (A⁻):** Worst values of each criterion  

The determination depends on **impacts**:
- `+` → Higher value is better  
- `-` → Lower value is better
  
## 5.Separation Measures
The Euclidean distance of each alternative from the ideal best and ideal worst is calculated:

\[
S_i^+ = \sqrt{\sum (v_{ij} - A_j^+)^2}
\]

\[
S_i^- = \sqrt{\sum (v_{ij} - A_j^-)^2}
\]

## 6.TOPSIS Score
The TOPSIS score (relative closeness) is calculated as:

\[
C_i = \frac{S_i^-}{S_i^+ + S_i^-}
\]

## 7.Ranking of Alternatives 
- Higher score ⇒ Better rank

## 8. Input and output table
<img width="558" height="285" alt="Screenshot 2026-01-18 at 9 03 23 PM" src="https://github.com/user-attachments/assets/21b0c4e6-64e0-45ca-b433-467746939614" />
<img width="571" height="287" alt="Screenshot 2026-01-18 at 9 03 03 PM" src="https://github.com/user-attachments/assets/7397451c-64e6-4a82-980c-8083278a7865" />

# Part 2
<img width="1355" height="683" alt="Screenshot 2026-01-19 at 8 03 19 PM" src="https://github.com/user-attachments/assets/ab5b75e6-bca0-42bd-8a08-7db3f3cf2adc" />

# Part 3
In this project, a **web-based TOPSIS service** is developed using **Flask**, where users can upload a CSV file, provide weights and impacts, and receive the ranked result via email.

## 🌐 Web Service Description

## User Inputs:
- CSV input file
- Weights (comma-separated)
- Impacts (comma-separated)
- Valid Email ID

## Validations:
- Number of weights = number of impacts
- Impacts must be either `+` or `-`
- Email format must be valid
- Criteria values must be numeric

---

## Output
- Result CSV file is generated
- Result file is sent to the provided **email ID**
- File contains TOPSIS score and rank

---

## Technologies Used
- Python
- Flask
- Pandas
- NumPy
- HTML 
- SMTP

## Conclusion
This project successfully demonstrates the implementation of the TOPSIS decision-making technique as a web service.  


<img width="390" height="323" alt="Screenshot 2026-01-18 at 10 27 57 PM" src="https://github.com/user-attachments/assets/e2c64859-5dc2-4b23-891c-6bd02d90879e" />






