#####################################
#	HADOOP SINGLE NODE SETUP		
#	
#	Author: Aman Hussain
#	Email:  aman@amandavinci.me
#	Date:   12/03/2018
#
#	Notes:
#	do not run as executable script
# 
######################################

# Adding a dedicated Hadoop system user
sudo addgroup hadoop
sudo adduser --ingroup hadoop hduser
sudo adduser hduser sudo

# Installing Java

## Latest JDK9 version is JDK9.0.1 released on 16th Jan, 2018.
BASE_URL_9=http://download.oracle.com/otn-pub/java/jdk/9.0.4+11/c2514751926b4512b076cc82f959763f/jdk-9.0.4_

declare -a PLATFORMS=("linux-x64_bin.tar.gz")
# declare -a PLATFORMS=("linux-x64_bin.rpm" "linux-x64_bin.tar.gz" "osx-x64_bin.dmg" "windows-x64_bin.exe" "solaris-sparcv9_bin.tar.gz" "doc-all.zip")

for platform in "${PLATFORMS[@]}"
do
    # wget -c --no-check-certificate --no-coo22kies --header "Cookie: oraclelicense=accept-securebackup-cookie" "${BASE_URL_9}${platform}"
    curl -C - -LR#OH "Cookie: oraclelicense=accept-securebackup-cookie" -k "${BASE_URL_9}${platform}"
done

tar -xvf jdk-9.0.4_linux-x64_bin.tar.gz
rm jdk-9.0.4_linux-x64_bin.tar.gz
sudo mkdir /usr/lib/jvm
sudo mv ./jdk-9.0.4 /usr/lib/jvm/

sudo update-alternatives --install "/usr/bin/java" "java" "/usr/lib/jvm/jdk-9.0.4/bin/java" 1
sudo update-alternatives --install "/usr/bin/javac" "javac" "/usr/lib/jvm/jdk-9.0.4/bin/javac" 1
sudo update-alternatives --install "/usr/bin/javaws" "javaws" "/usr/lib/jvm/jdk-9.0.4/bin/javaws" 1

sudo chmod a+x /usr/bin/java
sudo chmod a+x /usr/bin/javac
sudo chmod a+x /usr/bin/javaws

# check installation
java -version

# Configuring SSH
su - hduser
ssh-keygen -t rsa -P ""
cat $HOME/.ssh/id_rsa.pub >> $HOME/.ssh/authorized_keys
# Test Connection to localhost
ssh localhost

# Disable IPv6
sudo cp /etc/sysctl.conf /etc/sysctl.conf.backup
echo "net.ipv6.conf.all.disable_ipv6 = 1
net.ipv6.conf.default.disable_ipv6 = 1
net.ipv6.conf.lo.disable_ipv6 = 1" | sudo tee --append /etc/sysctl.conf
sudo sysctl -p
# check IPv6 status, must be 1
cat /proc/sys/net/ipv6/conf/all/disable_ipv6

# Download Hadoop
curl -O http://redrockdigimark.com/apachemirror/hadoop/common/hadoop-3.0.0/hadoop-3.0.0.tar.gz
tar xzf hadoop-3.0.0.tar.gz
rm hadoop-3.0.0.tar.gz
sudo mv hadoop-3.0.0 /usr/local/hadoop
sudo chown -R hduser:hadoop /usr/local/hadoop

# Update Bashrc
nano ~/.bashrc
echo "# Set Hadoop-related environment variables
export HADOOP_HOME=/usr/local/hadoop
# Set JAVA_HOME 
export JAVA_HOME=/usr/lib/jvm/jdk-9.0.4/
# Add Java bin
export PATH=$JAVA_HOME/bin:$PATH
# Add Hadoop bin/ directory to PATH
export PATH=$PATH:$HADOOP_HOME/bin
# Add Hadoop sbin/ directory to PATH
export PATH=$PATH:$HADOOP_HOME/sbin"
source ~/.bashrc

# Update Hadoop ENV variables
echo "export JAVA_HOME=/usr/lib/jvm/jdk-9.0.4/" >> /usr/local/hadoop/etc/hadoop/hadoop-env.sh

# Hadoop Configuration
sudo mkdir -p /app/hadoop/tmp
sudo chown hduser:hadoop /app/hadoop/tmp
sudo chmod 750 /app/hadoop/tmp

# ADD THE FOLLOWING LINES MANUALLY

nano /usr/local/hadoop/etc/hadoop/core-site.xml
# ---
<property>
  <name>hadoop.tmp.dir</name>
  <value>/app/hadoop/tmp</value>
  <description>A base for other temporary directories.</description>
</property>

<property>
  <name>fs.default.name</name>
  <value>hdfs://localhost:54310</value>
  <description>The name of the default file system.  A URI whose
  scheme and authority determine the FileSystem implementation.  The
  uri's scheme determines the config property (fs.SCHEME.impl) naming
  the FileSystem implementation class.  The uri's authority is used to
  determine the host, port, etc. for a filesystem.</description>
</property>
# ---

nano /usr/local/hadoop/etc/hadoop/mapred-site.xml
# ---
<property>
  <name>mapred.job.tracker</name>
  <value>localhost:54311</value>
  <description>The host and port that the MapReduce job tracker runs
  at.  If "local", then jobs are run in-process as a single map
  and reduce task.
  </description>
</property>
# ---

nano /usr/local/hadoop/etc/hadoop/hdfs-site.xml
# ---
<property>
  <name>dfs.replication</name>
  <value>1</value>
  <description>Default block replication.
  The actual number of replications can be specified when the file is created.
  The default is used if replication is not specified in create time.
  </description>
</property>
# ---

# Test Hadoop Installation
start-all.sh
jps
sudo netstat -plten | grep java
stop-all.sh