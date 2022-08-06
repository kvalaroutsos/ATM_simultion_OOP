class Services:
# There are the available methods for this class
    def __init__(self,balance, name):
        self.balance=balance
        self.name=name

#Method for withdraw money
    def get_money(self):
        try:
            wanted = int(input('What is your wanted amount of money?'))

            if wanted < 0:
                print('Please insert a valid amount')
                wanted = 0
                return wanted

            elif (wanted <= self.balance):
                if (wanted % 20 == 0) or (wanted % 50 == 0):
                    print(f'Here is your withdraw of {wanted}€')
                    return wanted

                else:
                    print('Please select a combination of 20€ or 50€')

                    wanted = 0
                    return wanted

            else:
                print('The wanted amount surpass your balance account')

                wanted = 0
                return wanted
        except ValueError:
            print('Please give an integer!')
            wanted=0
            return wanted


#Method for deposit money
    def give_money(self):
        try:
            deposit_amount = int(input('Please insert your amount'))

            if (deposit_amount>0) and (deposit_amount % 5==0):
                print(f'There is a successful deposit of {deposit_amount}€ in your account Mr/Ms {self.name}')
                return deposit_amount

            else:
                print('Please insert only bank notes')
                deposit_amount=0
                return deposit_amount
        except ValueError:
            print('Please give an integer!')
            deposit_amount = 0
            return deposit_amount


#Method for new current balance

    def current_balance(self,balance,transaction):
        new_balance=balance+transaction
        print(f'Your new balance is {new_balance}')
        return new_balance

#Method for pin changing
    def pin_change(self,pin):
        try:
            new_pin=input('Please give your new 4 digits pin')

            if len(new_pin)==4:
                new_pin=int(new_pin)
                validate=int(input('Please retype your new pin'))
                if validate==new_pin:
                    return new_pin

                else:
                    print('Sorry your pin entries do not match. Try again!')
                    return pin
            else:
                print('Please give a 4 digits number')
                return pin
        except ValueError:
            print('Please give a 4 digit integer number')
            return pin