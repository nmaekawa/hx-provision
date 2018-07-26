# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # vagrant dns; requires `vagrant plugin install landrush`
  config.landrush.enabled = true
  config.landrush.tld = "vm"

  # loris image server node
  config.vm.define "images" do |images|
    images.vm.box = "bento/ubuntu-16.04"
    images.vm.hostname = "images.vm"
    images.vm.network "private_network", ip: "10.8.0.10"

    images.ssh.forward_agent = true
    images.ssh.insert_key = false

    images.vm.provider "virtualbox" do |v|
        v.memory = "4096"
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

  # manifests node
  config.vm.define "manifests" do |manifests|
    manifests.vm.box = "bento/ubuntu-16.04"
    manifests.vm.hostname = "manifests.vm"
    manifests.vm.network "private_network", ip: "10.8.0.14"

    manifests.ssh.forward_agent = true
    manifests.ssh.insert_key = false

    manifests.vm.provider "virtualbox" do |v|
        v.memory = "1096"
    end
  end

  # mirador-lti node
  config.vm.define "mirador" do |mirador|
    mirador.vm.box = "bento/ubuntu-16.04"
    mirador.vm.hostname = "mirador.vm"
    mirador.vm.network "private_network", ip: "10.8.0.15"

    mirador.ssh.forward_agent = true
    mirador.ssh.insert_key = false

    mirador.vm.provider "virtualbox" do |v|
        v.memory = "1096"
    end
  end
end
