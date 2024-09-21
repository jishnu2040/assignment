"""
    22. Write a program to create Class with name and account number and implement get and set, with property 
        decorator and making account number and name private.  
"""

class SecretData:
  # variable name and accounr number declared as private
  __name = ""
  __account_number = ""
 
  # method to set and get name and account number
  def set_name(self, name):
    self.__name = name
 
  def get_name(self):
    return self.__name
 
  def set_account_num(self, account_no):
    self.__account_number = account_no
 
  def get_account_num(self):
    return self.__account_number
 
 
# create object
secret = SecretData()
 
# set name and account no
secret.set_name("Varun K V")
secret.set_account_num("123456789102")
 
# display output using get
print("Account Holder Name : ", secret.get_name())
print("Account Number : ", secret.get_account_num())