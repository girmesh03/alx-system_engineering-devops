# creating a custom HTTP header response using Puppet.

exec {'update':
  command => '/usr/bin/apt-get update',
}

package { 'nginx':
  ensure  => present,
}

file_line { 'header':
    path  => '/etc/nginx/nginx.conf',
    match => '^http {',
    line  => "http {\n\tadd_header X-Served-By \"${hostname}\";",
}

exec { 'nginx_restart':
  command => '/usr/sbin/service nginx restart',
}
