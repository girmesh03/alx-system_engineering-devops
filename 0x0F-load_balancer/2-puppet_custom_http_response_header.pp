# creating a custom HTTP header response using Puppet.

class nginx {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/conf.d/custom_header.conf':
    content => "add_header X-Served-By $::hostname;\n",
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure => running,
    enable => true,
    require => Package['nginx'],
  }
}

include nginx
