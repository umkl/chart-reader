# Chartreader in Python using OpenCV

## objective
Images consisting charts with the same pixel-layout but different dimensions must be converted into csv-data.

## process
Images are supplied by the input folder. These are converted by opencv into rgb-pixel-values. 

## project-structure

The project consists of 3 _helper classes_ which are used to get processable data. 
The result class makes use of all 3 of them and converts the data from the chart according to the y and x axis.

### The chart class
This class is used to read the blue pixels on the image considering an offset.

### The logAxis class
This class is used to read the y-axis and converting the data into a coordinate-log-map considering an offset.

### The dateAxis class
This class is used to read the x-axis and converting the data into a coordinate-date-map considering an offset.

## packaging
WIP

