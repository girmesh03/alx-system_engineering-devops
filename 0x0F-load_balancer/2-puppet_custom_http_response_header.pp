# creating a custom HTTP header response using Puppet.

class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { 'add_http_header':
    path    => '/etc/nginx/nginx.conf',
    match   => 'http {',
    content => "http {\n\tadd_header X-Frame-Options \"${hostname}\";\n",
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure  => running,
    enable  => true,
    require => Package['nginx'],
  }
}

include nginx
