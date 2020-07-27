# append to file
filename = 'result'
with open( dir + filename + ".txt", "a") as text_file:
     text_file.write("{:d}\t{:02X}\n".format(int_num, hex_num) )
# or 
fo = open('filename' + '.txt', 'a')
fo.write('%s\t%s\t%s\t%s\t' % (p[0],p[1],p[2],p[3]))
fo.write('%s\t%s\t%s\t%s\t' % (p[4],p[5],p[6],p[7]))
fo.write('%.2f\t' % (power))
fo.close()

# read line
import csv
import numpy as np
power1 = np.loadtxt("results/run1-power.csv", delimiter=",", skiprows=5)


# plots
import matplotlib.pyplot as plt 
for j in range( range(np.shape(some_set)[0]) ):
    y_vals = [all_data[i][j] for i in range(np.shape(x_vals)[0]) ] 
    plt.plot(x_vals, y_vals,'o-')
    plt.xlabel("Xxxxxxxxxxxx")
    plt.ylabel("Yyyyyyyyyyyy")
    plt.title("Tttttt %d" % some_set[j])
    plt.show()

# beep
import winsound
duration = 500  # milliseconds
freq = 440  # Hz
winsound.Beep(freq, duration)

# os commands
import os
os.chdir('/home/user/workspace/')
directory = mydirectory + '_1'
try:
    os.mkdir(directory)
except OSError:
    print ('Error: Creating directory. ' +  directory)
os.chdir(directory)
os.system('make run')

Slice = os.popen('cat results/area.txt |grep \'d S\' |tr -d \',\'|grep -o -E \'[0-9]+\' |head -1 |tr -d \'\\n\'').read()
Ram36 = os.popen('cat results/area.txt |grep \'6E1/\' |grep -o -E \'[0-9]+\' |head -5|tail -1 |tr -d \'\\n\'').read()
Ram18 = os.popen('cat results/area.txt |grep \'8E1/\' |grep -o -E \'[0-9]+\' |head -5|tail -1 |tr -d \'\\n\'').read()
Dsp48 = os.popen('cat results/area.txt |grep \'SP\' |grep -o -E \'[0-9]+\' |head -3|tail -1 |tr -d \'\\n\'').read()
os.system('cat results/performance.txt | grep Average| grep -o -E \'[0-9]+\' | tr \'\\n\' \'\\t\'>> ../result.txt' )
os.system('cat results/energy.txt | grep Average| grep -o -E \'[0-9]\.[0-9][0-9]\'>> ../result.txt' )
