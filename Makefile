run-first:
	docker build -t python-rest .
run:
	docker run -d -p 8081:8081 --rm --name python_rest_test python-rest
run-cli:
	docker run -p 8081:8081 --rm --name python_rest_test python-rest
stop:
	docker stop python_rest_test
clear:
	docker rmi python-rest

