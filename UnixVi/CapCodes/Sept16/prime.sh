echo -e "Enter Number : "

read n

for ((i=2; i<=$n/2; i++))

do

ans = $(( n%i ))

if [ $ans -eq 0 ]

then

echo "$n is not a prime number."

exit 0
fi

done

echo "$n is a prime number."

#5. Write a shell script that takes an argument & finds if it is prime or not. (Name the shell script as prime.sh)
