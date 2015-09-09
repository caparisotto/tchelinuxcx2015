# tchelinuxcx2015


PDF
==
No diretório PDF está o PDF da apresentação, além de um PDF com as fontes utilizadas

INSTALL
==
Caso optar por visualizar os HTMLs e até editá-los, eles estão na pasta Templates.
Para iniciar a aplicação (testado em Centos7):
yum -y install epel-release
yum -y install wget python python-pip zip unzip
#O Django precisa ser instalado via PIP. Se for via Yum
#vai baixar versão menor que a 1.8, aí não vai funcionar.
#Depois não diga que eu não avisei
pip install Django
wget https://github.com/caparisotto/tchelinuxcx2015/archive/master.zip   <ou>  baixar pelo Github
unzip master.zip
cd tchelinuxcx2015-master
./manage.py runserver 0.0.0.0:8000

ACESSO
==
Via Browser em localhost:8000 
Caso esteja em máquina diferente,
Liberar no Firewall:
iptables -I INPUT -p tcp --dport 8000 -j ACCEPT
E acessar com o IP, ex.:
10.1.1.1:8000
