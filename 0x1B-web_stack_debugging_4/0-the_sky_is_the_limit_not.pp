#increases the amount of traffic an Nginx server can handle

exec { 'fix-for-nginx':
  command => 'sed -i "s/15/4096/" /etc/default/nginx',
  path    => '/usr/local/bin/:/bin/'
}

exec {'restart':
  provider => shell,
  command  => 'sudo service nginx restart',
}
