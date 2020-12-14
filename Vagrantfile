# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
#DEFAULT_VB = "bento/ubuntu-18.04"
DEFAULT_VB = "geerlingguy/ubuntu1804"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # vagrant dns; requires `vagrant plugin install vagrant-dns`
  config.dns.tld = "vm"
  VagrantDNS::Config.logger = Logger.new("dns.log")
  VagrantDNS::Config.auto_run = false

  # reverse proxy node
  config.vm.define "images" do |images|
    images.vm.box = DEFAULT_VB
    images.vm.hostname = "images"
    images.dns.patterns = [/^images.vm$/]
    images.vm.network "private_network", ip: "10.8.0.10"

    images.ssh.forward_agent = true
    images.ssh.insert_key = false

    images.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # loris image server node
  config.vm.define "loris" do |loris|
    loris.vm.box = DEFAULT_VB
    loris.vm.hostname = "loris"
    loris.dns.patterns = [/^loris.vm$/]
    loris.vm.network "private_network", ip: "10.8.0.8"

    loris.ssh.forward_agent = true
    loris.ssh.insert_key = false

    loris.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # ids image server node
  config.vm.define "ids" do |ids|
    ids.vm.box = DEFAULT_VB
    ids.vm.hostname = "ids"
    ids.dns.patterns = [/^ids.vm$/]
    ids.vm.network "private_network", ip: "10.8.0.9"

    ids.ssh.forward_agent = true
    ids.ssh.insert_key = false

    ids.vm.provider "virtualbox" do |v|
        v.memory = "4096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # hxprezi node
  config.vm.define "hxprezi" do |hxprezi|
    hxprezi.vm.box = DEFAULT_VB
    hxprezi.vm.hostname = "hxprezi"
    hxprezi.dns.patterns = [/^hxprezi.vm$/]
    hxprezi.vm.network "private_network", ip: "10.8.0.14"

    hxprezi.ssh.forward_agent = true
    hxprezi.ssh.insert_key = false

    hxprezi.vm.provider "virtualbox" do |v|
        v.memory = "1096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

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

  # ids-varnish node
  config.vm.define "idsvarnish" do |idsvarnish|
    idsvarnish.vm.box = DEFAULT_VB
    idsvarnish.vm.hostname = "idsvarnish"
    idsvarnish.dns.patterns = [/^idsvarnish.vm$/]
    idsvarnish.vm.network "private_network", ip: "10.8.0.16"

    idsvarnish.ssh.forward_agent = true
    idsvarnish.ssh.insert_key = false

    idsvarnish.vm.provider "virtualbox" do |v|
        v.memory = "1096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # hx-varnish node
  config.vm.define "hxvarnish" do |hxvarnish|
    hxvarnish.vm.box = DEFAULT_VB
    hxvarnish.vm.hostname = "hxvarnish"
    hxvarnish.dns.patterns = [/^hxvarnish.vm$/]
    hxvarnish.vm.network "private_network", ip: "10.8.0.17"

    hxvarnish.ssh.forward_agent = true
    hxvarnish.ssh.insert_key = false

    hxvarnish.vm.provider "virtualbox" do |v|
        v.memory = "1096"
        v.customize [
            "modifyvm", :id, "--natdnshostresolver1", "on",
        ]
    end
  end

  # mediamanager node
  config.vm.define "mediamanager" do |mediamanager|
    mediamanager.vm.box = DEFAULT_VB
    mediamanager.vm.hostname = "mediamanager.vm"
    mediamanager.dns.patterns = [/^mediamanager.vm$/]
    mediamanager.vm.network "private_network", ip: "10.8.0.18"

    mediamanager.ssh.forward_agent = true
    mediamanager.ssh.insert_key = false

    mediamanager.vm.provider "virtualbox" do |v|
        v.memory = "1024"
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
    catchpy.vm.box = DEFAULT_VB
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
    hxat.vm.box = DEFAULT_VB
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
    hxarc.vm.box = DEFAULT_VB
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


  # playremote node
  config.vm.define "playremote" do |playremote|
    playremote.vm.box = DEFAULT_VB
    playremote.vm.hostname = "playremote"
    playremote.dns.patterns = [/^playremote.vm$/]
    playremote.vm.network "private_network", ip: "10.8.20.10"

    playremote.ssh.forward_agent = true
    playremote.ssh.insert_key = false

    playremote.vm.provider "virtualbox" do |v|
        v.memory = "4096"
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

end
