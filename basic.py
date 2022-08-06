from services import Services
from person_auth import PersonAuth
import pandas as pd


df=pd.read_csv('client_list.csv')  #Our practise dataset contains pin code, balance account and name

card_in=True


authorized=PersonAuth()
amount, name, indexx, pin =authorized.authorized(df)
while card_in:

        action = input('What would you like to do withdraw[w], deposit[d], change pin [c], exit[e]?')
        if action.lower()[0] == 'w':

                withdraw = Services(amount, name)
                wanted=withdraw.get_money()
                new_balance=withdraw.current_balance(amount, -wanted)
                authorized.update_file(df,indexx,new_balance, pin)
                amount = new_balance

        elif action.lower()[0] == 'd':

                deposit = Services(amount, name)
                deposit_amount=deposit.give_money()
                new_balance=deposit.current_balance(amount, deposit_amount)
                authorized.update_file(df,indexx,new_balance, pin)
                amount = new_balance

        elif action.lower()[0] =='e':
                print(f'Good Buy Mr/Ms {name}')
                print('Card returned')

                card_in =False

        elif action.lower()[0] =='c':
                pinchange = Services(amount, name)
                newpin=pinchange.pin_change(pin)
                authorized.update_file(df, indexx, amount, newpin)

        else:
                print('Not clear action is requested')

