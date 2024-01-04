import sys
from string import Template



def method1(args):
    payload = f'"{args.key1}": "admin","{args.key2}": "admin"'
    print(template.substitute(payload=payload))

def method2(args):
    payload = f'"{args.key1}": null,"{args.key2}": null'
    print(template.substitute(payload=payload))

def method3(args):
    payload = f'"{args.key1}": "{args.input1}","{args.key2}": null'
    print(template.substitute(payload=payload))

def method4(args):
    payload = f'"{args.key1}": "{args.input1}","{args.key2}": true'
    print(template.substitute(payload=payload))

def method5(args):
    payload = f'"{args.key1}": "{args.input1}","{args.key2}": false'
    print(template.substitute(payload=payload))

if __name__ == "__main__":
    if len(sys.argv) != 5:
        print("Usage: python jsonator.py <arg1> <arg2> <arg3>")
        sys.exit(1)

    key1 = sys.argv[1]
    key2 = sys.argv[2]
    input1 = sys.argv[3]
    input2 = sys.argv[4]

    class Argument:
        def __init__(self):
            self.key1 = sys.argv[1]
            self.key2 = sys.argv[2]
            self.input1 = sys.argv[3]
            self.input2 = sys.argv[4]
    
    args = Argument()
    bracket = False
    # bracket = sys.argv[5]

    if bracket == True:
        template = Template("{$payload}")
    else:
        template = Template("$payload")
    
    method1(args)
    method2(args)
    method3(args)
    method4(args)