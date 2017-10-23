# Domio Challenge

Thank you for letting my do this challenge!
I have included a few of the config files needed for this project as well as some links and useful endpoints.

## Endpoints and Logs

Here is the location of the load balancer that handles running the application

DomioApplicationBalancer-2109317508.us-west-2.elb.amazonaws.com

That link is currently running 2 instances of the application. Celery is running locally on those applications and redis is running on a separate server. Celery never seemed to work :/. I was going to debug why celery was not calling the application function but I ran out of time.

Here are some credentials to get access to the Dashboard for the kittens on AWS

https://megassessment.signin.aws.amazon.com/console 
User: Domio 
Password: 7'|lCSKwi62K 

Here is an endpoint to kill a server. Hit it twice in succession to kill both servers. There will be a minute or two of downtime in this case before the new servers boot up.

https://xaf6zeh5ai.execute-api.us-west-2.amazonaws.com/kill

## Secrets

Normally if I wanted to lock down part of an application I would do it by IP address. I was going to set up a VPN and give you credentials for that to access the secrets path, but again I ran out of time :/. So if you do hit it now, you will be redirected to a forbidden page unless you are at ip address happens to be 123.123.123.123. 

## Docker

To pull the docker container I am using to run the application you can run this command
```bash
docker pull samlightsey/domiochallange
```

To run the server
```bash
docker run -d -p 80:80 samlightsey/domiochallange /root/startup.sh
```
That command will start the server, but the application will fail as it won't be able to connect to redis being outside my VPC.

To run the docker container and have look around
```bash
docker run -it -p 80:80 samlightsey/domiochallange bash
```


## Final Notes
There are many improvements that I would have liked to have done including configuration management, getting celery debugged, version control, architecture as code,  etc. 

Please let me know if you have any questions or feedback.
Thanks!

