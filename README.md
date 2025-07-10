# flaskshell
A Flask-based backdoor providing remote command execution. For use on authorized systems only, designed for red v blue cybersecurity competitions. 
 <br> <br> backdoor.py - The backdoor server running on the target host, awaiting commands to be sent
 <br>commander.py - Client for sending commands to execute 

 <br> There is also the /run/<command> endpoint, which will run the <command> short command as long as it does not have spaces in it, useful for 
 short commands like ipconfig, whoami, id 
