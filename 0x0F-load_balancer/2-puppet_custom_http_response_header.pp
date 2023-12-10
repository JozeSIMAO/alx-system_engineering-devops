#+ Just as in task #0, we’d like you to automate the task of creating a custom HTTP header
#+ response, but with Puppet.
#+ The name of the custom HTTP header must be X-Served-By
#+ The value of the custom HTTP header must be the hostname of the
#+ server Nginx is running on
#+ Write 2-puppet_custom_http_response_header.pp so that it configures a
#+ brand new Ubuntu machine to the requirements asked in this task

# Setup New Ubuntu server with nginx
# and add a custom HTTP header

exec { 'update system':
        command => '/usr/bin/apt-get update',
}

package { 'nginx':
	ensure => 'installed',
	require => Exec['update system']
}

file {'/var/www/html/index.html':
	content => 'Hello World!'
}

exec {'redirect_me':
	command => 'sed -i "24i\	rewrite ^/redirect_me https://th3-gr00t.tk/ permanent;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

exec {'HTTP header':
	command => 'sed -i "25i\	add_header X-Served-By \$hostname;" /etc/nginx/sites-available/default',
	provider => 'shell'
}

service {'nginx':
	ensure => running,
	require => Package['nginx']
}