from calculator import negative_binary_calculator
decimal_num = int(input("Enter a number: "))
space = int(input("How much space does this number take? "))
dev = 2 ** (space-1)
binary = ""  


while dev >= 1:
    if decimal_num >= dev:
        binary += "1"
        decimal_num -= dev
    else:
        binary += "0"
    dev /= 2  


while len(binary) < space:
    binary = "0" + binary


negative_binary_calculator(binary)

        
    

        


    
