# -*- mode: ruby -*-
# vi: set ft=ruby :

Vagrant.configure("2") do |config|
  config.vm.box = "precise64"
  config.vm.box_url = "http://files.vagrantup.com/precise64.box"

  #config.vm.network :forwarded_port, guest: 80, host: 8080
  config.vm.network :private_network, ip: "192.168.50.1"

  config.vm.provision :ansible do |ansible|
    ansible.playbook = "ops/provision.yml"
    ansible.inventory_file = "ops/inventory.ini"
    ansible.limit = "vagrant"
  end
end
