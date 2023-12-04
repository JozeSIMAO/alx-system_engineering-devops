#!/usr/bin/env bash
#+ Just as in task #0, we’d like you to automate the task of creating a custom HTTP header
#+ response, but with Puppet.
#+ The name of the custom HTTP header must be X-Served-By
#+ The value of the custom HTTP header must be the hostname of the
#+ server Nginx is running on
#+ Write 2-puppet_custom_http_response_header.pp so that it configures a
#+ brand new Ubuntu machine to the requirements asked in this task

# Install Nginx
package { 'nginx':
  ensure => installed,
}

file { '/var/www/html':
  ensure => directory,
}

file { '/var/www/html/index.html':
  ensure  => present,
  content => 'Hello World!',
}

file { '/var/www/html/404.html':
  ensure  => present,
  content => "Ceci n'est pas une page",
}

file { '/etc/nginx/sites-available/default':
  ensure  => present,
  content => '
    server {
      listen 80 default_server;
      listen [::]:80 default_server;
      add_header X-Served-By $hostname;
      root /var/www/html;
      index index.html index.htm;

      location /redirect_me {
        return 301 https://youtube.com/;
      }

      error_page 404 /404.html;
      location /404 {
        root /var/www/html;
        internal;
      }
    }
  ',
}

service { 'nginx':
  ensure  => running,
  enable  => true,
  require => File['/etc/nginx/sites-available/default'],
}