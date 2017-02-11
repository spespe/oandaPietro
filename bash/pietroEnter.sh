#!/bin/bash

key="no value yet"
while true; do
 clear
 echo "Bash Extra Keys Demo. Keys to try:"
 echo
 echo "* Insert, Delete, Home, End, Page_Up and Page_Down"
 echo "* The four arrow keys"
 echo "* Tab, enter, escape, and space key"
 echo "* The letter and number keys, etc."
 echo
 echo " d = show date/time"
 echo " q = quit"
 echo "================================"
 echo

 if [ "$key" = $'\x1b\x4f\x48' ]; then
 key=$'\x1b\x5b\x31\x7e'
 fi

 if [ "$key" = $'\x1b\x4f\x46' ]; then
 key=$'\x1b\x5b\x34\x7e'
 fi
 case "$key" in
 $'\x1b\x5b\x32\x7e') 
 echo Insert Key
 ;;
 $'\x1b\x5b\x33\x7e') 
 echo Delete Key
 ;;
 $'\x1b\x5b\x31\x7e') 
 echo Home Key
 ;;
 $'\x1b\x5b\x34\x7e') 
 echo End Key
 ;;
 $'\x1b\x5b\x35\x7e') 
 echo Page_Up
 ;;
 $'\x1b\x5b\x36\x7e') 
 echo Page_Down
 ;;
 $'\x1b\x5b\x41') 
 echo Up arrow
 ;;
 $'\x1b\x5b\x42') 
 echo Down arrow
 ;;
 $'\x1b\x5b\x43') 
 echo Right arrow
 ;;
 $'\x1b\x5b\x44') 
 echo Left arrow
 ;;
 $'\x09') 
 echo Tab Key
 ;;
 $'\x0a') 
 echo Enter Key
 ;;
 $'\x1b') 
 echo Escape Key
 ;;
 $'\x20') 
 echo Space Key
 ;;
 d)
 date
 ;;
 q)
 echo Time to quit...
 echo
 exit 0
 ;;
 *)
 echo You pressed: \'"$key"\'
 ;;
 esac
 echo
 echo "================================"
 unset K1 K2 K3
 read -s -N1 -p "Press a key: "
 K1="$REPLY"
 read -s -N2 -t 0.001
 K2="$REPLY"
 read -s -N1 -t 0.001
 K3="$REPLY"
 key="$K1$K2$K3"
done
exit $?
