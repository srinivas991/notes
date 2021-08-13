### DOCKER SECURITY

Containerization technology - plug and play

#### DOCKER ARCH

docker client => docker build, pull, run etc

these commands will go to the `docker daemon` for processing, so basically this is an API request from the client to the docker daemon, and the connection is made through a TCP socket if its remote and a domain socket if its local

so this docker daemon then forwards that request to containerd (containerd is not very user / api friendly, so daemon is used for this), now, containerd is going to use the runtime, typically `runc`, which is going to start the actual containers

docker daemon and container communicate using gRPC (remote procedure call)

runc is going to use kernel primitives called `cgroups and namespaces` => used to set resource limits on containers, and ns are used for isolation

#### Things to secure

Docker host
Docker daemon
Containers - Hardening
Authentication and communication b/w the docker components
Registry Security and best practices

Docker CIS benchmark, vulnerabilities and CVE stuff

#### TOOLS

docker-bench-security, InSpec

** from a platform perspective, docker is pretty secure, most of the issues come with the misconfigurations

