#!/usr/bin/env bash

# The ssh client configuration

file_line{'Turn off passwd authentication':
path => '/etc/ssh/ssh_config',
line => 'PasswordAuthentication no'
}

file_line{'Define identity file':
path => '/etc/ssh/ssh_config',
line => 'IdentityFile ~/.ssh/school'
}
