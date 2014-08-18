import csv
import os
import sys
import re
import datetime
# from collections import OrderedDict


class ParseZoneData:
    def __init__(self, filename):
        self.filename = filename
        self.dict = dict()  # key - date, value - Dictionary keyed by type
        # Sample - 2014-07-20 : {'break': '1.88', 'Home-planned': '3.58'}

        #validations
        if not os.path.isfile(self.filename):
            print 'Invalid filename'
            sys.exit(1)

    def parse_file(self):
        fh = open(self.filename,'rb')
        for line in csv.reader(fh, delimiter=',', skipinitialspace=True):
            # Sample - Home-Miscellaneous,2014-07-27,1.56
            try:
                activity_type = line[0]
                date = line[1]
                hours = line[2]

                if self.validate_date(date):
                    #store in dictionary
                    if date in self.dict:
                        tmp_dict = self.dict[date]
                    else:
                        tmp_dict = dict()
                    tmp_dict[activity_type] = hours
                    self.dict[date] = tmp_dict

            except Exception, e:
                print 'Exception: ' + str(e)
                sys.exit(1)

    def validate_date(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def print_parsed_data(self):
        for key in sorted(self.dict.keys()):
            print key + " : " + str(self.dict[key])


#Testing
def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print 'Enter filename: '
        filename = sys.stdin.readline().rstrip()

    parse_zone_data = ParseZoneData(filename)
    parse_zone_data.parse_file()
    parse_zone_data.print_parsed_data()

if __name__ == '__main__':
    main()



