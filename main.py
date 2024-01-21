# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import pytest
class Calculator(object):
    def addition(self, num1, num2):
        print(num1+num2)
        return num1 + num2

    def multiply(self, num1, num2):
        return (num1 * num2)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    c = Calculator()
    c.addition(1,2)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
