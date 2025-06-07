import pandas as pd

#path of the file
ae = pd.read_csv("employees_messy.csv")

#remove spaces from all cells
ae = ae.applymap(lambda x: x.strip() if isinstance(x, str) else x)

#replace " with nothing
ae.replace('"','',regex=True, inplace=True)

#make first letter in each word capitale 
ae["Full Name"] = ae["Full Name"].str.title()

#convert string into number
ae["Salary"] = pd.to_numeric(ae["Salary"],errors="coerce")

#convert string into date
ae["StartDate"] = pd.to_datetime(ae["StartDate"], errors="coerce")

#make the strings in this coloumn all in lower form
ae["Department"] = ae["Department"].str.lower()

#deal with the % values as a numbers
ae["Bonus %"] = ae["Bonus %"].str.replace('%','').str.strip()
ae["Bonus %"] = pd.to_numeric(ae["Bonus %"],errors="coerce")
ae["Bonus %"] = ae["Bonus %"] / 100

ae["Active"] = ae["Active"].str.upper()

#remove duplicates
# ae = ae.drop_duplicates()
#reomve NA values
# ae = ae.dropna()

#sort with the salary in desecending form
ae = ae.sort_values(by="Salary", ascending=False)

#paste the csv values in a new csv file 
ae.to_csv("cleaned_employees.csv", index=False)

print(ae)