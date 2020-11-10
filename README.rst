
hx-provision
===============

Ansible provisioning for HarvardX projects.

To learn more about these projects, visit the hx wiki *** hx wiki link HERE ***.


disclaimer
==========

    For demo purposes only! These playbooks are provided to show how to setup
    a vagrant installation and support to this repo is ``OUT-OF-SCOPE``
    at this time.


requirements
============

* vagrant_ 2.2.13 or later
  * install dns plugin vagrant-dns_: ``$> vagrant plugin install vagrant-dns``

* virtualbox_ 6.1 or later
* ansible_ 2.9.8 or later (see below)


setup
=====

We usually set a virtualenv for ansible and other python packages.

.. code-block:: shell

    # create venv and install
    $> virtualenv -p python3 venv
    $> source ansible/bin/activate
    (venv) $>

    # install ansible
    (venv) $> pip install ansible

    # clone this repo
    (venv) $> git clone https://github.com/nmaekawa/hximg-provision.git

    # install ansible-roles requirements
    (venv) $> cd hximg-provision/roles
    (venv) $> ansible-galaxy install -p ./external -r ./requirements.yml

    # set vagrant insecure key in your env
    (venv) $> ssh-add ~/.vagrant.d/insecure_private_key

    # register vagrant-dns as a resolver
    (venv) $> vagrant dns --install

    # run vagrant-dns server
    (venv> $> vagrant dns --start


vagrant instances
=================

*BE WARNED:* The Vagrantfile in this repo defines dozens of ubuntu instances.
Be sure to specify which instance you want to launch:

.. code-block:: shell

    # check all instances names
    (venv) $> vagrant status
    Current machine states:

    images                    not created (virtualbox)
    loris                     not created (virtualbox)
    ids                       not created (virtualbox)
    hxprezi                   not created (virtualbox)
    mirador                   not created (virtualbox)
    idsvarnish                not created (virtualbox)
    hxvarnish                 not created (virtualbox)
    dbserver                  not created (virtualbox)
    catchpy                   not created (virtualbox)
    hxat                      not created (virtualbox)
    hxarc                     not created (virtualbox)

    This environment represents multiple VMs. The VMs are all listed
    above with their current state. For more information about a specific
    VM, run `vagrant status NAME`.

    # start the ones you need, say for catchpy and dbserver
    (venv) $> vagrant up catchpy dbserver


provision/config the instances
==============================

The overall workflow is:

- vagrant up instances for target project
- run relevant ansible playbooks

In the subdir `hosts` there are ansible inventory files for each project.
These inventories match the IPs and hostnames defined in the `Vagrantfile`.

In general, the defaults are good for vagrant instances and env vars are not
needed.


.. code-block:: shell

   # apply playbook
   (venv) $> ansible-playbook -i hosts/<relevant-vagrant-ini-file> <relevant-playbook-file>
   ...


To learn which playbooks are relevant for each project, see the hxwiki_.

---eop



.. _vagrant: https://www.vagrantup.com
.. _ansible: https://www.ansible.com
.. _virtualbox: https://www.virtualbox.org
.. _vagrant-dns: https://github.com/BerlinVagrant/vagrant-dns
.. _hxwiki: https://github.com/nmaekawa/hx-provision/wiki



