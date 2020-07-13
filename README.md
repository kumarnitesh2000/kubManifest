# kubManifest
in this the kubernetes deployments , secrets , configMaps and lots of kubernates objects manifests are there to immediately launch them
Continous Deployment with the help Of Argo Cd this repo have deployment Manifest ...



in normal where storage class is given not worry but start with nfs server with docker : 
                        docker run -d --net=host --privileged --name nfs-server-test katacoda/contained-nfs-server:centos7  /exports/data-0001 /exports/data-0002
         -->2 directories open [/exports/data-0001 and ..] you can mount data from this to your host conatiner . 
