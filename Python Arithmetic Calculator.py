import os
os.system("cls")
print("\tARITHMETIC OPERATIONS")
print('='*45)
perform='Y'
def Arithmetic():
	a=int(input('enter operand 1: '))
	operator=input('Select operator [**,*,/,//,%,+,-]: ')
	b=int(input('enter operand 2: '))
	if operator=='**':
		return a**b
	elif operator=='*':
		return a*b
	elif operator=='/':
		return a/b if b!=0 else "Error: Division by zero"
	elif operator=='//':
		return a//b if b!=0 else "Error: Division by zero"
	elif operator=='%':
		return a%b if b!=0 else "Error: Division by zero"
	elif operator=='+':
		return a+b
	elif operator=='-':
		return a-b
	else:
		return "Invalid operator"
while perform=='Y':
			perform=input('Do you want to perform any operations [Y/N]: ').upper()
			if perform!='Y':
				break
			result=Arithmetic()
			print("="*33)
			print(f'|	The Answer is: {result}	|')
			print("="*33)
