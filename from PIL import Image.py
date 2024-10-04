from PIL import Image
import io

def to_binary(data):
    return ''.join(format(byte, '08b') for byte in data)

def xor_encrypt(data, key):
    return bytes([b ^ key for b in data])

def binary_to_bytes(binary_data):
    byte_data = bytearray()
    for i in range(0, len(binary_data), 8):
        byte = binary_data[i:i+8]
        byte_data.append(int(byte, 2))
    return byte_data

def save_image(byte_data, output_path):
    image = Image.open(io.BytesIO(byte_data))
    image.save(output_path)
    image.show()  # מציג את התמונה לאחר השחזור

def main():
    try:
        print("Starting...")
        image_path = r'C:\Users\User\Downloads\אקר.jpeg'
        print(f"Opening image at: {image_path}")
        
        # קריאת התמונה ופעולה בינארית
        with open(image_path, 'rb') as image:
            binary_data = image.read()
            key = 123  # מפתח ההצפנה
            print("Encrypting data...")
            encrypted_data = xor_encrypt(binary_data, key)
            output_path = r'C:\\Users\\User\\Downloads\\image_encrypted.bin'
            
            # שמירת המידע המוצפן לקובץ
            with open(output_path, 'wb') as encrypted_file:
                encrypted_file.write(encrypted_data)
            print(f"Data encrypted and saved successfully to {output_path}.")
            
            # שיחזור התמונה מהמידע המוצפן
            restored_image_path = r'C:\\Users\\User\\Downloads\\restored_image.png'
            decrypted_data = xor_encrypt(encrypted_data, key)  # פענוח בעזרת XOR עם אותו מפתח
            save_image(decrypted_data, restored_image_path)
            print(f"Image restored and saved successfully to {restored_image_path}.")
    except Exception as e:
        print(f"Error: {e}")

main()