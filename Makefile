local:
	build.py

prod:
	build.py -fp

upload: prod
	    rsync --checksum --delete -av out-prod/ qwe2:WWW/sj/

.PHONY: local prod upload
