read -p 'Enter username to check: ' user

if who -u | grep -q "^$user "; then

top -u "$user"

else

echo "User $user is not logged in"

fi

#7. Write a shell script to see if a particular user has logged in. (Name the shell script as user.sh)
