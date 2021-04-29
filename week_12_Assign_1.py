# Create Main Function
def main():
    # Call the functions
    create_cast()
    add_data()

# Create a function to write data to a file 
def create_cast():
    characters=open('scoobydoo.txt','w')
    characters.write("Shaggy\n")
    characters.write("Scooby-Doo\n")
    characters.write("Daphne\n")
    characters.write("Velma\n")
    characters.close()

# Create another function to write add data to existing file
def add_data():
    characters = open('scoobydoo.txt','a')
    characters.write("Fred\n")
    characters.write("Scrappy\n")
    characters.close()

main()


