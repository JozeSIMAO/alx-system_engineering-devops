#!/usr/bin/env bash
#+ Just as in task #0, we’d like you to automate the task of creating a custom HTTP header
#+ response, but with Puppet.
#+ The name of the custom HTTP header must be X-Served-By
#+ The value of the custom HTTP header must be the hostname of the
#+ server Nginx is running on
#+ Write 2-puppet_custom_http_response_header.pp so that it configures a
#+ brand new Ubuntu machine to the requirements asked in this task

# Install Nginx
class { 'nginx':
  manage_repo => true,
}

# Define a custom HTTP header
nginx::resource::location { 'custom_header':
  location      => '~ ^/',
  server        => 'default',
  set_raw       => ['add_header X-Served-By $hostname;'],
  ssl           => false, # Set to true if you want to configure for HTTPS
}

# Restart Nginx to apply changes
service { 'nginx':
  ensure  => 'running',
  enable  => true,
  require => Class['nginx'],
}