# Introduction to containers (Homework)

There are two challenges. You may tackle just the first one or both (the ideal case). The first one is mandatory. The second one is for those of you, who find the first challenge as too easy. ;)

You will find that both are really close to what we did during the demo. So, all the answers are in this document.

Of course, should you have any questions, do not hesitate to ask for guidance. You can use the Discord channel - <https://discord.gg/ztaTJG2EuM>

## Challenge 1

For this one you will need a Docker host.

You are expected to:

* create a folder **homework-3**
* create a subfolder **web** and place there a simple **index.html** file that shows at least your **faculty number** and the **group** separated with comma (for example, ***1234567890, 45***)
* create a **Dockerfile** that contains instructions for creating a container image based either on **Apache** or **NGINX** that includes the **index.html** file from the previous step
* build an image named **homework** out of the **Dockerfile**
* use the image to run a container in **detached mode**  that publishes port **80** to port **8080** on the host
* put the two commands from the previous two bullets in a text file named **readme.txt**

At the end you are expected to end up with a file hierarchy like this:

```
homework-3/
├── Dockerfile
├── readme.txt
└── web
    └── index.html
```

Create **homework-3** repository in your GitHub account and upload the files there.

## Challenge 2 (*)

Proceed with this only if you are done with the first one.

For this one you will need a single node k3s cluster.

You are expected to:

* publish the image from the first challenge to your account in Docker Hub
* create a file named **homework-pod.yaml** in the **homework3** folder that creates a pod named homework-pod based on the published image and with label **app** set to **homework**
* create a file named **homework-svc.yaml** in the **homework3** folder that creates a service named homework-svc that serves the pod (looks for the same label with the same value) and listens on a **NodePort 30080**
* deploy the two manifests in the k3s cluster

At the end you are expected to end up with a file hierarchy like this:

```
homework-3/
├── Dockerfile
├── homework-pod.yaml
├── homework-svc.yaml
├── readme.txt
└── web
    └── index.html
```

Do not forget to make sure that the two manifests are uploaded in the GitHub repository from the first challenge.
