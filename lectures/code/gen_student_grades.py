# Generates fack student grades for testing

import numpy as np
import pandas as pd

output_file = "student_grades.csv"
columns = ['lab1','lab2','lab3','lab4','quiz1','quiz2']
sample_count = 200

student_avg = np.random.normal(loc=70, scale=12, size=sample_count).astype(int)
student_avg[student_avg > 100] = 100

student_grades = np.empty((sample_count, len(columns)), dtype=int)
for s in range(sample_count):
    grades = np.random.normal(loc=student_avg[s], scale=3, size=len(columns)).astype(int)
    grades[grades > 100] = 100
    student_grades[s, :] = grades

student_grades_df = pd.DataFrame(student_grades, columns=columns)
student_grades_df.to_csv(output_file, index=False)
