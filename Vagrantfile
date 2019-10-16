# -*- mode: ruby -*-
# vi: set ft=ruby :

VAGRANTFILE_API_VERSION = "2"
DEFAULT_VB = "bento/ubuntu-18.04"

Vagrant.configure(VAGRANTFILE_API_VERSION) do |config|

  # vagrant dns; requires `vagrant plugin install landrush`
  config.landrush.enabled = true
  config.landrush.tld = "vm"

  # reverse proxy node
  config.vm.define "images" do |images|
    images.vm.box = DEFAULT_VB
    images.vm.hostname = "images.vm"
    images.vm.network "private_network", ip: "10.8.0.10"

    images.ssh.forward_agent = true
    images.ssh.insert_key = false

    images.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end

  # loris image server node
  config.vm.define "loris" do |loris|
    loris.vm.box = DEFAULT_VB
    loris.vm.hostname = "loris.vm"
    loris.vm.network "private_network", ip: "10.8.0.8"

    loris.ssh.forward_agent = true
    loris.ssh.insert_key = false

    loris.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end

  # ids image server node
  config.vm.define "ids" do |ids|
    ids.vm.box = DEFAULT_VB
    ids.vm.hostname = "ids.vm"
    ids.vm.network "private_network", ip: "10.8.0.9"

    ids.ssh.forward_agent = true
    ids.ssh.insert_key = false

    ids.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end

  # hxprezi node
  config.vm.define "hxprezi" do |hxprezi|
    hxprezi.vm.box = DEFAULT_VB
    hxprezi.vm.hostname = "hxprezi.vm"
    hxprezi.vm.network "private_network", ip: "10.8.0.14"

    hxprezi.ssh.forward_agent = true
    hxprezi.ssh.insert_key = false

    hxprezi.vm.provider "virtualbox" do |v|
        v.memory = "1096"
    end
  end

  # mirador-lti node
  config.vm.define "mirador" do |mirador|
    mirador.vm.box = DEFAULT_VB
    mirador.vm.hostname = "mirador.vm"
    mirador.vm.network "private_network", ip: "10.8.0.15"

    mirador.ssh.forward_agent = true
    mirador.ssh.insert_key = false

    mirador.vm.provider "virtualbox" do |v|
        v.memory = "1096"
    end
  end

  # ids-varnish node
  config.vm.define "idsvarnish" do |idsvarnish|
    idsvarnish.vm.box = DEFAULT_VB
    idsvarnish.vm.hostname = "idsvarnish.vm"
    idsvarnish.vm.network "private_network", ip: "10.8.0.16"

    idsvarnish.ssh.forward_agent = true
    idsvarnish.ssh.insert_key = false

    idsvarnish.vm.provider "virtualbox" do |v|
        v.memory = "1096"
    end
  end

  # hx-varnish node
  config.vm.define "hxvarnish" do |hxvarnish|
    hxvarnish.vm.box = DEFAULT_VB
    hxvarnish.vm.hostname = "hxvarnish.vm"
    hxvarnish.vm.network "private_network", ip: "10.8.0.17"

    hxvarnish.ssh.forward_agent = true
    hxvarnish.ssh.insert_key = false

    hxvarnish.vm.provider "virtualbox" do |v|
        v.memory = "1096"
    end
  end

  # catchpy postgres
  config.vm.define "dbserver" do |dbserver|
    dbserver.vm.box = DEFAULT_VB
    dbserver.vm.hostname = "dbserver.vm"
    dbserver.vm.network "private_network", ip: "10.5.50.31"

    dbserver.ssh.forward_agent = true
    dbserver.ssh.insert_key = false

    dbserver.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end

  # catchpy webserver
  config.vm.define "catchpy" do |dbserver|
    dbserver.vm.box = DEFAULT_VB
    dbserver.vm.hostname = "catchpy.vm"
    dbserver.vm.network "private_network", ip: "10.5.50.41"

    dbserver.ssh.forward_agent = true
    dbserver.ssh.insert_key = false

    dbserver.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end

  # hxat  webserver
  config.vm.define "hxat" do |dbserver|
    dbserver.vm.box = DEFAULT_VB
    dbserver.vm.hostname = "hxat.vm"
    dbserver.vm.network "private_network", ip: "10.5.50.51"

    dbserver.ssh.forward_agent = true
    dbserver.ssh.insert_key = false

    dbserver.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end

  # hxarc node
  config.vm.define "hxarc" do |hxarc|
    hxarc.vm.box = "bento/ubuntu-16.04"
    hxarc.vm.hostname = "hxarc.vm"
    hxarc.vm.network "private_network", ip: "10.44.0.11"

    hxarc.ssh.forward_agent = true
    hxarc.ssh.insert_key = false

    hxarc.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end

  # rsyslog server node
  config.vm.define "rsyslog" do |rsyslog|
    rsyslog.vm.box = DEFAULT_VB
    rsyslog.vm.hostname = "rsyslog.vm"
    rsyslog.vm.network "private_network", ip: "10.55.0.11"

    rsyslog.ssh.forward_agent = true
    rsyslog.ssh.insert_key = false

    rsyslog.vm.provider "virtualbox" do |v|
        v.memory = "2048"
    end
  end
end
