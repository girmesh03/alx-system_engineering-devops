# creating a custom HTTP header response using Puppet.

exec {'update':
    command => 'apt-get update',
    path    => '/usr/bin',
}

  package { 'nginx':
      ensure => present,
  }

  file_line { 'http_header':
      path   => '/etc/nginx/nginx.conf',
      match  => 'http {',
      line   => "http {\n\tadd_header X-Served-By \"${hostname}\";",
      notify => Exec['nginx_restart'],
  }

  exec { 'nginx_restart':
      command     => '/usr/sbin/service nginx restart',
      refreshonly => true,
  }
