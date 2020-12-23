VENVN_NAME?=env
VENV_ACTIVATE=. $(VENVN_NAME)/bin/activate
PYTHON=${VENVN_NAME}/bin/python3

local:
	${PYTHON} build.py

local-server:
	${PYTHON} -m http.server -d ./out/

clean:
	rm -rf out/*

prod-clean:
	rm -rf out-prod/*

prod:
	${PYTHON} build.py -fp

upload: prod
	    rsync --checksum --delete -av out-prod/ csit:~/public_html/sj

.PHONY: local clean prod-clean prod upload
