# Assignment-1

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









