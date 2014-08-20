import numpy as np
import matplotlib.pyplot as plot
import sys
from ParseZoneData import *

# Reference
# - http://matplotlib.org/examples/pylab_examples/bar_stacked.html


class VisualizeData:
    def __init__(self, n, type_data, x_indices):
        self.data_size = n  # number of indexes
        self.activity_data = type_data  # key-type, value - list of hours spent in sorted order of date.
        self.x_indices = x_indices  # List of dates
        self.width = 0.35
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

    def validate_data(self):
        if len(self.x_indices) != self.data_size:
            print "ERROR: " + "No of x indices not equal to data size. Exiting"
            sys.exit(1)

    def plot_stacked_bar_graph(self):
        self.validate_data()

        bars = []

        i = 0
        for activity_type in self.activity_data.keys():
            bars.append(plot.bar(np.arange(len(self.x_indices)), self.activity_data[activity_type], width=self.width, color=self.colors[i]))
            i += 1
            print self.colors[i]

        # plot.xticks(self.x_indices+self.width/.2, self.x_indices)
        # plot.xticks(self.x_indices+self.width/.2, range(len(self.x_indices)))

        plot.yticks(np.arange(0, 10, 1))
        # plot.show()
        plot.savefig('out.png')




def main():
    if len(sys.argv) > 1:
        filename = sys.argv[1]
    else:
        print 'Enter filename: '
        filename = sys.stdin.readline().rstrip()

    parse_zone_data = ParseZoneData(filename)
    parse_zone_data.parse_file()
    parse_zone_data.print_parsed_data()
    parse_zone_data.generate_visual_data()

    visualize_data = VisualizeData(n=len(parse_zone_data.visualize_data_dates),
                                   type_data=parse_zone_data.visualize_data_typewise_hours,
                                   x_indices=parse_zone_data.visualize_data_dates)
    visualize_data.plot_stacked_bar_graph()

    return

if __name__ == '__main__':
    main()