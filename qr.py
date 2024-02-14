import qrcode

def generate_qr_code(link, filename="qr_code.png"):
    # Generate QR code
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    qr.add_data(link)
    qr.make(fit=True)

    # Create an image from the QR code
    img = qr.make_image(fill_color="black", back_color="white")

    # Save the image
    img.save(filename)

    print(f"QR code generated successfully as {filename}")

if __name__ == "__main__":
    link = input("Enter the link you want to encode: ")
    filename = input("Enter the filename to save the QR code (default: qr_code.png): ")
    if not filename:
        filename = "qr_code.png"
    generate_qr_code(link, filename)
