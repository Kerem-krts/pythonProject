import pandas as pd
path = r"C:\Users\KEREM\Desktop\iris\iris.data" #dataset yolu

csv_data = pd.read_csv(path, delimiter=",",header=None) #dataset okuma

exel_path = r"C:\Users\KEREM\Desktop\iris\iris2.xlsx" #exel yolu
smp_csv_data = csv_data.sample(frac=1) #karıştırma

smp_csv_data[4] = smp_csv_data[4].replace("Iris-setosa", "1")  #değer değiştirme
smp_csv_data[4] = smp_csv_data[4].replace("Iris-virginica", "2")
smp_csv_data[4] = smp_csv_data[4].replace("Iris-versicolor", "3")


smp_csv_data.to_excel(exel_path,index=False) #exele çevirme