import sys
import csv
"""Parses the provided csv file for different companies' share data
    and provides highest share prices"""
class Parser(object):
    def __init__(self, arg):
        super(Parser, self).__init__()
        self.file = arg
        # Basic field structure followed in csv files with company names being variable in number
        fieldnames=["Month", "Year", "Companies"]
        self.reader = csv.DictReader(fieldnames)

    def parse_file_contents(self, file_name = None):
        if file_name is not None:
            self.file = file_name
        try:
            self.reader = csv.DictReader(open(self.file))
        except Exception, e:
            print("Unable to parse the csv file")
    
    def find_highest_values(self):
        self.highest = dict()
        try:
            for company in self.reader.fieldnames[2:]:
                self.highest[company] = ['', '', -1]
            for row in self.reader:
                for item in self.highest:
                    if( int(row[item]) > self.highest[item][-1] ):
                        self.highest[item] = [row['Month'], row['Year'], int(row[item])]
        except Exception, e:
            print("received exception in file parsing: "+str(e))
            raise
        finally:
            print("file processing completed")
    
    """Provides the data as it is stored without any modifications"""
    def get_parsed_data(self):
        return self.highest
    
    """Provides the desired information as requested in the specs.
        This list contains the results once the processing is done """
    def get_processed_company_list(self):
        if self.highest is None:
            return None
        else:
            return self.highest.items()


"""This application requires the csv file to be presented as an argument."""
def main(argv = None):
  if argv is None or len(argv)<2:
    print("Usage: python parser.py data_file.csv")
  else:
    data_file = argv[-1] # The last argument is the csv file
    p = Parser(data_file)
    p.parse_file_contents()
    p.find_highest_values()
    data = p.get_parsed_data()
    for datum in data:
      print datum + ' had largest share in '+data[datum][0]+data[datum][1]
if __name__ == '__main__':
  main(sys.argv)
