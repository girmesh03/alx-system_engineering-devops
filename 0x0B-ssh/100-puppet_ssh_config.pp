#!/usr/bin/env bash
# The ssh client configuration

file_line{'set PasswordAuthentication':
    path => '/etc/ssh/ssh_config',
    line => 'PasswordAuthentication no'
}

file_line{'set IdentityFile':
    path => '/etc/ssh/ssh_config',
    line => 'IdentityFile ~/.ssh/school'
}
