echo  -e "Enter Number : \c"

read n

ans-$( ( n%2 ) )

if [ $ans -eq 0 ]

then

echo "Sn is even number." 
exit 0

fi

echo "$n is odd number"
