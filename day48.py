import qrcode
import cv2
import os

def generate_qr(text, filename="my_qr.png"):
    img = qrcode.make(text)
    img.save(filename)
    print(f"✔ QR Code saved as {filename}")

def scan_qr(image_path):
    if not os.path.exists(image_path):
        print("❌ File not found!")
        return

    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()

    data, bbox, rectified = detector.detectAndDecode(img)

    if data:
        print("\n--- QR SCAN RESULT ---")
        print("Decoded Text:", data)
        print("-----------------------\n")
    else:
        print("❌ QR code not detected!")

def main():
    while True:
        print("\n--- QR CODE TOOL ---")
        print("1. Generate QR")
        print("2. Scan QR from Image")
        print("3. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            text = input("Enter text or URL to convert: ")
            filename = input("QR File Name (default: my_qr.png): ") or "my_qr.png"
            generate_qr(text, filename)

        elif choice == "2":
            image_path = input("Enter QR image filename: ")
            scan_qr(image_path)

        elif choice == "3":
            print("Exiting...")
            break

        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
