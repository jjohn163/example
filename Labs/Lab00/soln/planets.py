def weight_on_planets():
   pounds = float(input("What do you weigh on earth? "))
   
   print("\nOn Mars you would weigh", pounds*.38, "pounds.\n" +
         "On Jupiter you would weigh", pounds*2.34, "pounds.")
     
if __name__ == '__main__':
   weight_on_planets()