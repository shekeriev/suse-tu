# Introduction to containers

## Introduction to containers with Docker
 - slides - why containers; containers vs virtual machines; types of containers; Docker; workflow; Dockerfile
 - demo - install Docker; basic post-config; run a few containers; create image; run a multi-container application
 
### Create virtual machine from template (VirtualBox)

First, we must create the virtual machine using one of the provided templates:
1) Start **VirtualBox**
2) Go to **File** > **Import Appliance**
3) Click the **Browse** button and navigate to the downloaded template
4) Select it and confirm with **Open**
5) Click **Next**
6) Change the name to **opensuse-docker**
7) Adjust the rest of the parameters as you like
8) Click **Import** to start the process

After a few moments our new virtual machine will appear in the list. 

### Prepare network connectivity (VirtualBox)

By default, our new virtual machine, is connected in NAT mode. This is fine for this first part, and yet we have to make a few adjustments.

Should we want to communicate with the virtual machine from our host, which is exactly what we want, we must set a few port-forwarding rules.

Let's create two - one for the SSH communication and one for accessing WEB services on the virtual machine. Execute the following actions:

1) With **VirtualBox** started, select the virtual machine
2) Navigate to **Machine** > **Settings**
3) Switch from **General** to **Network** view
4) While in **Adapter 1** settings, click the **Advanced** option
5) Then click the **Port Forwarding** button
6) To add a rule, click on the little green button in the top right corner of the window
7) Change rule's attributes to 
   - Name -> ***SSH***
   - Protocol -> ***TCP***
   - Host Port -> ***2222***
   - Guest Port -> ***22***
8) Add one more rule and change its attributes to 
   - Name -> ***WEB***
   - Protocol -> ***TCP***
   - Host Port -> ***8080***
   - Guest Port -> ***8080***
9) Click **OK** to close the **Port Forwarding Rules** window and then once again **OK** to close virtual machine' settings window

### Start the virtual machine and establish a connection

We are ready to begin our journey. With **VirtualBox** started, select the virtual machine and go to **Machine** > **Start** > **Normal Start**.

Now, after the machine is ready, we can work on its **console** (the window that appeared) or open a **SSH session** to it. The first option doesn't require any additional software but has its limitations. The main one being that we cannot use copy-paste between the host and the virtual machine. So, we will go with the second approach. But first, we must make sure that we have a **SSH client** installed. With modern versions of **Windows 10** we have **OpenSSH** installed by default. This applies to **macOS** and all **Linux** distributions as well. If we have an older version of **Windows** or we just want to try something else, we can install the **PuTTY** client (https://www.putty.org/) which happens to be one of the most popular options.

#### Command line SSH client

Open a terminal session on your host machine. On Windows this could be either PowerShell or Command Prompt window. On macOS and various Linux distributions it may come under different name like **Terminal**, **Konsole**, etc.

Once, on the terminal, enter:

`ssh -p 2222 user@localhost`

On your first session to this machine, you may be asked to confirm the connection. Do it by entering ***yes***. Then enter ***linux*** as password (keep in mind that no characters will be displayed while you type) and hit **Enter**. 

Now, you should see a prompt like this one:

`user@opensuse:~>`

#### PuTTY

If you go with the **PuTTY** or another similar client, then your way of entering the connection details will be like the shown on this picture:
![](images/putty-screen-1.png)

Once you enter the credentials and establish a connection, everything else will behave the same no matter which client you use.

### Install Docker

Installing **Docker** on **openSUSE Leap** is a simple task. It is enough to execute the following command:

`sudo zypper install docker`

Enter the password for the **root** user (which in our case is also set to **linux**) and press **Enter**. A few other packages will be installed as well. Confirm by typing ***y*** and hit **Enter**.

That is almost all, we have it installed. However, there are a few other task which we have to deal with.

Set the **Docker** service to start automatically on boot:

`sudo systemctl enable docker`

And then start it:

`sudo systemctl start docker`

We can check if the service started:

`systemctl status docker`

And if it showed **active (running)**, we may test that we can interact with it by asking for its version:

`sudo docker version`

We should see both the version of the client utility and the service (or daemon).

Next, we must add our user to the **docker** group. For this, we will execute:

`sudo usermod -aG docker user`

Now, in order some of the changes to take effect, we must close our session by executing the following command:

`exit`

Open a new session and once in, try to execute the following command (this time without **sudo** in front of it):

`docker version`

In addition, we may ask for even more details with:

`docker info`

Both should work. Now, we are all set up and can start our journey with **Docker**.

### Start our first container

Let's check if we have any container images already:

`docker image ls`

Now, we do not have any. This is a brand new installation, after all. 

Start one to see that everything works as promised:

`docker container run hello-world`

It works! From the output, we can see that it did not find the image locally, then downloaded it, and finally, started the container. While this is not something extraordinary, it proves that our setup works as expected.

Now, let's list the container images again:

`docker image ls`

Aha, now we have one. It was used to start our first container. Can we use it to start another one? Yes, we can. So, let's do it:

`docker container run hello-world`

This time the execution took less time. The main reason behind this is that we have the image locally and there is no need to spend time downloading it again.

Let's check what containers we have. We started two so far, so we expect to see them. Execute this:

`docker container ls`

Hm, none. Strange. In fact, it is by design. We started two containers but both executed, showed something, and then exited. So, we do not have any running containers (which is what this command shows). And is there any way to see those that exited? Yes, execute the following modified version of the command:

`docker container ls -a`

Here, we can see them. We can see some details about them like ID, image, name, etc.

Let's delete them. First, we will use an ID:

`docker container rm <container-id>`

And then we will use a name:

`docker container rm <container-name>`

Now, if we ask again for the list of all containers (running and stopped):

`docker container ls -a`

We won't see anything. And our container image? Is it still there? Let's check

`docker image ls`

Yes, it is there. Can we delete it? Of course. Execute:

`docker image rm hello-world`

And if we check again:

`docker image ls`

We won't see anything. All are gone. With images, just like with containers, we can use the ID as well. Remember, that we can delete only images, that are not referred by any container - either running or stopped.

### Start a container in interactive mode

Now, let's start a container and interact with it:

`docker container run -it ubuntu bash` 

After a while we will be presented with a different prompt. We are inside the container. Let's execute a few commands:

`ps ax`

`uname -a`

`cat /etc/os-release`

`ls -l /`

`echo 'Hello Container! :)' > /hello.txt`

`cat /hello.txt`

In this particular case, all worked as expected. It is not always like this. It depends on what the author of the image decided to include.

Okay, but how can we return to our initial session? There two ways - to terminate the **bash** session in the container by executing **exit** or just close the session without terminating it by pressing **Ctrl+P** and then **Ctrl+Q**. 

Let's try the first way. Execute:

`exit`

And check if our container is still running:

`docker container ls -a`

No, it exited. We caused this by terminating the only process that was running inside the container. This is by design.

Now, start a new one:

`docker container run -it ubuntu bash`

Once, inside the container, press **Ctrl+P** and then **Ctrl+Q** to close just the session. Now, check the state of the containers with:

`docker container ls -a`

This time, we have one running and one stopped. We can stop the running one from here, just execute:

`docker container stop <container-name-or-id>`

Please note, that when we use the ID, instead of typing all its symbols, we can use just the first few that identify it amongst the others.

### Start a container in detached mode

Starting a container in interactive mode while not that rare, is not the typical way of using containers. We usually work in interactive mode, when we want to troubleshoot strange behavior or try something.

The most common way of running containers is in background or detached mode. For example, we can run a web server in a container or some other process that does its work in the background.

Let's start one container that doesn't do anything but to sleep for 1 day. We can do it with this command:

`docker container run -d --name sleeper alpine sleep 1d`

It is based on Alpine Linux and just sleeps for 1 day (if we allow it). One more thing, this time, we named the container. This will make our interaction with it easier.

Let's see the list of running containers:

`docker container ls`

It is there. Okay but what if we want to do something inside such a container? We can start a process inside it and attach to it. Usually this process is a shell. Which one, depends on the container. In this particular case, we can execute this:

`docker container exec -it sleeper sh`

Once in, execute the following commands:

`ps ax`

`cat /etc/os-release`

There is not just the process with ID 1 (which in our case is the sleep command) but also the **sh** process. Now, close the session by executing this:

`exit`

And check the list of running containers:

`docker container ls`

Aha, it is not gone. The reason for this is that we terminated the **sh** process but it wasn't the only one there. The **sleep** process "keeps" the container in running state.

We can stop this one now by executing:

`docker container stop sleeper`

### Start a container and publish a port

Now, let's run a web server based container and see how we can access the web page that is inside it. Start the container with the following command:

`docker container run -d --name web -p 8080:80 nginx`

This will start a named container in detached mode. We went over this, so we know it. The new part here (**-p 8080:80**) does the real magic. It will **publish** (**forward**) port **80** of the container to port **8080** on the virtual machine where **Docker** is running. There is a long version of the option as well - **--publish**.

But our machine does not have desktop environment. How can we access this page? We can use a command. Execute the following:

`curl http://localhost:8080`

Yes. We can "see" the default web page of the **NGINX** web server that is running inside the container. 

Can we see it better? Yes, we can. Remember that in the beginning, while we were setting our virtual machine, we created two port forwarding rules? Now, we will utilize the second one. Open a browser on your host machine and navigate to http://localhost:8080. Now, this is another story. 

So, in summary, we have this chain of port forwarding:

`Container (80) -> Virtual Machine (8080) -> Physical Machine (8080)`

Now, stop and remove the container with:

`docker container rm --force web`

The **--force** flag is required as the container is still running.

### Exchange data with container

Can we change the default web page? Yes, we can. Let's first prepare something. 

Create a folder in the home folder of the current user:

`mkdir ~/web`

Then create a simple **index.html** file inside the folder with the following command:

`echo 'Hello Container World! :)' > ~/web/index.html`

Now we have all that we need. Let's start another container, but this time using an extended command:

`docker container run -d --name web -v ~/web:/usr/share/nginx/html -p 8080:80 nginx`

The new bit there is the **-v** flag (its long version is **--volume**) with which we attached our local folder **~/web** as the **/usr/share/nginx/html** folder in the container. This mage all our local files in the source folder available in the container. Further details on how to work with this image can be found here: https://hub.docker.com/_/nginx

We can test it both on the command line in the virtual machine and in a browser tab on the host. It will work either way.

Once done exploring, stop and remove the container with:

`docker container rm --force web`

### Create and publish own container image

Let's go even further and create our own simple container image. It will be based on this image **php:apache** (https://hub.docker.com/_/php). 

Create a new folder, in the home folder of our user on the virtual machine, to accommodate all necessary files and change to it:

`mkdir ~/docker-image`

`cd ~/docker-image`

Now, create one more folder:

`mkdir web`

And then create a simple **index.php** file with the following content:

```php
<?php
  print "<h2>Hello Container World!</h2>\n";
  print "<hr />\n";
  print "<small><i>Running on <b>".gethostname()."</b></i></small>\n"; 
?>
```

You can use for example the **nano** text editor. Start it with:

`nano web/index.php`

And paste the above text there. Then press **Ctrl+O** to save the file and confirm with **Enter**. Once done, press **Ctrl+X** to close the file.

Before we continue, we should test our **PHP** code. Let's start a container and inject it there:

`docker container run -d --name web -v ~/docker-image/web:/var/www/html  -p 8080:80 php:apache`

Test the result either on the command line or in a browser. It should work and besides the greeting, should show the name of the container in which it is working. 

Stop and remove the container:

`docker container rm --force web`

Now that we are sure in our code, we must create one more file. This is the **Dockerfile** file which will contain the instructions for the creation of our container image.

Start the 

### Run a multi container application (*)

 
## Getting to know Kubernetes with k3s

 - slides - why orchestration; what is Kubernetes; Kubernetes components; Kubernetes distributions; SUSE Rancher products; k3s; basic objects/resources
 - demo - spin a single k3s instance; introduction to some of the basic resources - namespace, pod, service, replicaset, deployment; labels and selectors

## Kubernetes cluster with k3s
 - slides 
 - demo - spin a small k3s based cluster; run an application; scale it up and down; stop a node; start the node back

## Homework
 - create image (base it on an image that offers both PHP and Apache)
 - publish it to registry (create an account in Docker Hub)
 - install a k3s single node cluster (follow the same procedure as the one in the demonstration)
 - create a deployment with 3 replicas and a service (they may be two separate files or one)
 - deploy the application ()
 - upload the files to the git repo