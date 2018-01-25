# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # vagrant dns; requires `vagrant plugin install landrush`
  config.landrush.enabled = true
  config.landrush.tld = "vm"

  # metadata server node
#  config.vm.define "meta" do |meta|
#    meta.vm.box = "geerlingguy/ubuntu1404"
#    meta.vm.hostname = "meta.vm"
#    meta.vm.network "private_network", ip: "10.8.0.5"
#
#    meta.ssh.forward_agent = true
#    meta.ssh.insert_key = false
#
#    meta.vm.provider "virtualbox" do |v|
#        v.memory = "4096"
#    end
#  end

  # image server node
  config.vm.define "image" do |image|
    image.vm.box = "bento/ubuntu-16.04"
    image.vm.hostname = "image.vm"
    image.vm.network "private_network", ip: "10.8.0.6"

    image.ssh.forward_agent = true
    image.ssh.insert_key = false

    image.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end

end
