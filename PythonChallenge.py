import csv

class PythonChallenge:
    '''
    A Constructor with just the path to CSV file
    Basically, you set up the path to the file here, and get_data + read_csv
    would use this link
    '''
    def __init__(self):
        try:
            self.path = r'C:\Users\Aliaksei\Documents\WorldViz\PythonChallenge3.txt'
            simulation_data = self.get_data()
            #print(simulation_data[2][2])
        except TypeError:
            return None
        
    '''
    Creating a method for reading a csv file and coverting it into a list of rows
    '''
    def read_csv(self, csv_file_path):
        #Using try/catch for all exceptions that pop up
            try:
                #reading the csv file
                with open (csv_file_path) as csv_file:
                    csv_reader = csv.reader(csv_file, delimiter=',')
                    if csv_reader == None:
                        return None
                    rows = []
                    for row in csv_reader:
                        rows.append(row)
                        #making sure the values in cells 2: are floats
                        for row in rows[1:]:
                            row[2] = float(row[2])
                            row[3] = float(row[3])
                            row[4] = float(row[4])
                            row[5] = float(row[5])
                            row[6] = float(row[6])
                            row[7] = float(row[7])    
                    data = list(rows)
                    csv_file.close()           
                    return data
            #ValueError would block the whole list if there will be a non-convertable value                    
            except ValueError:
                print("Warning!")
                return None
            #FileNotFound exception would block either non-existent files or empty ones
            except FileNotFoundError:
                return None

    '''
    This method returns the file we read in a form of 2D list
    '''
    def get_data(self):
        simulation_data = self.read_csv(self.path)
        #Checking for the NoneType elements
        if simulation_data != None:
            if len(simulation_data) == 0:
                return None
            else:
                return simulation_data
        else:
            return None
    '''
    This method returns a specific row we would like to select from our list
    '''
    def get_row(self, row_num):
        data = self.get_data()
        while data != None:
            for i in range(len(data)):
                if row_num == i:
                    return self.get_data()[i]
                     

        


file = PythonChallenge()
#print(file.get_data())
#print(file.get_row(1))

#print(file.get_row(4))
#file.read_csv(r'C:\Users\Aliaksei\Documents\WorldViz\PythonChallenge.txt')
#print(file.read_csv(r'C:\Users\Aliaksei\Documents\WorldViz\PythonChallenge.txt'))
#print(file.get_data())
#print(file.get_row(3))
#file.read_csv(r'C:\Users\Aliaksei\Documents\WorldViz\PythonChallenge.txt')
#print(file.get_row(4))
#file.read_csv(r'C:\Users\Aliaksei\Documents\WorldViz\PythonChallenge3.txt')
#print(file.get_row(3))
#file.read_csv(r'C:\Users\Aliaksei\Documents\WorldViz\PythonChallenge4.txt')
#file.read_csv(r'C:\Users\Aliaksei\Documents\WorldViz\PythonChallenge5.txt')








        
        


    
