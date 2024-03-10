print(f"NameError {type(NameError)}-{issubclass (NameError, BaseException)}")

a=1
b=0
try:
    a / b
except ZeroDivisionError:
    print('na 0 nemohna dilutu')

try:
    a=open('file.txt', 'r')
except FileNotFoundError:
    print('fail ne znaideno')

import warnings
warnings.warn("Warning, no code here", SyntaxWarning)

import warnings
warnings.simplefilter ( "ignore", SyntaxWarning)
warnings.simplefilter ( "always", ImportWarning)
warnings.warn( "Warning, no code here", SyntaxWarning)
warnings.warn( "Warning, module not import", ImportWarning)