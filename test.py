import os
import ast


#eval("__import__('os').system('clear')", {'__builtins__':{}})



if __name__ == '__main__':
    cmd_api_client()
# A user-defined method named "eval" should not get flagged.
class Test(object):
    def eval(self):
        print("hi")
    def foo(self):
        self.eval()

Test().eval()
