1. Open your terminal and change directory to mysite folder
2. Run command "sudo docker build --tag django-app ." - this will build your docker image based on Dockerfile.
3. Start container based on docker image we have just created "sudo docker run --name test1 --publish 8000:8000 django-app"
4. Test if you can see the index site when you access http://0.0.0.0:8000/polls/ 
