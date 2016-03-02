#!/bin/bash 

if [ $UID -eq 0 ]; then
	echo "Installing Command cheatsheet in your O.S."

	cp -r ../ccsheet /opt/
	groupadd ccsheet
	chgrp -R ccsheet /opt/ccsheet
	chmod -R 770 /opt/ccsheet

	echo '# Command Cheatsheet Alias -------------------' >> /root/.bashrc
	echo 'alias ccs="python /opt/ccsheet/ccs.py"' >> /root/.bashrc
	echo 'alias ccsl="python /opt/ccsheet/ccs.py -l"' >> /root/.bashrc
	echo 'alias ccsgui="python /opt/ccsheet/ccsgui.py"' >> /root/.bashrc
	echo '# Command Cheatsheet Alias -------------------' >> /root/.bashrc
	
	for user in `ls /home/ | grep -v "lost+found"`
	do
		next=false
		while ! $next 
		do
			read -p "Install for user: $user [y/n] " opc 
			if [ $opc = 'y' ]; then
				next=true
				gpasswd -a $user ccsheet
				echo '# Command Cheatsheet Alias -------------------' >> /home/$user/.bashrc
				echo 'alias ccs="python /opt/ccsheet/ccs.py"' >> /home/$user/.bashrc
				echo 'alias ccsl="python /opt/ccsheet/ccs.py -l"' >> /home/$user/.bashrc
				echo 'alias ccsgui="python /opt/ccsheet/ccsgui.py"' >> /home/$user/.bashrc
				echo '# Command Cheatsheet Alias -------------------' >> /home/$user/.bashrc
			elif [ $opc = 'n' ]; then
				next=true
			else
				next=false
			fi
		done
	done
	clear
	echo "Installation done..."
	echo "To make the application works you must restart the user session"
	echo "When you restart you can put the next commands to access the application"
	echo "ccs    - command cheatsheet application"
	echo "ccsl   - command cheatsheet list categories"
	echo "ccsgui - command cheatsheet gui for make new cheatsheet"
	echo "Enjoy :)"
else
	echo "You must login as root"
fi
