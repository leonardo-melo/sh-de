1) About once every two weeks, SWORD asks its patients how much they would recommend its therapy to someone they know on a scale from 0 to 10. Assume you have a table called Scores having a json string containing (among other things) the satisfaction scores of SWORD’s patients along with the corresponding date, as follows:

| id | patient-id | scores                                        | date       |
|----|------------|-----------------------------------------------|------------|
| 1  | 1323       | {‘satisfaction’: 9, ‘pain’: 2, ‘fatigue’: 2}  | 2020-06-25 |
| 2  | 9032       | {‘satisfaction’: 2, ‘pain’: 7, ‘fatigue’: 5}  | 2020-06-30 |
| 3  | 2331       | {‘satisfaction’: 7, ‘pain’: 1, ‘fatigue’: 1}  | 2020-07-05 |
| 4  | 2303       | {‘satisfaction’: 8, ‘pain’: 9, ‘fatigue’: 0}  | 2020-07-12 |
| 5  | 1323       | {‘satisfaction’: 10, ‘pain’: 0, ‘fatigue’: 0} | 2020-07-09 |
|    | 2331       | {‘satisfaction’: 8, ‘pain’: 9, ‘fatigue’: 5}  | 2020-07-20 |

One of our most important metrics is the NPS which is calculated with the following formula:

number of patients

$$ NPS = {number.of.promoters − number.of.detractors \over number.of.patients} $$

Patients are classified in the following groups according to their most recent satisfaction
report:
● > 8 is a promoter
● < 7 is a detractor

Write a SQL query to calculate SWORD’s Digital Therapist NPS for each month. E.g.:

| month    | NPS |
|----------|-----|
| January  | 50  |
| February | 45  |
| March    | 53  |
| ...      | ... |