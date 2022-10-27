Web Debbugging 2

<p align="center">
 <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/271/B4eeypV.jpg">
</p>

* **1 Nginx likes port 80**

[0-nginx_likes_port_80](0-nginx_likes_port_80)

Using your debugging skills, find out what’s keeping your Ubuntu container’s Nginx installation from listening on port 80. Feel free to install whatever tool you need, start and destroy as many containers as you need to debug the issue. Then, write a Bash script with the minimum number of commands to automate your fix.
Requirements:
Nginx must be running, and listening on port 80 of all the server’s active IPv4 IPs
Write a Bash script that configures a server to the above requirements

* **2. Make it sweet and short**

[1-debugging_made_short](1-debugging_made_short)

Using what you did for task #0, make your fix short and sweet.

Requirements:

Your Bash script must be 5 lines long or less
There must be a new line at the end of the file
You must respect usual Bash script requirements
You cannot use ;
You cannot use &&
You cannot use wget
You cannot execute your previous answer file (Do not include the name of the previous script in this one)
service (init) must say that nginx is not running ← for real