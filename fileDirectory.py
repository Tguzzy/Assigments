import os 

def main():
    filePath = input("Enter the directory that you want to save the file to: ")
    fileName = input("Enter the file name: ")
    name = input("Enter your name: ")
    address = input("Enter your address: ")
    phone_number = input("Enter your phone number: ")

    #check to see if the directory exists
    if os.path.isdir(filePath):
        writeFile = open(os.path.join(filePath, fileName),'w+') #creating and opening the file to write
        writeFile.write(name+ ',' +address+ ',' +phone_number+ '\n') #writing the data seperated by a comma
        writeFile.close() #closing file after its written

        print("\nFile Contents: ")
        readFile = open(os.path.join(filePath,fileName),'r')
        for line in readFile:
            print(line)
        readFile.close()
    else:
        print("Sorry that File Directory does not exist...")

    
main()
        
        
        
