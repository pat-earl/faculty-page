local:
	build.py

clean:
	rm -rf out/*

prod-clean:
	rm -rf out-prod/*

prod:
	build.py -fp

upload: prod
	    rsync --checksum --delete -av out-prod/ qwe2:WWW/sj/

.PHONY: local clean prod-clean prod upload
