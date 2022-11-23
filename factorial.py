from pythonnet import load

load("coreclr")
import clr

reference = clr.AddReference('./Math/Math/bin/Debug/net6.0/publish/Math')
print(reference)
from Math import Calculator

factorial = Calculator.Factorial(6)
print(factorial)
