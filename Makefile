DOCKER_RUN = docker run --rm -it -l stdout --log-opt mode=non-blocking -v ${PWD}:/app --env PYTHONUNBUFFERED=0 --env-file .env.development -w /app --network=host python:3.8-alpine sh -c
DOCKER_RUN_ATTACHED = docker run --rm -it -v ${PWD}:/app --env PYTHONUNBUFFERED=0 --env-file src/Config/.env.development -w /app --network=host python:3.8-alpine sh
REQUIREMENTS = pip install --upgrade pip -r requirements.txt

run:
	${DOCKER_RUN} '${REQUIREMENTS} && python3 -m src.main'

run-attached:
	${DOCKER_RUN_ATTACHED}

install-package:
	${DOCKER_RUN} 'pip install ${PACK}'