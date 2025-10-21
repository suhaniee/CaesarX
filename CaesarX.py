print("Welcome to CaesarX!")
choice=int(input("Type 1 to encrypt or 2 to decrypt the message : "))
msg=input("Type your message : ")
shift=int(input("Enter shift key : "))
#using modulo % to maintain shift key loop even if its value exceeds 26
shift=shift%26
start_up=ord('A')
end_up=ord('Z')
start_low=ord('a')
end_low=ord('z')

def caesarx(msg,shift):
    #initialize result as string
    result=""
    #go thru each of letters in the message
    for char in msg:
        #do something
        """using if and isalpha() method filter out alphabets 
        from signs & symbols"""

        if char.isalpha():

            """filter out upper and lower case letters as they
            have diffrent ascii code"""
            if char.isupper():

                """ convert to ascii with inbuilt python function ord()
                where ord stands for ordinal """
                ascii=ord(char)
                """ converting the string character ascii individually to encrypted
                character ascii  by using the shift key """
                en_ascii=ascii + shift

                if en_ascii>end_up:
                    en_ascii=en_ascii-26

                if en_ascii<start_up:
                    en_ascii=en_ascii+26
                """now converting the new ascii to new character by 
                using inbuilt function chr()"""
                en_char=chr(en_ascii)
                """now add character to result as string"""
                result=result+en_char
            
            else:
                ascii=ord(char)
                en_ascii=ascii + shift
                if en_ascii>end_low:
                    en_ascii=en_ascii-26

                if en_ascii<start_low:
                    en_ascii=en_ascii+26
                en_char=chr(en_ascii)
                result=result+en_char

        #else condition for symbols
        else:
            symb=char
            result=result+symb

    print(result)

if choice == 1:
    caesarx(msg,shift)

elif choice == 2:
    caesarx(msg,-shift)
    
else:
    print("Invalid input! ")
