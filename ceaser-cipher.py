print("""
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     'Y8 a8P_____88 I8[    "" ""     'Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  '"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 '"Ybbd8"' '"8bbdP"Y8  '"Ybbd8"' '"YbbdP"' '"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 '"Ybbd8"' 88 88'YbbdP"'  88       88  '"Ybbd8"' 88          
              88                                             
              88           
""")



def ceaser (text_org, shift_amount, encode_or_decode) :
    encrypt_text = ""

    if encode_or_decode == 'decode' :
        shift_amount *= -1
    
    for x in text_org :
        
        if x not in alphabet :

            encrypt_text += x

        else :

            shift2 = alphabet.index(x) + shift_amount
            shift2 %= len(alphabet)
            encrypt_text += alphabet[shift2]

    print(f"Here is the {encode_or_decode}d result : {encrypt_text} ")


stop = False
while not stop :

    alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    ceaser(text_org= text, shift_amount= shift, encode_or_decode= direction)
    user_ch = input("Type 'yes' if you wanna go again.Otherwise, type 'no' :\n")

    if user_ch == "no" :
        stop = True
        print("Goodbye!!!")