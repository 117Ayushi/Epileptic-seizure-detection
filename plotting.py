import matplotlib.pyplot as plt
import csv
import numpy as np


active_patient = {
    'Dog_1_test_segment': {
        'seizure': [],
        'early': []
    },
    'Dog_2_test_segment': {
        'seizure': [],
        'early': []
    },
    'Dog_3_test_segment': {
        'seizure': [],
        'early': []
    },
    'Dog_4_test_segment': {
        'seizure': [],
        'early': []
    },
    'Patient_1_test_segment': {
        'seizure': [],
        'early': []
    },
    'Patient_2_test_segment': {
        'seizure': [],
        'early': []
    },
    'Patient_3_test_segment': {
        'seizure': [],
        'early': []
    },
    'Patient_4_test_segment': {
        'seizure': [],
        'early': []
    },
    'Patient_5_test_segment': {
        'seizure': [],
        'early': []
    },
    'Patient_6_test_segment': {
        'seizure': [],
        'early': []
    },
    'Patient_7_test_segment': {
        'seizure': [],
        'early': []
    },
    'Patient_8_test_segment': {
        'seizure': [],
        'early': []
    }
}


with open('submissions/output.csv') as csvfile:
    active_patient_csv = csv.reader(csvfile)
    for clip, seizure, early in active_patient_csv:
        active_patient[clip]['seizure'].append(seizure)
        active_patient[clip]['early'].append(early)


fig1 = plt.figure()
dog_1 = fig1.add_subplot(211)
dog_1.set_title('DOG_1')

fig2 = plt.figure()
dog_2 = fig2.add_subplot(211)
dog_2.set_title('DOG_2')

fig3 = plt.figure()
dog_3 = fig3.add_subplot(211)
dog_3.set_title('DOG_3')

fig4 = plt.figure()
dog_4 = fig4.add_subplot(211)
dog_4.set_title('DOG_4')

fig5 = plt.figure()
patient_1 = fig5.add_subplot(211)
patient_1.set_title('PATIENT_1')

fig6 = plt.figure()
patient_2 = fig6.add_subplot(211)
patient_2.set_title('PATIENT_2')

fig7 = plt.figure()
patient_3 = fig7.add_subplot(211)
patient_3.set_title('PATIENT_3')

fig8 = plt.figure()
patient_4 = fig8.add_subplot(211)
patient_4.set_title('PATIENT_4')

fig9 = plt.figure()
patient_5 = fig9.add_subplot(211)
patient_5.set_title('PATIENT_5')

fig10 = plt.figure()
patient_6 = fig10.add_subplot(211)
patient_6.set_title('PATIENT_6')

fig11 = plt.figure()
patient_7 = fig11.add_subplot(211)
patient_7.set_title('PATIENT_7')

fig12 = plt.figure()
patient_8 = fig12.add_subplot(211)
patient_8.set_title('PATIENT_8')


dog_1.scatter(active_patient['Dog_1_test_segment']['early'],active_patient['Dog_1_test_segment']['seizure'], c='#138D75')
dog_2.scatter(active_patient['Dog_2_test_segment']['early'],active_patient['Dog_2_test_segment']['seizure'], c='#00FA9A')
dog_3.scatter(active_patient['Dog_3_test_segment']['early'],active_patient['Dog_3_test_segment']['seizure'], c='#90EE90')
dog_4.scatter(active_patient['Dog_4_test_segment']['early'],active_patient['Dog_4_test_segment']['seizure'], c='#3CB371')

patient_1.scatter(active_patient['Patient_1_test_segment']['early'],active_patient['Patient_1_test_segment']['seizure'], c='#FFA07A')
patient_2.scatter(active_patient['Patient_2_test_segment']['early'],active_patient['Patient_2_test_segment']['seizure'], c='#FA8072')
patient_3.scatter(active_patient['Patient_3_test_segment']['early'],active_patient['Patient_3_test_segment']['seizure'], c='#E9967A')
patient_4.scatter(active_patient['Patient_4_test_segment']['early'],active_patient['Patient_4_test_segment']['seizure'], c='#F08080')
patient_5.scatter(active_patient['Patient_5_test_segment']['early'],active_patient['Patient_5_test_segment']['seizure'], c='#CD5C5C')
patient_6.scatter(active_patient['Patient_6_test_segment']['early'],active_patient['Patient_6_test_segment']['seizure'], c='#DC143C')
patient_7.scatter(active_patient['Patient_7_test_segment']['early'],active_patient['Patient_7_test_segment']['seizure'], c='#B22222')
patient_8.scatter(active_patient['Patient_8_test_segment']['early'],active_patient['Patient_8_test_segment']['seizure'], c='#FF0000')



# plt.xlabel('Seizures Range')
# plt.ylabel('Seizure Detected')
plt.show()
