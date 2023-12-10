### Load Balancer Configuration Project

This project aims to improve the web stack infrastructure by adding redundancy to the web servers and installing a load balancer. The goal is to enhance reliability, handle more traffic, and understand how a load balancer works.

#### Project Structure

- **0x0F-load_balancer**
  - **0-custom_http_response_header**: Bash script to configure Nginx with a custom HTTP response header.
  - **1-install_load_balancer**: Bash script to install and configure HAproxy on the load balancer server.

#### Task 0: Double the number of webservers

In this task, the script `0-custom_http_response_header` configures Nginx on web-02 to be identical to web-01. It adds a custom HTTP response header (`X-Served-By`) to track which web server is handling requests.

##### Usage:
```bash
./0-custom_http_response_header
