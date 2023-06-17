import pandas as pd

file_name = "Test 1.txt"

with open(file_name, 'r') as file: 
  lines = file.readlines()

dates = []
datas = []
prices = []
accounts = []
descriptions = []

for line in lines:
  line = line.strip()
  if '/' in line:
    date = line
  elif line !="":
    data = line.split()             
    price = float(data[0])           
    account = data[1]                
    description = ' '.join(data[3:])

    prices.append(price)
    dates.append(date)
    accounts.append(account)
    descriptions.append(description)
    

# Conver list to dataframe
df = pd.DataFrame(
    {
    'Dates': dates,
    'Price': prices,
    'Account': accounts,
    'Description': descriptions
    }
)

# Save file in excel
test_1_excel = 'Test_1.xlsx'
df.to_excel(test_1_excel, index = False)

# Open excel file
df = pd.read_excel('Test_1.xlsx')
df
