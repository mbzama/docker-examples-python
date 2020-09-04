-------------
Run locally
-------------
	python api.py

	Access the app using
		Windows: http://192.168.99.100:5001/greet?name=zama
		Ubuntu : http://localhost:5001/greet?name=zama

-------------
Build docker image
-------------
	docker build -t docker-example-python .

-------------
Run app as Docker container
-------------
	docker run -p 5001:5001 --name docker-example-python-c docker-example-python

	Access the app using
		Windows: http://192.168.99.100:5001/greet?name=zama 
		Ubuntu : http://localhost:5001/greet?name=zama
