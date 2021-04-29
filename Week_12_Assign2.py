def main():
    print("Function 1 Output")
    read_1()
    print("Function 2 Output")
    read_2()

def read_1():
        Blah = open('scoobydoo.txt', 'r')
        Read_list = Blah.read()
        Blah.close()
        print(Read_list)
    


def read_2():
        Blah = open ('scoobydoo.txt','r')
        line1 = Blah.readline()
        line1 = line1.rstrip('\n')
        line2 = Blah.readline()
        line2 = line2.rstrip('\n')
        line3 = Blah.readline()
        line3 = line3.rstrip('\n')
        
        Blah.close()
        print(line1)
        print(line2)
        print(line3)
    
main()

