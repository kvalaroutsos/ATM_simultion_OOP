class PersonAuth:

# Authorizes a person to use the account

    def authorized(self,df):
        try:
            for i in range(3):

                my_code = input('your Pin?')
                if int(my_code) in list(df.Code):

                    amount = df.loc[df['Code'] == int(my_code)]
                    indexx = amount.index.values

                    amount = df.loc[df['Code'] == int(my_code)].iloc[0, 1]

                    name = df.loc[df['Code'] == int(my_code)].iloc[0, 2]

                    pin=df.loc[df['Code'] == int(my_code)].iloc[0, 0]
                    break

                elif int(i) == 2:
                    print('You had 3 failed attempts your card is withholded')
                    exit()

            print(f'Your Current ammount Mr/Ms {name} is {amount}€')
            return amount, name, indexx, pin
        except ValueError:
            print('Please give integer numbers')
            exit()

#Method for updating the database
    def update_file(self,df,indexx, new_balance, pin):

        df.iloc[[indexx], [0]] = pin
        df.iloc[[indexx], [1]] = new_balance
        df.to_csv('client_list.csv', index=False)





