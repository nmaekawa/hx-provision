
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

The vagrantfile in this repo will start 3 ubuntu xenial instances:

- loris.vm, the hx iiif image server
- ids.vm, another loris image server to mock the libraries server
- manifest.vm, the iiif manifest server

The hx image server (loris.vm) has a varnish cache setup in the same instance,
as well as an nginx for reverse proxy. The varnish cache uses the loris from
loris.vm and ids.vm as backend. manifest.vm is a static html server for
manifests.


    $> git clone https://github.com/nmaekawa/hximg-provision.git
    $> cd hximg-provision
    $> vagrant up


This will only start the boxes and they don't have anything installed yet. You
can change the tld and assigned local ips in the `Vagrantfile`.

Login into the boxes like below, so the ssh host key
fingerprint is stored in `~/.ssh/known_hosts`. This helps with ansible-playbook
when installing hxarc:

    $> ssh vagrant@loris.vm -i ~/.vagrant.d/insecure_private_key
    loris $> exit
    ...
    $> ssh vagrant@manifest.vm -i ~/.vagrant.d/insecure_private_key
    proxy $> exit
    ...
    $> ssh vagrant@ids.vm -i ~/.vagrant.d/insecure_private_key
    ids $> exit
    ...

# about sample images

You will have to provide some images for this install to work. Say you have a
bunch of jpg to use as sample. This will work with jpegs and non-pyramidal tiffs,
but the file extension has to be `.jgp` and `.tif` respectively (loris
requirement). The provision playbooks expects the images to be a `.tar.gz`
file, below is an example of gathering your sample images. Note that the
subdirs for hx images and libraries images is relevant as the proxy will filter
out requests that don't follow this pattern.


    # say some images are in /tmp/iiif
    $> cd /tmp
    $> tar cvzf /tmp/images.tar.gz ./iiif
    
    # and to fake the libraries server, some other images are in /tmp/ids/iiif
    $> tar cvzf /tmp/other_images.tar.gz ./ids

    # set the path in loris_vars.yml
    $> vi hximg-provision/vars/loris_vars.yml
    ...
    local_image_sample_path_tar_gz: '/tmp/images.tar.gz'
    ...
    
    # set the path for fake libraries server in the playbook
    $> vi hximg-provision/ids_play.yml
    ...
        - name: setup ids loris
            include_role:
                name: hx.loris
            vars:
                local_image_sample_path_tar_gz: '/tmp/other_images.tar.gz'
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
    # loris.vm will fail
    (venv) $> ansible-playbook -i hosts/vagrant.ini ids_play.yml
    
    # provision the images server
    (venv) $> ansible-playbook -i hosts/vagrant.ini loris_play.yml
    
    # provision the manifest
    (venv) $> ansible-playbook -i hosts/vagrant.ini manifest_play.yml
    

if all goes well, you should be able to see images in your browser by hitting
the url for hx images server:

    http://loris.vm/iiif/<your_sample_image.jpg>/full/128,/0/default.jpg


or the fake libraries server, via varnish cache:

    http://loris.vm/ids/iiif/<your_sample_image.jpg>/full/128,/0/default.jpg


---eop
