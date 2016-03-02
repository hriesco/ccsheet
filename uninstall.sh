#!/bin/bash 

if [ $UID -eq 0 ]; then
	echo "Delete alias in bashrc files..."
	sed -i '/\# Command Cheatsheet Alias \-\-\-\-/d' /root/.bashrc
	sed -i '/alias ccs\=\"python \/opt\/ccsheet\/ccs\.py/d' /root/.bashrc
	sed -i '/alias ccsl\=\"python \/opt\/ccsheet\/ccs\.py \-l/d' /root/.bashrc
	sed -i '/alias ccsgui\=\"python \/opt\/ccsheet\/ccsgui\.py/d' /root/.bashrc

	for user in `ls /home/ | grep -v "lost+found"`
	do
		sed -i '/\# Command Cheatsheet Alias \-\-\-\-/d' /home/$user/.bashrc
		sed -i '/alias ccs\=\"python \/opt\/ccsheet\/ccs\.py/d' /home/$user/.bashrc
		sed -i '/alias ccsl\=\"python \/opt\/ccsheet\/ccs\.py \-l/d' /home/$user/.bashrc
		sed -i '/alias ccsgui\=\"python \/opt\/ccsheet\/ccsgui\.py/d' /home/$user/.bashrc

		echo "Delete group ccsheet for user: $user"
		gpasswd -d $user ccsheet
	done

	echo "Delete directory /opt/ccsheet/"
	rm -rf /opt/ccsheet/
	
	echo "Delete group ccsheet..."
	groupdel ccsheet

	echo "Uninstall complete"
else
	echo "You must be logued as root"
fi
