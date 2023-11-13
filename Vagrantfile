# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
UBUNTU2204 = "bento/ubuntu-22.04"
UBUNTU2204_DESKTOP = "fasmat/ubuntu2204-desktop"
UBUNTU_JAMMY = "ubuntu/jammy64"
UBUNTU_FOCAL = "ubuntu/focal64"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # vagrant dns; requires `vagrant plugin install vagrant-dns`
  config.dns.tld = "vm"

  # catchpy postgres
  config.vm.define "dbserver" do |dbserver|
    dbserver.vm.box = UBUNTU_JAMMY
    dbserver.vm.hostname = "dbserver"
    dbserver.dns.patterns = [/^dbserver.vm$/]
    dbserver.vm.network "private_network", ip: "10.8.50.31"

    dbserver.ssh.forward_agent = true
    dbserver.ssh.insert_key = false

    dbserver.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id,
              "--natdnshostresolver1", "on",
              "--natdnshostresolver2", "on",
        ]
    end
  end

  # catchpy webserver
  config.vm.define "catchpy" do |catchpy|
    catchpy.vm.box = UBUNTU_JAMMY
    catchpy.vm.hostname = "catchpy"
    catchpy.dns.patterns = [/^catchpy.vm$/]
    catchpy.vm.network "private_network", ip: "10.8.50.41"

    catchpy.ssh.forward_agent = true
    catchpy.ssh.insert_key = false

    catchpy.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id,
            "--natdnshostresolver1", "on",
            "--natdnshostresolver2", "on",
        ]
    end
  end

  # hxat  webserver
  config.vm.define "hxat" do |hxat|
    hxat.vm.box = UBUNTU_JAMMY
    hxat.vm.hostname = "hxat"
    hxat.dns.patterns = [/^hxat.vm$/]
    hxat.vm.network "private_network", ip: "10.8.50.51"

    hxat.ssh.forward_agent = true
    hxat.ssh.insert_key = false

    hxat.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id,
              "--natdnshostresolver1", "on",
              "--natdnshostresolver2", "on",
        ]
    end
  end

  # hxarc node
  config.vm.define "hxarc" do |hxarc|
    hxarc.vm.box = UBUNTU_JAMMY
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
    www2.vm.box = UBUNTU_JAMMY
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
    fnup.vm.box = UBUNTU_JAMMY
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
    eedev.vm.box = UBUNTU2204_DESKTOP
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
    hxydra.vm.box = UBUNTU_JAMMY
    hxydra.vm.hostname = "hxydra"
    hxydra.dns.patterns = [/^hxydra.vm$/]
    hxydra.vm.network "private_network", ip: "10.11.10.10"

    hxydra.ssh.forward_agent = true
    hxydra.ssh.insert_key = false

    hxydra.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
              "--natdnshostresolver2", "on",
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

  # lti13 inspector
  config.vm.define "inspector" do |inspector|
    inspector.vm.box = UBUNTU2204
    inspector.vm.hostname = "inspector"
    inspector.dns.patterns = [/^inspector.vm$/]
    inspector.vm.network "private_network", ip: "10.77.30.10"

    inspector.ssh.forward_agent = true
    inspector.ssh.insert_key = false

    inspector.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id,
              "--natdnshostresolver1", "on",
              "--natdnshostresolver2", "on",
        ]
    end
  end

  # ubuntu sakai
  config.vm.define "sakai" do |sakai|
    sakai.vm.box = UBUNTU_JAMMY
    sakai.vm.hostname = "sakai"
    sakai.dns.patterns = [/^sakai.vm$/]
    sakai.vm.network "private_network", ip: "10.77.30.40"

    sakai.ssh.forward_agent = true
    sakai.ssh.insert_key = false

    sakai.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id,
            "--natdnshostresolver1", "on",
            "--natdnshostresolver2", "on",
        ]
    end
  end

  # allow guests to reach each other by hostname
  config.vm.provision "allow_guest_host_resolution",
    type: "shell",
    inline: <<-SHELL
      apt update
      apt install -y avahi-daemon libnss-mdns
    SHELL

end

#
# for vagrant plugin dns
# https://stackoverflow.com/a/70704094
# https://www.virtualbox.org/manual/ch06.html#network_hostonly
# $> cat /etc/vbox/networks.conf
# * 10.0.0.0/8 192.168.0.0/16
# * 2001::/64
#
