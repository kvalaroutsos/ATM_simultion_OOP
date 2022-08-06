import random
import pandas as pd
from faker import Faker

# Execute This code in order to produce some fake data with Pin numbers, balance accounts and name of the owner.
df=pd.DataFrame.from_dict({
    'Code':[],
    'Balance':[],
    'Name':[],

})

print(df)

numbers=list(range(1000,10000))
print(len(numbers))
fake=Faker()

for i in range(1000):

    radn=random.choice(numbers)

    numbers.remove(radn)
    radn=str(radn)

    cash=random.randint(0,1000)
    name=fake.last_name()

    df.loc[len(df)]=[radn, cash, name]

print(df)
df.to_csv('client_list.csv',index=False)


