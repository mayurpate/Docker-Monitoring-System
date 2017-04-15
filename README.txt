---------------------Installation Instructions-------------
Operating System Required: Ubuntu 16.04

1. Install Docker. Execute following instruction
sudo apt-get update
sudo apt-get install apt-transport-https ca-certificates
sudo apt-key adv \
               --keyserver hkp://ha.pool.sks-keyservers.net:80 \
               --recv-keys 58118E89F3A912897C070ADBF76221572C52609D

echo "deb https://apt.dockerproject.org/repo ubuntu-xenial main" | sudo tee /etc/apt/sources.list.d/docker.list

sudo apt-get update
apt-cache policy docker-engine

sudo apt-get install docker-engine
sudo service docker start

sudo docker run hello-world

-----This command downloads a test image and runs it in a container. When the container runs, it prints an informational message and exits.

2. sudo docker run --volume=/:/rootfs:ro --volume=/var/run:/var/run:rw --volume=/sys:/sys:ro --volume=/var/lib/docker/:/var/lib/docker:ro --publish=8080:8080 --detach=true --name=cadvisor6 google/cadvisor:latest


3. sudo docker run -it ubuntu bash
- After this a root promt will open: exucute following command
fulload() { dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null | dd if=/dev/zero of=/dev/null & }; fulload; read; killall dd

Leave this prompt as it is and open new terminal

4. Download mongodb tar from email with name mongodb.tar. File will be downloaded in default downloads folder.
cd ~/Downloads/dockcode
tar -xvzf mongodb.tar	 
mv mongodb-linux-x86_64-2.4.9 mongodb
sudo mkdir /data
sudo mkdir /data/db
sudo ./mongodb/bin/mongod --logpath /var/mongo.log --fork
cd ~

5. Execute Following Command: python -V
		If it says python 2.7.X 
			then we are fine 
		otherwise 
			execute following commands one by one:
			sudo add-apt-repository ppa:fkrull/deadsnakes-python2.7
			sudo apt-get update
			sudo apt-get install python2.7
6. Execute : pip -h
		If it displays help
			then we are fine
		otherwise
			sudo apt-get install python-pip

7. Download source code from email with name sourcecode.tar.gz. This will be downloaded in default downloads folder.
cd ~/Downloads/dockcode
tar -xvzf sourcecode.tar.gz
cd sourcecode

8. sudo cp monitoring_client.py /opt

9. crontab -e
append this line to file
*/1 * * * * /opt/monitoring_client.py
save this file

10. sudo pip install -r requirements.txt
	 			
11. Execute following commands 
cd docker_monitoring/
paster serve development.ini --daemon

Above step will run the application server. 

Please wait for 10 mins to generate the stats for local docker instance. 


12. Open the browser and type 127.0.0.1:5000.  

UI will ask for IP address: Please enter i/p as 127.0.0.1 to get the correct output.

Click on blue links in containers section to see CPU and memory graphs. 


