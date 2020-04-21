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
  config.vm.define "catchpy" do |catchpy|
    catchpy.vm.box = DEFAULT_VB
    catchpy.vm.hostname = "catchpy.vm"
    catchpy.vm.network "private_network", ip: "10.5.50.41"

    catchpy.ssh.forward_agent = true
    catchpy.ssh.insert_key = false

    catchpy.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end

  # hxat  webserver
  config.vm.define "hxat" do |hxat|
    hxat.vm.box = DEFAULT_VB
    hxat.vm.hostname = "hxat.vm"
    hxat.vm.network "private_network", ip: "10.5.50.51"

    hxat.ssh.forward_agent = true
    hxat.ssh.insert_key = false

    hxat.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end

  # hxarc node
  config.vm.define "hxarc" do |hxarc|
    hxarc.vm.box = DEFAULT_VB
    hxarc.vm.hostname = "hxarc.vm"
    hxarc.vm.network "private_network", ip: "10.44.0.11"

    hxarc.ssh.forward_agent = true
    hxarc.ssh.insert_key = false

    hxarc.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end

  # www2 node
  config.vm.define "www2" do |www2|
    www2.vm.box = DEFAULT_VB
    www2.vm.hostname = "www2.vm"
    www2.vm.network "private_network", ip: "10.55.0.11"

    www2.ssh.forward_agent = true
    www2.ssh.insert_key = false

    www2.vm.provider "virtualbox" do |v|
        v.memory = "1024"
    end
  end

  # playremote node
  config.vm.define "playremote" do |playremote|
    playremote.vm.box = DEFAULT_VB
    playremote.vm.hostname = "playremote.vm"
    playremote.vm.network "private_network", ip: "10.222.0.10"

    playremote.ssh.forward_agent = true
    playremote.ssh.insert_key = false

    playremote.vm.provider "virtualbox" do |v|
        v.memory = "4096"
    end
  end
end
