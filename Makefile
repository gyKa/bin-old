install:
	crontab -l | { cat; echo "0 * * * * `pwd`/remove-downloads.sh"; } | crontab -
