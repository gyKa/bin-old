install:
	crontab -l | { cat; echo "0 * * * * `pwd`/remove-downloads.sh"; } | crontab -
	crontab -l | { cat; echo "0 19 * * * python `pwd`/backup.py"; } | crontab -
