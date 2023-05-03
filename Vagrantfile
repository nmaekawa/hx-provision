# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
DEFAULT_VB = "geerlingguy/ubuntu2004"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # vagrant dns; requires `vagrant plugin install vagrant-dns`
  config.dns.tld = "vm"
  VagrantDNS::Config.logger = Logger.new("dns.log")
  VagrantDNS::Config.auto_run = false

  # mirador-lti node
  config.vm.define "mirador" do |mirador|
    mirador.vm.box = DEFAULT_VB
    mirador.vm.hostname = "mirador"
    mirador.dns.patterns = [/^mirador.vm$/]
    mirador.vm.network "private_network", ip: "10.8.0.15"

    mirador.ssh.forward_agent = true
    mirador.ssh.insert_key = false

    mirador.vm.provider "virtualbox" do |v|
        v.memory = "1096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # catchpy postgres
  config.vm.define "dbserver" do |dbserver|
    dbserver.vm.box = DEFAULT_VB
    dbserver.vm.hostname = "dbserver"
    dbserver.dns.patterns = [/^dbserver.vm$/]
    dbserver.vm.network "private_network", ip: "10.8.50.31"

    dbserver.ssh.forward_agent = true
    dbserver.ssh.insert_key = false

    dbserver.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # catchpy webserver
  config.vm.define "catchpy" do |catchpy|
    catchpy.vm.box = "geerlingguy/ubuntu2004"
    catchpy.vm.hostname = "catchpy"
    catchpy.dns.patterns = [/^catchpy.vm$/]
    catchpy.vm.network "private_network", ip: "10.8.50.41"

    catchpy.ssh.forward_agent = true
    catchpy.ssh.insert_key = false

    catchpy.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # hxat  webserver
  config.vm.define "hxat" do |hxat|
    #hxat.vm.box = DEFAULT_VB
    hxat.vm.box = "geerlingguy/ubuntu2004"
    hxat.vm.hostname = "hxat"
    hxat.dns.patterns = [/^hxat.vm$/]
    hxat.vm.network "private_network", ip: "10.8.50.51"

    hxat.ssh.forward_agent = true
    hxat.ssh.insert_key = false

    hxat.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # hxarc node
  config.vm.define "hxarc" do |hxarc|
    hxarc.vm.box = "geerlingguy/ubuntu2004"
    hxarc.vm.hostname = "hxarc"
    hxarc.dns.patterns = [/^hxarc.vm$/]
    hxarc.vm.network "private_network", ip: "10.8.44.11"

    hxarc.ssh.forward_agent = true
    hxarc.ssh.insert_key = false

    hxarc.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # www2 node
  config.vm.define "www2" do |www2|
    www2.vm.box = DEFAULT_VB
    www2.vm.hostname = "www2"
    www2.dns.patterns = [/^www2.vm$/]
    www2.vm.network "private_network", ip: "10.8.10.11"

    www2.ssh.forward_agent = true
    www2.ssh.insert_key = false

    www2.vm.provider "virtualbox" do |v|
        v.memory = "1024"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # fnup node  (hbso files&uploads)
  config.vm.define "fnup" do |fnup|
    fnup.vm.box = DEFAULT_VB
    fnup.vm.hostname = "fnup"
    fnup.dns.patterns = [/^fnup.vm$/]
    fnup.vm.network "private_network", ip: "10.8.10.21"

    fnup.ssh.forward_agent = true
    fnup.ssh.insert_key = false

    fnup.vm.provider "virtualbox" do |v|
        v.memory = "1024"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # eedev  webserver
  config.vm.define "eedev" do |eedev|
    eedev.vm.box = DEFAULT_VB
    eedev.vm.hostname = "eedev"
    eedev.dns.patterns = [/^eedev.vm$/]
    eedev.vm.network "private_network", ip: "10.10.10.10"

    eedev.ssh.forward_agent = true
    eedev.ssh.insert_key = false

    eedev.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # hxydra  webserver
  config.vm.define "hxydra" do |hxydra|
    hxydra.vm.box = "geerlingguy/ubuntu2004"
    hxydra.vm.hostname = "hxydra"
    hxydra.dns.patterns = [/^hxydra.vm$/]
    hxydra.vm.network "private_network", ip: "10.11.10.10"

    hxydra.ssh.forward_agent = true
    hxydra.ssh.insert_key = false

    hxydra.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # issue tracker roundup: https://www.roundup-tracker.org/index.html
  config.vm.define "roundup" do |roundup|
    roundup.vm.box = "geerlingguy/ubuntu2004"
    roundup.vm.hostname = "roundup"
    roundup.dns.patterns = [/^roundup.vm$/]
    roundup.vm.network "private_network", ip: "10.77.10.10"

    roundup.ssh.forward_agent = true
    roundup.ssh.insert_key = false

    roundup.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # goaccess log analyzer https://goaccess.io/download#distro
  config.vm.define "goaccess" do |goaccess|
    goaccess.vm.box = "geerlingguy/ubuntu2004"
    goaccess.vm.hostname = "goaccess"
    goaccess.dns.patterns = [/^goaccess.vm$/]
    goaccess.vm.network "private_network", ip: "10.77.20.10"

    goaccess.ssh.forward_agent = true
    goaccess.ssh.insert_key = false

    goaccess.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

end

#
# for vagrant plugin dns
# https://stackoverflow.com/a/70704094
# https://www.virtualbox.org/manual/ch06.html#network_hostonly
# $> cat /etc/vbox/networks.conf
# * 10.0.0.0/8 192.168.0.0/16
# * 2001::/64
#
