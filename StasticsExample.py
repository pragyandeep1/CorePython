import statistics
# list of positive integer numbers
datasets = [5, 2, 7, 4, 2, 6, 8]
x = statistics.mean(datasets)
# Printing the mean
print("Mean is :", x)
print("------------")
datasetsmedian = [1, 2, 4, 7,8, 11, 13, 19]
print("Median of data-set is : % s " % (statistics.median(datasetsmedian)))
print("Mode of data-set is : % s " % (statistics.mode(datasetsmedian)))
print("stdev of data-set is : % s " % (statistics.stdev(datasetsmedian)))
print("medianlow of data-set is : % s " % (statistics.median_low(datasetsmedian)))
print("medianheigh of data-set is : % s " % (statistics.median_high(datasetsmedian)))


