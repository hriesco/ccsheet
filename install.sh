#!/bin/bash 

if [ $UID -eq 0 ]; then
	echo "Installing Command cheatsheet in your O.S."
	cp -r ../ccsheet /opt/
	echo '"# Command Cheatsheet Alias -------------------"' >> ~/.bashrc
	echo 'alias ccs="python /opt/ccsheet/ccs.py"' >> ~/.bashrc
	echo 'alias ccsl="python /opt/ccsheet/ccs.py -l"' >> ~/.bashrc
	echo 'alias ccsgui="python /opt/ccsheet/ccsgui.py"' >> ~/.bashrc
	echo '"-----------------------------------------------"' >> ~/.bashrc
	
	for user in `ls /home/ | grep -v "lost+found"`
	do
		next=false
		while ! $next 
		do
			echo $next
			read -p "Install for user: $user [y/n] " opc 
			if [ $opc = 'y' ]; then
				next=true
				echo '"# Command Cheatsheet Alias -------------------"' >> /home/$(user)/.bashrc
				echo 'alias ccs="python /opt/ccsheet/ccs.py"' >> /home/$(user)/.bashrc
				echo 'alias ccsl="python /opt/ccsheet/ccs.py -l"' >> /home/$(user)/.bashrc
				echo 'alias ccsgui="python /opt/ccsheet/ccsgui.py"' >> /home/$(user)/.bashrc
				echo '"-----------------------------------------------"' >> /home/$(user)/.bashrc
			elif [ $opc = 'n' ]; then
				next=true
			else
				next=false
			fi
		done
	done
	echo "Installation done"
	echo "Now you con put in your terminal the next commands to access the application"
	echo "ccs    - command cheatsheet application"
	echo "ccsl   - command cheatsheet list categories"
	echo "ccsgui - command cheatsheet gui for make new cheatsheet"
	echo "Enjoy :)"
else
	echo "You must login as root"
fi
