Vagrant.configure("2") do |config|

    config.vm.define "jobmanager" do |node|
        node.vm.box = "ubuntu/xenial64"
        node.vm.network "public_network", bridge: "en0: WLAN (AirPort)"
        
        node.ssh.insert_key = false
        node.ssh.private_key_path = ["~/.ssh/id_rsa", "~/.vagrant.d/insecure_private_key"]
        node.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/authorized_keys"
        node.vm.provision "shell", inline: <<-EOC
            sudo sed -i -e "\\#PasswordAuthentication yes# s#PasswordAuthentication yes#PasswordAuthentication no#g" /etc/ssh/sshd_config
            sudo service ssh restart
        EOC
    end

    config.vm.define "worker-node-1" do |node|
        node.vm.box = "ubuntu/xenial64"
        node.vm.network "public_network", bridge: "en0: WLAN (AirPort)"
        
        node.ssh.insert_key = false
        node.ssh.private_key_path = ["~/.ssh/id_rsa", "~/.vagrant.d/insecure_private_key"]
        node.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/authorized_keys"
        node.vm.provision "shell", inline: <<-EOC
            sudo sed -i -e "\\#PasswordAuthentication yes# s#PasswordAuthentication yes#PasswordAuthentication no#g" /etc/ssh/sshd_config
            sudo service ssh restart
        EOC
    end


    config.vm.define "monitoring" do |node|
        node.vm.box = "ubuntu/xenial64"
        node.vm.network "public_network", bridge: "en0: WLAN (AirPort)"
        
        node.ssh.insert_key = false
        node.ssh.private_key_path = ["~/.ssh/id_rsa", "~/.vagrant.d/insecure_private_key"]
        node.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/authorized_keys"
        node.vm.provision "shell", inline: <<-EOC
            sudo sed -i -e "\\#PasswordAuthentication yes# s#PasswordAuthentication yes#PasswordAuthentication no#g" /etc/ssh/sshd_config
            sudo service ssh restart
        EOC
    end

    config.vm.define "nfs" do |node|
        node.vm.box = "ubuntu/xenial64"
        node.vm.network "public_network", bridge: "en0: WLAN (AirPort)"
        
        node.ssh.insert_key = false
        node.ssh.private_key_path = ["~/.ssh/id_rsa", "~/.vagrant.d/insecure_private_key"]
        node.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/authorized_keys"
        node.vm.provision "shell", inline: <<-EOC
            sudo sed -i -e "\\#PasswordAuthentication yes# s#PasswordAuthentication yes#PasswordAuthentication no#g" /etc/ssh/sshd_config
            sudo service ssh restart
        EOC
    end

    config.vm.define "dns" do |node|
        node.vm.box = "ubuntu/xenial64"
        node.vm.network "public_network", bridge: "en0: WLAN (AirPort)"
        
        node.ssh.insert_key = false
        node.ssh.private_key_path = ["~/.ssh/id_rsa", "~/.vagrant.d/insecure_private_key"]
        node.vm.provision "file", source: "~/.ssh/id_rsa.pub", destination: "~/.ssh/authorized_keys"
        node.vm.provision "shell", inline: <<-EOC
            sudo sed -i -e "\\#PasswordAuthentication yes# s#PasswordAuthentication yes#PasswordAuthentication no#g" /etc/ssh/sshd_config
            sudo service ssh restart
        EOC
    end

    
end
