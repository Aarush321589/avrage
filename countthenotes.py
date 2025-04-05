#taking the total amount of the user
amount=int (input("please enter the amount to withdraw"))
#calculating the numbers of note
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10
print("notes of 100 Rs",note1)
print("notes of 50 Rs",note2)
print("notes of 10 Rs",note3)


