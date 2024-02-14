# QR Code Generator

This Python script allows you to generate a QR code that, when scanned, will open a specific link. It uses the `qrcode` library to create the QR code.

## Prerequisites

- Python 3.x installed on your system.
- `qrcode` library installed. You can install it using pip:

    ```bash
    pip install qrcode[pil]
    ```

## Installation

1. Clone the repository to your local machine:

    ```bash
    git clone https://github.com/your_username/qr-code-generator.git
    ```

2. Navigate to the project directory:

    ```bash
    cd qr-code-generator
    ```

## Usage

1. Run the Python script:

    ```bash
    python generate_qr_code.py
    ```

2. Enter the link you want to encode when prompted by the terminal.

3. Enter the filename to save the QR code (optional). If not provided, the default filename will be `qr_code.png`.

4. Press Enter, and the script will generate the QR code.

5. You can use any QR code scanner to scan the generated QR code. It will open the provided link when scanned.

## Example

```bash
$ python generate_qr_code.py
Enter the link you want to encode: https://example.com
Enter the filename to save the QR code (default: qr_code.png):
QR code generated successfully as qr_code.png
```

## Contributing

Contributions are welcome! If you find any issues or want to add new features, feel free to submit a pull request.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
