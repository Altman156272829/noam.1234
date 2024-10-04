from PIL import Image
import io
code =int(input("enter your code"))
def to_binary(data):
    return ''.join(format(byte, '08b') for byte in data)

def xor_encrypt(data, key):
    return ''.join(chr(ord(c) ^ key) for c in data)

def main():
    try:
        
        with open(r"C:\Users\User\Downloads\אקר.jpeg", 'rb') as image:
            binary_data = to_binary(image.read()) # החלק שבו יש בינארי
            key = 123  # מפתח ההצפנה
            encrypted_data = xor_encrypt(binary_data, key)
            with open(r'C:\\Users\\User\\Downloads\\image_encrypted.bin', 'wb') as encrypted_file:
                encrypted_file.write(bytes(encrypted_data, 'utf-8'))
            print("Data encrypted and saved successfully.")
    except Exception as e:
        print(f"Error: {e}")

def decoder():
    with open(r'C:\\Users\\User\\Downloads\\image_encrypted.bin','rb') as text:
        encrypted_file = text.read()
        bin_encrypted_file = int(to_binary(encrypted_file))
        print(bin_encrypted_file)
        data = bin_encrypted_file ^ code
        data = bytes(data)
    with open(r'C:\\Users\\User\\Downloads\\secret.bin', 'wb') as secret:
        secret.write(data)
        Img = Image.open(secret)
        Img.show()

main()

decoder()