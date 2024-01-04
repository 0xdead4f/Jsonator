![Jsonator](jsonator.png)
# Jsonator: JSON Fuzzing Wordlist Generator (On Development)

Jsonator is a tool designed to generate fuzzing wordlists specifically for JSON data structures. It aids in discovering potential vulnerabilities, misconfigurations, or edge cases in applications that handle JSON data. 

The objective actually to find unexpected behavior of the software or API.

## Features

- 40 custom json fuzzing technique
- output in stdout
- custom input

## Usage

To start generating fuzzing wordlists, define the input first in the ``input.json`` file :
```
{
    "key1":"username",
    "key2":"password",
    "value_key1":"admin@admin.com",
    "value_key1_2":"user@user.com",
    "value_key2":"Admin123",
    "value_key2_2":"User123",
    "ip":"127.0.0.1",
    "domain":"example.com"
}
```

Run the script :

```bash
python jsonator.py 
```
Output :
```
"username": "admin","password": "admin"
"username": null,"password": null
"username": "admin@admin.com","password": null
"username": "admin@admin.com","password": true
...
...
...
```
## Contributing

Contributions are welcome! 

