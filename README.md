# Advanced Brute Cipher (ABC)
## Et tu, Brute?
BruteCipher is a simple and secure encryption tool that performs all operations locally in your browser using HTML, JavaScript, and CSS. Manage your encryption keys without relying on external CDNs. This project is a web-based encryption and decryption tool that supports multiple languages and includes features like dark mode, mobile compatibility, and key management. It's designed to provide a user-friendly interface for secure data handling.

# Table of Contents
1. [Demo](#demo)
2. [Features](#features)
3. [Installation HTML Version](#installation-html-version)
4. [Python Version](#python-version)
   - [Installation](#installation)
   - [Updating the Application](#updating-the-application)
   - [Usage](#usage)
   - [Removing the Project](#removing-the-project)
5. [Extended Description](#extended-description)
   - [Key Features](#key-features)
   - [How It Works](#how-it-works)
   - [Future Plans](#future-plans)
6. [Important Notice](#important-notice)
7. [Contributing](#contributing)
8. [License](#license)
9. [BruteCipher Wiki](#brutecipher-wiki)
   - [About BruteCipher](#about-brutecipher)
     - [Origin of the Name](#origin-of-the-name)
     - [Unique Aspects of BruteCipher](#unique-aspects-of-brutecipher)
   - [Future Enhancements](#future-enhancements)


![cover](https://github.com/dogukansahil/AdvancedBruteCipher/blob/main/docs/public/cover.jpg?raw=true)


Welcome to BruteCipher, a simple and secure encryption tool inspired by historical figures. This is the beta version of our project, and we are constantly working on improving its features and security.

## Demo

**[Demo](https://htmlpreview.github.io/?https://github.com/dogukansahil/AdvancedBruteCipher/blob/main/webapp/index.html) | Do not use here for encryption and decryption.**

## Features
- **Local Processing**: All encryption and decryption processes occur locally within your browser, meaning your data is never shared with external servers. (Only the language selection is stored in the browser.)
- - All operations are performed locally in your browser using HTML, JavaScript, and CSS or local Python code.
- **Robust Algorithm**: Utilizes a double hashing algorithm for enhanced security, inspired by the historical figure Brutus.
- **Secure Key Management**: Manage your encryption keys securely within your browser.
- **User-Friendly Interface**: Simple and intuitive interface for easy encryption and decryption.
- **Multilingual Support**: Supports multiple languages including English, **Turkish, Russian, Spanish, German, Italian, and Chinese**.

## Installation HTML Version 

Simply download and open the `index.html` file to begin using the tool.

1. Clone the repository:
    ```bash
    git clone https://github.com/dogukansahil/AdvancedBruteCipher.git
    ```
2. Navigate to the project directory:
    ```bash
    cd AdvancedBruteCipher/webapp
    ```
3. Open the `index.html` file in your browser to use the tool:
    ```bash
    open index.html
    ```

## Python Version

### Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/dogukansahil/AdvancedBruteCipher.git
    ```
2. Navigate to the project directory:
    ```bash
    cd AdvancedBruteCipher
    ```
3. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
4. Run the Python application:
    ```bash
    python AdvancedBruteCipher.py
    ```

### Updating the Application

To ensure you have the latest updates and improvements:

1. Navigate to the project directory if you are not already there:
    ```bash
    cd AdvancedBruteCipher
    ```
2. Pull the latest changes from the repository:
    ```bash
    git pull
    ```

This will update your local copy with the most recent version from the GitHub repository.

### Usage

1. Enter the text you want to encrypt or decrypt in the input field.
2. Provide the necessary keys in the respective fields.
3. Click on the "Encrypt" or "Decrypt" button to see the result in the output area.

### Removing the Project

If you want to remove the project from your local machine, you can use the following command:
    ```
    rm -rf AdvancedBruteCipher
    ```

## Extended Description

BruteCipher aims to provide a user-friendly and secure way to manage text encryption and decryption without relying on external services or CDNs. All operations are performed locally in your browser using HTML, JavaScript, and CSS, ensuring that your data remains private and secure.

### Key Features

- **Local Processing**: All encryption and decryption processes occur locally within your browser, meaning your data is never shared with external servers.
- **Robust Algorithm**: Utilizes a double hashing algorithm for enhanced security, inspired by the historical figure Brutus.
- **Secure Key Management**: Manage your encryption keys securely within your browser.
- **User-Friendly Interface**: Simple and intuitive interface for easy encryption and decryption.

### How It Works

- **Double Hashing Algorithm**: The algorithm applies two rounds of hashing to the input text, with each round using a different key. This makes it significantly harder for unauthorized parties to decrypt the data without the correct keys.
- **Key Management**: Users can generate and store their keys locally, ensuring that sensitive information is not exposed to external threats.
- **Passphrase Protection**: The passphrase can be any length, providing flexibility and adding an extra layer of security and convenience.

### Future Plans

We are continuously working on enhancing BruteCipher. Future updates will include:
- Improved user interface
- Enhanced security features
- Support for more complex encryption algorithms
- Integration with local password storage systems

## Important Notice

**Warning:** This is a beta version. Do not use BruteCipher for important or sensitive information at this stage. We recommend waiting for the stable release for critical use cases. **Do not select important passwords with this algorithm and always keep them up to date.** Parameters may change!

## Contributing

We welcome contributions! Please fork this repository and submit pull requests to help us improve BruteCipher.

## License

This project is open source and available under the [MIT License](LICENSE).

# BruteCipher Wiki

## About BruteCipher

### Origin of the Name
The name **BruteCipher** is inspired by both the historical figure Brutus and the concept of brute force in cryptography. The famous phrase **"Et tu, Brute?"** (And you, Brutus?) from Shakespeare's play Julius Caesar symbolizes betrayal and intrigue, themes often associated with the need for secure communication. The term **brute force** refers to a method in cryptography where an attacker tries all possible keys to decrypt data. BruteCipher aims to provide robust encryption, making such brute force attacks impractical.

### Unique Aspects of BruteCipher
- **No External CDN Dependencies**: BruteCipher does not rely on any external Content Delivery Networks (CDNs). All code and resources are hosted locally, ensuring that your data remains private and secure.
- **Local Encryption and Decryption**: All encryption and decryption operations are performed locally within your browser using HTML, JavaScript, and CSS. This means your data is never transmitted over the internet, providing an additional layer of security.

## Future Enhancements
We are continuously working on enhancing BruteCipher. Future updates will include:
- Improved user interface
- Enhanced security features
- Support for more complex encryption algorithms
- Integration with local password storage systems
