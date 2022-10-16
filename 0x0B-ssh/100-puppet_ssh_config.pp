# Setting up ssh config file using puppet
file_line {'ssh_config_first_work':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => 'IdentityFile ~/.ssh/school',
  multiple => true,
}
file_line {'ssh_config_second_work':
  ensure   => present,
  path     => '/etc/ssh/ssh_config',
  line     => 'PasswordAuthentication no',
  multiple => true,
}
