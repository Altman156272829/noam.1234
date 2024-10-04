from PIL import Image
import io

# טען את התמונה
from PIL import Image

with open(r'C:\Users\User\Downloads\אקר.jpeg', 'rb') as file:
    img = Image.open(file)
    img.show()
# שמור את התמונה כייצוג בינארי
with io.BytesIO() as output:
    img.save(output, format="JPEG")
    binary_data = output.getvalue()

# הדפס את המידע הבינארי או שמור לקובץ
print(binary_data)
with open('output_image.bin', 'wb') as f:
    f.write(binary_data)

