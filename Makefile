SHELL = /bin/bash
VENVN_NAME?=env
VENV_ACTIVATE=. $(VENVN_NAME)/bin/activate
PYTHON=${VENVN_NAME}/bin/python3

local:
	${PYTHON} build.py

local-force:
	${PYTHON} build.py -f

local-server:
	${PYTHON} -m http.server -d ./out/

clean:
	rm -rf ./out
	rm -rf ./pdfs

prod-clean:
	rm -rf ./out-prod
	rm -rf ./pdfs

prod:
	${PYTHON} build.py -p

prod-force:
	${PYTHON} build.py -fp

upload: prod
	./lftp_upload.sh	

upload-force: prod-force
	./lftp_upload.sh

.PHONY: local clean prod-clean prod upload

# old stuff for "prod" uploads
# rsync --omit-dir-times --checksum --delete -av out-prod/ csit:~/public_html/s
# rsync --omit-dir-times --checksum --delete -av out-prod/ vps:/var/www/pat-earl.com/faculty-bak 