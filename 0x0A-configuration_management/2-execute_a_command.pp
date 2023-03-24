# Excecute commands

exec { 'killmenow':
  command => '/usr/bin/pkill killmenow',
}