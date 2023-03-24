# Creates file school in /tmp
node default {
  # Create file
  file{ '/tmp/school':
    ensure  =>'present',
    owner   =>'www-data',
    group   =>'www-data',
    mode    =>'0744',
    content =>'I love Puppet'
  }
}

# node 'stapp01.stratos.xfusioncorp.com' {
#  include file_creator
# }