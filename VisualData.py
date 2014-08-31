#!/usr/bin/python
import numpy as np
import matplotlib.pyplot as plot
from ParseZoneData import *

# Reference
# - http://matplotlib.org/examples/pylab_examples/bar_stacked.html


class VisualizeData:
    def __init__(self, n, type_data, x_indices):
        self.data_size = n  # number of indexes
        self.activity_data = type_data  # key-type, value - list of hours spent in sorted order of date.
        self.x_indices = x_indices  # List of dates
        self.width = 1
        self.ind = np.arange(self.data_size)
        # Bar graphs expect a total width of "1.0" per group
        # Thus, you should make the sum of the two margins
        # plus the sum of the width for each entry equal 1.0.
        # One way of doing that is shown below. You can make
        # The margins smaller if they're still too big.
        # margin = 0.05
        # self.width = (1.-2.*margin)/self.data_size
        self.colors = ['b', 'g', 'r', 'c', 'm', 'y', 'k']

        self.files_generated = list()

    def validate_data(self):
        if len(self.x_indices) != self.data_size:
            print "ERROR: " + "No of x indices not equal to data size. Exiting"
            sys.exit(1)

    def plot_stacked_bar_graph(self):
        self.validate_data()
        plot.subplot(111)
        plot.figure(figsize=(20, 20))
        bars = []
        bottom_y_coordinate = [0]*len(self.x_indices)
        color_count = 0
        for activity_type in self.activity_data.keys():
            bars.append(plot.bar(self.ind,
                                 self.activity_data[activity_type],
                                 width=self.width,
                                 color=self.colors[color_count],
                                 bottom=bottom_y_coordinate,
                                 align='center'))

            # Increase the bottom by the height of each current type bar
            for i in range(len(self.activity_data[activity_type])):
                bottom_y_coordinate[i] += self.activity_data[activity_type][i]

            print activity_type, " = ", self.colors[color_count]
            color_count += 1

        # plot.xticks(self.ind, self.x_indices, rotation='vertical', size='small')
        plot.xticks(self.ind+self.width, self.x_indices, rotation='vertical')  # size='small')
        plot.subplots_adjust(bottom=.25)
        plot.legend((x[0] for x in bars), self.activity_data.keys())  # x[0] for each plot.bar stores the color

        plot.yticks(np.arange(0, 10, 1))
        file_name = 'out.png'
        self.files_generated.append(file_name)
        plot.savefig(file_name, dpi=100)
        plot.close()

    def plot_per_activity_bar_graph(self):
        # bars = []
        plot.subplot(111)
        plot.figure(figsize=(20, 20))
        color = 'r'
        for activity_type in self.activity_data.keys():
            bars = list()
            bars.append(plot.bar(self.ind,
                                 self.activity_data[activity_type],
                                 width=self.width,
                                 color=color))


            plot.xticks(self.ind+self.width/2., self.x_indices, rotation='vertical')
            plot.subplots_adjust(bottom=.5)
            file_name = str(activity_type)+'.png'
            plot.savefig(file_name, dpi=100)

            self.files_generated.append(file_name)
            plot.close()
            # plot.legend((x[0] for x in bars), self.activity_data.keys())  # x[0] for each plot.bar stores the color


