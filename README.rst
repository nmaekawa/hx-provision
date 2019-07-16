
hximg-provision
===============

Ansible provisioning for HarvardX projects

disclaimer
==========

For demo purposes only! provided to show how to setup a vagrant
installation and support to this repo is OUT-OF-SCOPE at this time.


requirements
============

* vagrant 2.2.5 or later

  * install dns plugin landrush: ``$> vagrant plugin install landrush``

* virtualbox 6.0 or later
* ansible 2.8.0 or later (see below)


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






start vagrant instances
=======================

*BE WARNED:* the vagrantfile in this repo defines dozens of ubuntu instances.
Be sure to specify which instance you want like:

.. code-block:: shell

    # check all instances names
    $> vagrant status
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

    # start the ones you need
    $> vagrant up catchpy dbserver


about sample images
===================

You will have to provide some images for this install to work. Say you have a
bunch of jpg to use as sample. This will work with jpegs and non-pyramidal tiffs,
but the file extension has to be ``.jgp`` and ``.tif`` respectively (loris
requirement). The provision playbooks expect the images to be a ``.tar.gz``
file, below is an example of gathering your sample images. Note that the
subdirs for hx images and libraries images is relevant as the proxy will filter
out requests that don't follow this pattern.

.. code-block::

   # say some images are in /tmp/iiif
   $> cd /tmp
   $> tar cvzf /tmp/images.tar.gz ./iiif

   # and to fake the libraries server, some other images are in /tmp/ids/iiif
   $> tar cvzf /tmp/other_images.tar.gz ./ids

   # set the path for hx images in the playbook
   $> vi hximg-provision/loris_play.yml
   ...
       - name: setup loris
           include_role:
               name: hx.loris
           vars:
               local_image_sample_path_tar_gz: '/tmp/images.tar.gz'

   # set the path for fake libraries server in the playbook
   $> vi hximg-provision/ids_play.yml
   ...
       - name: setup ids loris
           include_role:
               name: hx.loris
           vars:
               local_image_sample_path_tar_gz: '/tmp/other_images.tar.gz'
   ...



about sample manifests
======================

You will have to provide some manifests that point to above mentioned sample
images as well. The provision playbooks expect the manifests to be a ``.tar.gz``
file, below is an example of gathering sample manifests. Again, subdirs are
relevant since hxprezi is rigid about the format of a manifest id, and quite
coupled to HarvardX way to define manifests. Refer to the
`hxprezi <https://github.com/nmaekawa/hxprezi>`_ repo for details.

.. code-block::

   # say some manifests (that reference your sample images) are in /tmp/hx
   $> ls /tmp/hx
   cellx:123456.json
   ...
   $> cd /tmp
   $> tar cvzf manifests.tar.gz ./hx

   # then set the path for hx manifests in the playbook
   $> vi hximg-provision/hxprezi_play.yml
   ...
       - hosts: '{{ target_hosts | default("tag_service_hxprezi", true) }}'
         remote_user: "{{ my_remote_user }}"
         become: yes
             vars:
                local_manifests_path_tar_gz: /tmp/manifests.tar.gz
   ...



provision the instances
=======================

Because this involves all these vms, it's easier to do it piecemeal. I had
problems accessing github.com (of all things) and having the playbooks fail
right in the beginning of the process... so, again, be warned not to expect
hximg_play.yml to work with vagrant.

Run:

.. code-block::

   # you do want a virtualenv
   $> cd hximg-provision
   $> virtualenv venv
   $> source venv/bin/activate
   (venv) $> pip install ansible

   # install external ansible roles
   (venv) $> cd roles
   (venv) $> ansible-galaxy -r requirements.yml -p ./external

   # back to hximg-provision root dir
   (venv) $> cd ..

   # set vagrant insecure key in your env
   (venv) $> ssh-add ~/.vagrant.d/insecure_private_key

   # run the common_play.yml for each instance, preferably 2 at a time
   (venv) $> ansible-playbook -i hosts/vagrant.ini common_play.yml --extra-vars target_hosts=hxmirador.vm,hxprezi.vm
   ...

   (venv) $> ansible-playbook -i hosts/vagrant.ini common_play.yml --extra-vars target_hosts=loris.vm,images.vm
   ...
   # ... and so forth


   # then provision each service; order matters
   (venv) $> ansible-playbook -i hosts/vagrant.ini ids_play.yml

   (venv) $> ansible-playbook -i hosts/vagrant.ini hxmirador_play.yml
   (venv) $> ansible-playbook -i hosts/vagrant.ini hxprezi_play.yml

   (venv) $> ansible-playbook -i hosts/vagrant.ini images_loris_play.yml
   (venv) $> ansible-playbook -i hosts/vagrant.ini images_varnish_play.yml
   (venv) $> ansible-playbook -i hosts/vagrant.ini images_reverseproxy_play.yml


if all goes well, you should be able to see images in your browser by hitting
the url for hx images server:

.. code-block::

   http://images.vm/iiif/<your_sample_image.jpg>/full/128,/0/default.jpg



or the fake libraries server, via varnish cache:

.. code-block::

   http://idsvarnish.vm/ids/iiif/<your_sample_image.jpg>/full/128,/0/default.jpg



you can then go to

.. code-block::

   http://projectmirador.org/demo



and replace an object with your local manifest

.. code-block::

   http://manifest.vm/manifests/<source>:<manifest_id>



for the example above:

.. code-block::

   http://manifest.vm/manifests/cellx:123456



Note that this author did not find an easy way to integrate the mirador lti
provider in a local environment (yet). You can try to use the edx devstack
container as the lti consumer, but will need to tweak the networking configs in
order to get the edx in docker talking to the mirador provider in vagrant. If
you figure this out, let me know!

---eop
