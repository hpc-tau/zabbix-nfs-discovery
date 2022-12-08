# zabbix-nfs-discovery
template for zabbix for discovering only nfs mount and checking if they are mounted

create folder /etc/zabbix/scripts
copy nfs_discovery.py to that folder

create a file in /etc/zabbix/zabbix_agent2.d/ called userparameter_mounts.conf
inside is the call to the script:
UserParameter=vfs.fs.mfs.discovery, python3 /etc/zabbix/scripts/nfs_discovery.py


in zabbix, when you create a new discovery rule, put 'vfs.fs.mfs.discovery' under key
