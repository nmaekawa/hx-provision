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

  # iipsrv image server node
#  config.vm.define "iip" do |iip|
#    iip.vm.box = "bento/ubuntu-16.04"
#    iip.vm.hostname = "iip.vm"
#    iip.vm.network "private_network", ip: "10.8.0.6"
#
#    iip.ssh.forward_agent = true
#    iip.ssh.insert_key = false
#
#    iip.vm.provider "virtualbox" do |v|
#        v.memory = "4096"
#    end
#  end

  # loris image server node
  config.vm.define "loris" do |loris|
    loris.vm.box = "bento/ubuntu-16.04"
    loris.vm.hostname = "loris.vm"
    loris.vm.network "private_network", ip: "10.8.0.7"

    loris.ssh.forward_agent = true
    loris.ssh.insert_key = false

    loris.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end

  # loris image server node
  config.vm.define "varnish" do |varnish|
    varnish.vm.box = "bento/ubuntu-16.04"
    varnish.vm.hostname = "varnish.vm"
    varnish.vm.network "private_network", ip: "10.8.0.8"

    varnish.ssh.forward_agent = true
    varnish.ssh.insert_key = false

    varnish.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end
end
