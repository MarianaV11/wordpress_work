# Project Setup

1. Download the images for MySQL and WordPress

```
docker-compose pull
```

2. Start the containers once the images are available

```
docker-compose up -d
```

3. Check the running containers — there should be **3 WordPress instances** and **1 Nginx**.

```
docker-compose ps
```

4. (Optional) Check if MySQL has started successfully.

```
docker-compose logs -f db
```

5. Open in your browser:

```
http://localhost/
```

Set up your WordPress account.

# To List the IPs of the WordPress Instances

```
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' wordpress1
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' wordpress2
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' wordpress3
```

# Test

Run the command below and observe the **round-robin behavior** every time you create or refresh a page in WordPress.

Note that, based on the previously listed IPs, the `X-Upstream` header will change every time you execute it — this behavior is controlled by Nginx.

```
curl -I http://localhost/
```

# Evidence of Execution

The following image shows the result of the docker-compose ps command, confirming that 3 WordPress containers, 1 MySQL, and 1 Nginx service are running as expected.

![Docker ps](./images/image_1.png)

---

This image displays the output of the docker inspect command, where we can see the individual IP addresses assigned to each WordPress container.
These IPs are used by the load balancer (Nginx) to distribute requests.

![Containers running](./images/image_2.png)

---

The image below shows the results of consecutive executions of the curl -I http://localhost/ command.
Each response includes a different X-Upstream header value, demonstrating that the load balancing mechanism is successfully rotating between WordPress instances (Round Robin strategy).

![Round Robin behavior](./images/image_3.png)
