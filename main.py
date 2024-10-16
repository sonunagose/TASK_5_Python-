from utils.userData import getNumericData
from utils.dateFormate import custom_date_format

def main():
    user_input=input('enter any data: ')
    data=getNumericData(user_input)
    print(f'data={data}')

    print()
    print('------')
    print()

    date_string=input("enter date: ")
    d=custom_date_format(date_string)
    print(f'd={d}')

if __name__=='__main__':
  main()