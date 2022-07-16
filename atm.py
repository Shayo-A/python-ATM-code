import sys
import getpass
class Bank_Account:
    def __init__(self):
        self.balance=0
        print('''
              #############################################################################
              ##                                                                         ##
              ##               welcome TO CEPHAS DIGITAL BANK ATM POINT                  ##
              ##                                                                         ##
              #############################################################################
              ''')
        
    def login_page(self):
        print(' kindly sign-in')
        d={'shayo':'1234','remond':'2345','toyin':'9001','josh':'0011'}
        a=list(d.keys())
        b=list(d.values())
        counter=0
        username=input('enter username:')
        username=username.lower()
        while username.lower() not in d.keys():
            print('DEAR',username.upper(),',\nyou have not register with us ,kindly visit our customer care for further enquries')
            sys.exit()
        while username.lower() in a:
            print('welcome',username.upper(),'\n','kindly enter your password')
            password=getpass.getpass('enter your password:')
            while  password!=b[a.index(username)]: 
                print('error!!!!,try again you have',2-counter,'more attempt')
                password=getpass.getpass('kindly re-enter your password:')
                counter+=1 
                if counter>=3:
                    print('your account have deactivated,visit our nearest branch')
                    sys.exit()
            if password==b[a.index(username)]:
                    print('login successful')
            break
    def deposit(self):
              # self.amount
               print('''
                     ########################################################################
                     ##            press the following to deposit the specifyed amount:    ##
                     ########################################################################
                   1.500                                                                  4.10000
                   2.1000                                                                 6.15000
                   3.2000                                                                 7.50000
                   4.5000                                                                 8. other amount
                ''')
               option=input('pick the amount you want to withdraw:')
               while option not in['1','2','3','4','5','6','7','8']:
                   print('kindly pick option between 1-8')
                   option=input('pick the amount you want to withdraw:')
               if option=='8':
                     print('enter the amount you to withdraw:')
                     amount=input('enter amount to withdraw here:')
                
                     while  not amount.isdecimal():
                        print('error!!!!!! kindly enter floating nimber:')
                        amount=input('enter amount to withdraw here:')
               elif option=='1':
                    amount=500
               elif option=='2':
                      amount=1000
                      print('you want to withdraw #1000 ')
               elif option=='3':
                      amount=2000
                      #amont=float(res)
               elif option=='4':
                      amount=5000
                      #amont=float(res)
               elif option=='5':
                      amount=10000
                      #amont=float(res)
               elif option=='6':
                      amount=15000
                      #amont=float(res)
               elif option=='7':
                      amount=50000
               amount=float(amount)
               # amount=float(input('enter the amount you want to deposit:#'))
               self.balance+=amount
               print('\n AMOUNT DEPOSITED=','#',amount)
    def withdraw(self):
                #self.amont
                print('''
                      #########################################################################
                      ##         press the following to withdraw the specifyed amount:       ##
                      #########################################################################
                   1.500                                                                  4.10000
                   2.1000                                                                 6.15000
                   3.2000                                                                 7.50000
                   4.5000                                                                 8. other amount
                ''')
    
                option=input('pick the amount you want to withdraw:')
                while option not in['1','2','3','4','5','6','7','8']:
                   print('kindly pick option between 1-8')
                   option=input('pick the amount you want to withdraw:')
                if option=='8':
                     print('enter the amount you to withdraw:')
                     amont=input('enter amount to withdraw here:')
                
                     while  not amont.isdecimal():
                        print('error!!!!!! kindly enter floating nimber:')
                        amont=input('enter amount to withdraw here:')
                elif option=='1':
                    amont=500
                elif option=='2':
                      amont=1000
                      print('you want to withdraw #1000 ')
                elif option=='3':
                      amont=2000
                      #amont=float(res)
                elif option=='4':
                      amont=5000
                      #amont=float(res)
                elif option=='5':
                      amont=10000
                      #amont=float(res)
                elif option=='6':
                      amont=15000
                      #amont=float(res)
                elif option=='7':
                      amont=50000
                amont=float(amont)
                if self.balance>=amont:
                 self.balance-=amont
                 print('\n you withdraw #',amont)
                else:
                    print('\n insufficient balance')
               # break
    def account_balance(self):
                print('\n account balance=#',self.balance)
c=Bank_Account()
choice=1
while choice!=0:
    c.login_page()
    print('''
          press 1 to deposit
          presss 2 to withdraw
          press 3 to check account balance''')
    d=input('enter your option')
    if d=='1':
        c.deposit()
        d=input()
    elif d=='2':
        c.withdraw()
        d=input()
    elif d=='3':
        c.account_balance()
        d=input()
    