# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # vagrant dns; requires `vagrant plugin install landrush`
  config.landrush.enabled = true
  config.landrush.tld = "vm"

  # loris image server node
  config.vm.define "loris" do |loris|
    loris.vm.box = "bento/ubuntu-16.04"
    loris.vm.hostname = "loris.vm"
    loris.vm.network "private_network", ip: "10.8.0.10"

    loris.ssh.forward_agent = true
    loris.ssh.insert_key = false

    loris.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end

  # proxy node
  config.vm.define "proxy" do |proxy|
    proxy.vm.box = "bento/ubuntu-16.04"
    proxy.vm.hostname = "proxy.vm"
    proxy.vm.network "private_network", ip: "10.8.0.8"

    proxy.ssh.forward_agent = true
    proxy.ssh.insert_key = false

    proxy.vm.provider "virtualbox" do |v|
        v.memory = "1096"
    end
  end

  # ids image server node
  config.vm.define "ids" do |ids|
    ids.vm.box = "bento/ubuntu-16.04"
    ids.vm.hostname = "ids.vm"
    ids.vm.network "private_network", ip: "10.8.0.9"

    ids.ssh.forward_agent = true
    ids.ssh.insert_key = false

    ids.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end
end
