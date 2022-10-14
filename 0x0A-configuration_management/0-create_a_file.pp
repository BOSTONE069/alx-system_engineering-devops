# Creatring a file in /tmp and

file {'school':
  ensure  => 'present',
  content => 'I love Puppet',
  group   => 'www-data',
  mode    => '0744',
  owner   => 'www-data',
  path    => '/tmp/schhol',
}
