Vagrant.configure("2") do |config|

    config.vm.define "jobmanager" do |jobmanager|
        jobmanager.vm.box = "ubuntu/xenial64"
        jobmanager.vm.network "public_network" # , bridge: "en0: WLAN (AirPort)"
        
        jobmanager.ssh.insert_key = false
        jobmanager.ssh.private_key_path = ["~/.ssh/id_rsa", "~/.vagrant.d/insecure_private_key"]
        jobmanager.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/authorized_keys"
        jobmanager.vm.provision "shell", inline: <<-EOC
            sudo sed -i -e "\\#PasswordAuthentication yes# s#PasswordAuthentication yes#PasswordAuthentication no#g" /etc/ssh/sshd_config
            sudo service ssh restart
        EOC

        jobmanager.vm.provision "ansible" do |ansible|
            ansible.playbook = "site.yml"
            ansible.become = true
            ansible.vault_password_file = "credentials.vault"
        end 
    end

    config.vm.define "worker-node-1" do |worker|
        worker.vm.box = "ubuntu/xenial64"
        worker.vm.network "public_network" # , bridge: "en0: WLAN (AirPort)"
        
        worker.ssh.insert_key = false
        worker.ssh.private_key_path = ["~/.ssh/id_rsa", "~/.vagrant.d/insecure_private_key"]
        worker.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/authorized_keys"
        worker.vm.provision "shell", inline: <<-EOC
            sudo sed -i -e "\\#PasswordAuthentication yes# s#PasswordAuthentication yes#PasswordAuthentication no#g" /etc/ssh/sshd_config
            sudo service ssh restart
        EOC

        worker.vm.provision "ansible" do |ansible|
            ansible.playbook = "site.yml"
            ansible.become = true
            ansible.vault_password_file = "credentials.vault"
        end 
    end
end
