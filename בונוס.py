from PIL import Image

def image_to_binary(image_path):
    try:
        with Image.open(image_path) as img:
            binary_data = []
            for pixel in img.getdata():
                r, g, b = pixel[:3]  # וודא שאתה מתייחס רק לרכיבי ה-RGB של הפיקסל
                binary_pixel = f'{r:08b} {g:08b} {b:08b}'
                binary_data.append(binary_pixel)
                print(binary_pixel)  # הדפסת נתוני הפיקסלים הבינאריים
            return binary_data
    except Exception as e:
        print(f"Error: {e}")     

image_path = r"C:\Users\User\Downloads\אקר.jpeg"  # ודא שהמסלול נכון
image_to_binary(image_path)

