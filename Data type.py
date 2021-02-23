Python 3.2.3 (default, Apr 11 2012, 07:12:16) [MSC v.1500 64 bit (AMD64)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> a = input('Please enter a number')
Please enter a number 2
>>> b = input ('Enter another number')
Enter another number 8
>>> sum = a + b
>>> print ('\ndata type:', sum, type(sum))

data type:  2 8 <class 'str'>
>>> sum = int(a) + int (b)
>>> print ('Data type sum', sum, type(sum))
Data type sum 10 <class 'int'>
>>> c = print('Enter two whole numbers')
Enter two whole numbers
>>> c = input('Enter a number')
Enter a number9
>>> d = input('Enter an another number')
Enter an another number7
>>> sum = int(c) + int(d)
>>> print('Data type sum', sum, type(sum))
Data type sum 16 <class 'int'>
>>> e = input('Enter a number with fractional part')
Enter a number with fractional part1.5
>>> f = input('Enter another number with a fractional part')
Enter another number with a fractional part7.2
>>> sum = float(e) + float(f)
>>> print ('Data type sum', sum, type(sum))
Data type sum 8.7 <class 'float'>
>>> 
