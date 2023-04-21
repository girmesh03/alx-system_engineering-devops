# Create a file with the content "I love Puppet" and
# set the owner and group to www-data.
# With permissions set to 0744.

file { '/tmp/school':
  ensure  => file,
  mode    => '0744',
  owner   => 'www-data',
  group   => 'www-data',
  content => 'I love Puppet',
}
