import time
import netpbmfile, os
import numpy as np
from effects import object_filtering, shades_of_gray, horizontal_flip


def main():
    """main function"""
    print("Hello and welcome to image editor")
    
    selection = input(
    """
    Please enter choice of editing feature.
    [1] filter out foreign objects
    [2] grayscale ppm image
    [3] flip ppm imageimage \n
    """)
    
    if "1" in selection:
        # prompt user for 3 input files 
        try:
            file_name1 = str(input("please enter file 1: \n"))
            file_name2 = str(input("please enter file 2: \n"))
            file_name3 = str(input("please enter file 3: \n"))
            output = input("please enter output file name: \n")
            
            object_filtering(file_name1,file_name2,file_name3,output)
        except FileNotFoundError as f:
            print("file not found")
            time.sleep(1)
            return main()
        
    elif "2" in selection:
        file_name1 = str(input("Please enter file name: \n"))
        output = str(input("please enter output file name: \n"))
        try:
            shades_of_gray(file_name1,output)
        except FileNotFoundError as f:
            print("{} not found".format(file_name1))
            print()
            time.sleep(1)
            return main()
        
    elif "3" in selection:
        file_name1 = str(input("Please enter file name: \n"))
        output = str(input("Please enter output file name: \n"))
        try:
            horizontal_flip(file_name1,output)
        except FileNotFoundError as f:
            print("{} not found".format(file_name1))
            print()
            time.sleep(1)
            return main()
    else:
        print("Please enter a valid selection")
        print()
        time.sleep(1)
        return main()
    
    print(output +" was created. Thanks for using this program!")

if __name__ == "__main__":
    main()