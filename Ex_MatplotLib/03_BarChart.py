import matplotlib.pyplot as plt
%matplotlib inline

blood_sugar_men = [113, 85, 90, 150, 88, 93, 115, 135, 80, 77, 82, 129]
blood_sugar_women = [67, 98, 89, 120, 133, 150, 84, 69, 89, 79, 120, 112, 100]

plt.hist([blood_sugar_men, blood_sugar_women], 
             bins=[80, 100, 125, 150], rwidth=0.95,
             color=['green', 'orange'],
             label=['men', 'women'])

plt.title('Blood Sugar Analysis')
plt.xlabel('Sugar Range')
plt.ylabel('No. of Patients')

plt.legend()