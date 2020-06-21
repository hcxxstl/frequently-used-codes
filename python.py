# append to file
with open( dir + filename + ".txt", "a") as text_file:
     text_file.write("{:d}\t{:02X}\n".format(int_num, hex_num) )

# plots
import matplotlib.pyplot as plt 
for j in range( range(np.shape(some_set)[0]) ):
    y_vals = [all_data[i][j] for i in range(np.shape(x_vals)[0]) ] 
    plt.plot(x_vals, y_vals,'o-')
    plt.xlabel("Xxxxxxxxxxxx")
    plt.ylabel("Yyyyyyyyyyyy")
    plt.title("Tttttt %d" % some_set[j])
    plt.show()
