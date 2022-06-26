ssh -i eu-vm andrei@35.222.72.120 exit

if [ $? -eq 0 ]
then
    echo 'connection successful'
    pwd
fi      
scp -i eu-vm screenshot.png andrei@35.222.72.120:~/