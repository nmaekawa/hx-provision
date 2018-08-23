
# hximg-provision
Ansible provisioning for iiif backend service

# disclaimer
For demo purposes only! provided to show how to setup a hximg vagrant
installation and support to this repo is OUT-OF-SCOPE at this time.


# for local vagrant hximg

You'll need:

- vagrant
    - install dns plugin landrush: `$> vagrant plugin install landrush`
- virtualbox
- ansible 2.4.0

# start vagrant instances

The vagrantfile in this repo will start 4 ubuntu xenial instances:

- images.vm, the hx iiif loris image server
- ids.vm, another loris image server to mock the libraries server
- manifests.vm, the iiif manifest server
- mirador.vm, a mirador(iiif image viewer) lti provider

The hx image server (images.vm) has a varnish cache setup in the same instance,
as well as an nginx for reverse proxy. The varnish cache uses the loris from
images.vm and ids.vm as backend. manifests.vm uses
[hxprezi][https://github.com/nmaekawa/hxprezi] as iiif manifest
server. The mirador lti provider
[hxmirador][https://github.com/nmaekawa/hxmirador] serves a
[mirador][http://projectmirador.org/docs/] instance via lti protocol.


    $> git clone https://github.com/nmaekawa/hximg-provision.git
    $> cd hximg-provision
    $> vagrant up


This will only start the boxes and they don't have anything installed yet. You
can change the assigned local ips in the `Vagrantfile`.

Login into the boxes like below, so the ssh host key
fingerprint is stored in `~/.ssh/known_hosts`. This helps with ansible-playbook
when installing hximg:

    $> ssh vagrant@images.vm -i ~/.vagrant.d/insecure_private_key
    images $> exit
    ...
    $> ssh vagrant@manifests.vm -i ~/.vagrant.d/insecure_private_key
    proxy $> exit
    ...
    $> ssh vagrant@ids.vm -i ~/.vagrant.d/insecure_private_key
    ids $> exit
    ...
    $> ssh vagrant@mirador.vm -i ~/.vagrant.d/insecure_private_key
    mirador $> exit
    ...

# about sample images

You will have to provide some images for this install to work. Say you have a
bunch of jpg to use as sample. This will work with jpegs and non-pyramidal tiffs,
but the file extension has to be `.jgp` and `.tif` respectively (loris
requirement). The provision playbooks expect the images to be a `.tar.gz`
file, below is an example of gathering your sample images. Note that the
subdirs for hx images and libraries images is relevant as the proxy will filter
out requests that don't follow this pattern.


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


# about sample manifests

You will have to provide some manifests that point to above mentioned sample
images as well. The provision playbooks expect the manifests to be a `.tar.gz`
file, below is an example of gathering sample manifests. Again, subdirs are
relevant since hxprezi is rigid about the format of a manifest id, and quite
coupled to HarvardX way to define manifests. Refer to the
[hxprezi][https://github.com/nmaekawa/hxprezi] repo for details.

    # say some manifests (that reference your sample images) are in /tmp/hx
    $> ls /tmp/hx
    cellx:123456.json
    ...
    $> cd /tmp
    $> tar cvzf manifests.tar.gz ./hx

    # then set the path for hx manifests in the playbook
    $> vi hximg-provision/hxprezi_play.yml
    ...
        - hosts: '{{ target_hosts | default("tag_manifest", true) }}'
          remote_user: "{{ my_remote_user }}"
          become: yes
              vars:
                 local_manifests_path_tar_gz: /tmp/manifests.tar.gz
    ...


# provision the instances

Run:

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
    
    # there's a playbook for each instance
    # provision the libraries mock -- this has to be first, otherwise varnish
    # in images.vm will fail
    (venv) $> ansible-playbook -i hosts/vagrant.ini ids_play.yml
    
    # provision the images server
    (venv) $> ansible-playbook -i hosts/vagrant.ini loris_play.yml
    
    # provision the manifest
    (venv) $> ansible-playbook -i hosts/vagrant.ini hxprezi_play.yml
    
    # provision the mirador lti provider
    (venv) $> ansible-playbook -i hosts/vagrant.ini hxmirador_play.yml

if all goes well, you should be able to see images in your browser by hitting
the url for hx images server:

    http://images.vm/iiif/<your_sample_image.jpg>/full/128,/0/default.jpg


or the fake libraries server, via varnish cache:

    http://images.vm/ids/iiif/<your_sample_image.jpg>/full/128,/0/default.jpg


you can then go to

    http://projectmirador.org/demo


and replace an object with your local manifest

    http://manifest.vm/manifests/<source>:<manifest_id>


for the example above:

    http://manifest.vm/manifests/cellx:123456


Note that this author did not find an easy way to integrate the mirador lti
provider in a local environment (yet). You can try to use the edx devstack
container as the lti consumer, but will need to tweak the networking configs in
order to get the edx in docker talking to the mirador provider in vagrant. If
you figure this out, let me know!



---eop




