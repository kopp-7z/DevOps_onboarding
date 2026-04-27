  Vagrant.configure("2") do |config|                                                                                                                                                          
    config.vm.box = "bento/ubuntu-24.04"                                                                                                                                                                    
    config.vm.network "private_network", ip: "192.168.56.10"
                                                                                                                                                                                              
    config.vm.provider "virtualbox" do |vb|                                                                                                                                                   
      vb.memory = "1024"
      vb.cpus = 3                                                                                                                                                                          
    end           
    config.vm.provision "ansible" do |ansible|
        ansible.playbook = "onboard_playbook.yml"
        ansible.inventory_path = "inventory.ini"
        ansible.limit = "myhosts"
        end                                                                                                                                                     
  end
           