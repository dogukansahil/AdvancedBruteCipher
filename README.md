# BruteCipher
## Et tu, Brute?

![alt text](https://brutecipher.com/BruteCipher.jpg)

Welcome to BruteCipher, a simple and secure encryption tool inspired by historical figures. This is the beta version of our project, and we are constantly working on improving its features and security.

## Demo

[Demo](https://brutecipher.com/) | **Do not use here for encryption and decryption.**

## Features
- Encrypt and decrypt text using a robust algorithm
- Easy-to-use interface
- Secure key management
- No external CDN & API dependencies
- All operations are performed locally in your browser using HTML, JavaScript, and CSS or local python code.

## Installation HTML version 

Simply download and open the `index.html` file to begin using the tool.

1. Clone the repository:
    ```bash
    git clone https://github.com/dogukansahil/BruteCipher.git
    ```
2. Navigate to the project directory:
    ```bash
    cd BruteCipher
    ```
3. Open the `index.html` file in your browser to use the tool:
    ```bash
    open index.html
    ```

## Python Version

### Installation

1. Clone the repository:
    ```sh
    git clone https://github.com/dogukansahil/BruteCipher.git
    ```
2. Navigate to the project directory:
    ```sh
    cd BruteCipher
    ```
3. Make sure you have Python installed on your system. You can download it from [python.org](https://www.python.org/).
4. Run the Python application:
    ```sh
    python brutecipher.py
    ```

### Usage

1. Enter the text you want to encrypt or decrypt in the input field.
2. Provide the necessary keys in the respective fields.
3. Click on the "Encrypt" or "Decrypt" button to see the result in the output area.

### Removing the Project

If you want to remove the project from your local machine, you can use the following command:
    ```
    rm -rf BruteCipher
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
- **Passphrase Protection**: A 4-digit passphrase can be used to export and import keys, adding an extra layer of security and convenience.

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
