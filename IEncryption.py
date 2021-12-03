try:
    path = input("Enter absolute path of Image : ")
    key = int(input('Enter Key for encryption of Image : '))
    
    print("The path of file : ", path)
    print("Key for encryption : ", key)
    
    file = open(path, 'rb')
    
    image = file.read()
    file.close()
    
    image = bytearray(image)
    for index, values in enumerate(image):
        image[index] = values ^ key
    
    file = open(path, 'wb')
    
    file.write(image)
    file.close()
    print("Encryption Done.")
    
except Exception:
    print("Error caught : ", Exception.__name__)