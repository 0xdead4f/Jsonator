![Alt text](jsonator.png)
# Jsonator: JSON Fuzzing Wordlist Generator

Jsonator is a tool designed to generate fuzzing wordlists specifically for JSON data structures. It aids in discovering potential vulnerabilities, misconfigurations, or edge cases in applications that handle JSON data. 

The objective actually to find unexpected behavior of the software or API.

## Features

- output in stdout

## Usage

To start generating fuzzing wordlists, use the following command-line syntax:

```bash
python jsonator.py [key1] [key2] [value1] [value2]
```
## Examples

- Generate a basic wordlist:
  ```bash
  python jsonator.py username password admin@admin.com user1@user.com
  ```

## Contributing

Contributions are welcome! Please read the [Contribution Guidelines](CONTRIBUTING.md) for details on how to contribute to this project.

