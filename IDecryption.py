try:
    path = input("Enter absolute path of Image : ")
    key = int(input("Enter Key for decryption of Image : "))
    
    print("The path of file : ", path)
    print("Note : Encryption key and Decryption key must be same.")
    print("Key for Decryption : ", key)
    
    file = open(path, 'rb')
    
    image = file.read()
    file.close()
    
    image = bytearray(image)  
    for index, values in enumerate(image):
        image[index] = values ^ key
    
    file = open(path, 'wb')
    
    file.write(image)
    file.close()
    print("Decryption Done.")

except Exception:
    print("Error caught : ", Exception.__name__)