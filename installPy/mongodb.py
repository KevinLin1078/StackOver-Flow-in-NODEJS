import os

arr =   [	"sudo apt-key adv --keyserver hkp://keyserver.ubuntu.com:80 --recv 0C49F3730359A14518585931BC711F9BA15703C6",
			"echo 'deb [ arch=amd64,arm64 ] http://repo.mongodb.org/apt/ubuntu xenial/mongodb-org/3.4 multiverse' | sudo tee /etc/apt/sources.list.d/mongodb-org-3.4.list",
			"sudo apt-get update", "sudo apt-get install -y mongodb-org","sudo ufw enable",
			"sudo systemctl enable mongod","sudo systemctl start mongod", "sudo systemctl status mongod"
			"sudo ufw allow from 130.245.170.247/32 to any port 27017", 
			"sudo ufw status"
		]

for i in arr:
	os.system(i);
