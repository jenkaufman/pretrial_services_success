# Pretrial Services Success
Statistical analysis of Pretrial Services success rates

***

## Overview
Pretrial Services in Denver Colorado provides supervision for defendants ordered by the Court to supervised conditions of release. Defendants can be released successfully from pretrial supervision once their case is sentenced or dismissed, or if supervision is terminated due to compliance. Defendants can also be released unsuccessfully from pretrial supervision if they fail to appear (FTA) for Court or receive new charges while under pretrial supervision.

This project is to determine whether success rates vary by age, ethnicity, or length of supervision.

The data set is from my current employer, City and County of Denver, Department of Public Safety, Community Corrections, and represents all defendants released from pretrial services during calendar years 2018 and 2019.

***

## Hypotheses and Statistical Tests
### Age <br>
Hypothesis 1
* $H_0$: Successful and unsuccessful groups do not vary by age.<br>
* $H_a$: Successful and unsuccessful groups do vary by age.<br>
alpha=0.05<br>
statistical test=Mann–Whitney U test<br>
![Age](/Age.png)

### Gender
Hypothesis 2 
* $H_0$: Pretrial services success and gender are independent.<br>
* $H_a$: Pretrial services success and gender are not independent.<br>
alpha with Bonferroni Correction=0.025 (0.05/2)<br>
statistical test=chi-squared test of independence<br>

### Ethnicity
Hypothesis 3
* $H_0$: Pretrial services success and ethnicity are independent.<br>
* $H_a$: Pretrial services success and ethnicity are not independent.<br>
alpha with Bonferroni Correction=0.0166 (0.05/3)<br>alpha with Bonferroni Correction=0.025 (0.05/2)<br><br>
statistical test=chi-squared test of independence<br>

### Length of Supervision
Hypothesis 4
* $H_0$: Successful and unsuccessful groups do not vary by length of supervision.<br>
* $H_a$: Successful and unsuccessful groups do vary by length of supervision.<br>
alpha with Bonferroni Correction=0.0125 (0.05/4)<br>
statistical test=Mann–Whitney U test<br>
***

## Results

***

## Future Analysis