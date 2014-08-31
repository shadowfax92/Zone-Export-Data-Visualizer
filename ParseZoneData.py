import csv
import os
import sys
import re
import datetime
# from collections import OrderedDict


class ParseZoneData:
    def __init__(self, filename):
        self.filename = filename
        self.input_data = dict()  # key - date, value - Dictionary keyed by type
        # Sample - 2014-07-20 : {'break': '1.88', 'Home-planned': '3.58'}
        self.all_types_present = []

        self.visualize_data_typewise_hours = dict()  # key-type, value - list of hours spent in sorted order of date.
        self.visualize_data_dates = list()

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
                    if date in self.input_data:
                        tmp_dict = self.input_data[date]
                    else:
                        tmp_dict = dict()
                    tmp_dict[activity_type] = hours
                    self.input_data[date] = tmp_dict

                    if activity_type not in self.all_types_present:
                        self.all_types_present.append(activity_type)

            except Exception, e:
                print 'Exception: ' + str(e)
                sys.exit(1)

    def validate_date(self, date_text):
        try:
            datetime.datetime.strptime(date_text, '%Y-%m-%d')
            return True
        except ValueError:
            return False

    def get_day_of_week(self, date_text):
        try:
            date_string = datetime.datetime.strptime(date_text, '%Y-%m-%d').strftime('%a')
        except:
            date_string = "None"
        finally:
            return date_string

    def get_simplified_date(self, date_text):
        try:
            date_string = datetime.datetime.strptime(date_text, '%Y-%m-%d').strftime('%d-%h (%a)')
        except:
            date_string = "None"
        finally:
            return date_string


    def generate_visual_data(self):
        # Generate the date list. Should store dates in sorted order
        for date in sorted(self.input_data.keys()):
            # self.visualize_data_dates.append(" (" + date + ") " + self.get_day_of_week(date))
            self.visualize_data_dates.append(self.get_simplified_date(date))

        # Generates a Dictionary with each element of a particular type storing the hours spent on that date
        for date_key in sorted(self.input_data.keys()):
            for type_key in self.all_types_present:
                if type_key not in self.visualize_data_typewise_hours:
                    self.visualize_data_typewise_hours[type_key] = list()

                if type_key not in self.input_data[date_key]:
                    self.visualize_data_typewise_hours[type_key].append(float(0))  # just append 0hrs for that day
                else:
                    self.visualize_data_typewise_hours[type_key].append(float(self.input_data[date_key][type_key]))  # else append actual hours spent

    def print_parsed_data(self):
        for key in sorted(self.input_data.keys()):
            print key + " : " + str(self.input_data[key])

        print 'Visual data'
        print self.visualize_data_dates
        print self.visualize_data_typewise_hours


#Testing
def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print 'Enter filename: '
        filename = sys.stdin.readline().rstrip()

    parse_zone_data = ParseZoneData(filename)
    parse_zone_data.parse_file()
    parse_zone_data.generate_visual_data()
    parse_zone_data.print_parsed_data()


if __name__ == '__main__':
    main()



