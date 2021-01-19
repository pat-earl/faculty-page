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
	${PYTHON} build.py -fp

upload: prod
	    rsync --omit-dir-times --checksum --delete -av out-prod/ csit:~/public_html/s

.PHONY: local clean prod-clean prod upload
