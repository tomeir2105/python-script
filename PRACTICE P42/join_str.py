# create variable for wifi/eth/network that you are connected to, and put in it that name.
ssid_name = "netgear_fa34"

# create variable for your laptops hostname and save the name in it.
laptop_hostname = "godzila"

# concatenate the variable above with new variable named my_con, print() the variable
my_con = ""
my_con = my_con + "_" + ssid_name + "_" + laptop_hostname
print(my_con)

# add id (or any number) of your connection to my_con variable and re-print it.
my_id=31512246
my_con2 = f"{my_con}{my_id}"
my_con = my_con+"_"+str(my_id)
print(my_con)
