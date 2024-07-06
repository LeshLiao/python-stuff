try:
    # Open a file in write-mode
    f = open("myfile.txt", 'w')
    f.write("Hello World!")
except IOError as e:
    print("An error occurred:", e)
finally:
    print("Closing the file now")
    f.close()