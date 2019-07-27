#!/bin/bash

##############################################
#The objective of this code is to ping each IP address that is listed in a text file
#It will display the results of each ping whether or not the ping was successful
#Next, the successfully pinged IP address will be put into a separate list/text file  




# if [[ -f ips.txt ]]; then
#      rm ips.txt
#      echo "this file already existed, a new one was made in its place"
# fi


#goes through list of IP address and displays the results
for i in `cat testfile`; do ping -c 4 -t 5 $i; done


# ping -c 4 google.com > ips.txt

#get 4th field from all lines
#copy file in order to extract just the IP
#awk '{print $4}' ips.txt > copy.txt

#awk 'NR==2 {print;exit}' copy.txt > copy1.txt

#cat copy1.txt | cut -d ":" -f 1 > ready.txt

#if [[ -f ready.txt ]]; then
#      VAR1=(cat readt.txt)
#fi
