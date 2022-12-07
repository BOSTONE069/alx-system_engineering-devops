# set limits on user.

file { '/etc/security/limits.conf':
  ensure => present,
} -> exec { 'Limit HARD':
  command => 'sed -i "s/holberton hard nofile 5/holberton hard nofile unlimited/" /etc/security/limits.conf',
  path    => '/bin',
} -> exec { 'Limit SOFT':
  command => 'sed -i "s/holberton soft nofile 4/holberton hard nofile 1000/" /etc/security/limits.conf',
  path    => '/bin',
}
