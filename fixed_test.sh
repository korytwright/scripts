#!bin/bash

if [[ -f ips.txt ]]; then
      rm ips.txt
      echo "this file already existed, a new one was made in its place"
fi

ping -c 4 google.com > ips.txt

#get 4th field from all lines
#copy file in order to extract just the IP
awk '{print $4}' ips.txt > copy.txt

awk 'NR==2 {print;exit}' copy.txt > copy1.txt

cat copy1.txt | cut -d ":" -f 1 > ready.txt

if [[ -f ready.txt ]]; then
      VAR1=(cat readt.txt)
fi
