#Add a custom HTTP header with Puppet

exec { 'apt-update':
  command => '/usr/bin/apt update',
}

package { 'nginx':
    ensure  => present,
    require => Exec['apt-update'],
}

file_line {'Adding_Header':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'listen 80 default_server;',
    line    => 'add_header X-Served-By $hostname;',
    require => Package['nginx'],
}

service { 'nginx':
    ensure  => running,
    require => Package['nginx'],
}
