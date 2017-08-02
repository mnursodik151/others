# -*- mode: ruby -*-
# vi: set ft=ruby :

# All Vagrant configuration is done below. The "2" in Vagrant.configure
# configures the configuration version (we support older styles for
# backwards compatibility). Please don't change it unless you know what
# you're doing.
Vagrant.configure("2") do |config|
  # The most common configuration options are documented and commented below.
  # For a complete reference, please see the online documentation at
  # https://docs.vagrantup.com.

  # Every Vagrant development environment requires a box. You can search for
  # boxes at https://atlas.hashicorp.com/search.
  config.vm.box = "bhawiyuga/hadoop-spark"

  # config.vm.synced_folder "../data", "/vagrant_data"

  config.vm.provider "virtualbox" do |vb|
    vb.gui = false
    vb.memory = "512"
  end

  config.vm.define "slave_node1" do |vm|
  vm.vm.network "private_network", ip: "192.168.56.2", netmask: "28", virtualbox__intnet: "network1"
  vm.vm.provision "shell", inline: <<-SHELL
    sudo addgroup hadoop
    sudo adduser --ingroup hadoop --disabled-password --gecos "" hduser
    sudo adduser hduser sudo
    echo "hduser:123" | sudo chpasswd
    sudo chown -R hduser:hadoop /usr/local/hadoop
    sudo chown -R hduser:hadoop /usr/local/hadoop-2.7.1
    sudo su - hduser
    sudo sed -i '25s|.*|export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/jre/|g' /usr/local/hadoop/etc/hadoop/hadoop-env.sh
    echo $JAVA_HOME
    mkdir -pv /usr/local/hadoop/data/datanode
    echo "FINISHED PROVISIONING"
  SHELL
  end

  config.vm.define "slave_node2" do |vm|
  vm.vm.network "private_network", ip: "192.168.56.3", netmask: "28", virtualbox__intnet: "network1"
  vm.vm.provision "shell", inline: <<-SHELL
    sudo addgroup hadoop
    sudo adduser --ingroup hadoop --disabled-password --gecos "" hduser
    sudo adduser hduser sudo
    echo "hduser:123" | sudo chpasswd
    sudo chown -R hduser:hadoop /usr/local/hadoop
    sudo chown -R hduser:hadoop /usr/local/hadoop-2.7.1
    sudo su - hduser
    sudo sed -i '25s|.*|export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/jre/|g' /usr/local/hadoop/etc/hadoop/hadoop-env.sh
    echo $JAVA_HOME
    mkdir -pv /usr/local/hadoop/data/datanode
    echo "FINISHED PROVISIONING"
  SHELL
  end

  config.vm.define "master_node" do |vm|
  vm.vm.network "private_network", ip: "172.13.10.1", netmask: "24"
  vm.vm.network "private_network", ip: "192.168.56.1", netmask: "28", virtualbox__intnet: "network1"
  vm.vm.provision "shell", inline: <<-SHELL
    sudo sysctl -w net.ipv4.ip_forward=1
    sudo route add -net 172.13.10.0 netmask 255.255.255.0 dev eth1
    sudo route add -net 192.168.56.0 netmask 255.255.255.240 dev eth2
    sudo iptables -t nat -A POSTROUTING -o eth2 -j MASQUERADE
    sudo iptables -t nat -A POSTROUTING -o eth1 -j MASQUERADE
    sudo iptables -A FORWARD -i eth1 -o eth2 -j ACCEPT
    sudo iptables -A FORWARD -i eth2 -o eth1 -j ACCEPT
    sudo iptables-save > /etc/iptables.rules
    sudo addgroup hadoop
    sudo adduser --ingroup hadoop --disabled-password --gecos "" hduser
    sudo adduser hduser sudo
    echo "hduser:123" | sudo chpasswd
    sudo chown -R hduser:hadoop /usr/local/hadoop
    sudo chown -R hduser:hadoop /usr/local/hadoop-2.7.1
    sudo su - hduser
    sudo sed -i '25s|.*|export JAVA_HOME=/usr/lib/jvm/java-7-openjdk-amd64/jre/|g' /usr/local/hadoop/etc/hadoop/hadoop-env.sh
    echo $JAVA_HOME
    mkdir -pv /usr/local/hadoop/data/namenode
    mkdir -pv /usr/local/hadoop/data/datanode
    echo "FINISHED PROVISIONING"
  SHELL
  end

end
