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
