Moje myšlienky pri spracovaní tasku:

1: deployment kontajneru Wikiny 
   po prvotnom zoznámení sa s docker-compose a deploynutí si vlastnej getting started stránky na localhoste som začal písať yaml pre dCompose (zistil som že yaml je vlastne bash skript len inak)
   Boli teda využité 3 tooliky 
      - nginx ako reverse proxy router pre wikinu,
      - wiki.js ako aplikáciu
      - postgreSQL ako databázu
   
   dockerhub bol užitočný pre pochopenie ako sa majú správne vyvolať v compose
   postgreSQL syntax bol napísaný celý na Docker-hube. 
   podobne s ostatnými dvoma

   aby spolu všetky časti dokázali komunikovať bolo treba ich hodiť na rovnakú sieť definovanú na konci (wiki-net) (zistil som cez chybovú hlášku)
   definoval som aj subnet ale to neskôr kvôli ansiblu 

   deployment kontaineru:
   ```bash
   docker compose up -d
   ```
   vytvoril som nginx.conf aby forwardovalo requesty na port 80 pre wiki.js
   kvôli getting started tutorialu mi vyhdzovali port konflikty, takže som ho musel zavraždiť getting started. 
   potom problém pretože postgres pulloval verziu 18 čo robilo data dir problémy - downgrade na postres 16 problém vyriešil. 
   na localhoste 8080 bola už wikina accesible. 
   cez klasické príkazy sa dala napríklad cez ID resetovať a zhodiť. 

2: Kompresia databázy
   celá databáza sa nachádza v /var/lib/docker/volumes/onboarding_db-data/onboarding_db-data
   tu som sa odrbal s cestou :/var/lib/postgresql/data (cesta vzhľadom na kontajner a nie mojej lokálnej db) 
   celé čo python script robí je že zavolá tento bash script: sudo docker exec onboarding-db-1 pg_dump -U user -d wikijs a zazipuje outcome. 

3: Ansible playbook time
   Potom prišlo čítanie dokumentácie pre ansible. Znovu yaml file s logickými bash inštrukciami. rozšíril som dCompose o subnet, aby som si mohol vyskúšať zbehnutie playbooku na hostoch (zakomentovaná časť v inventory #172.20.0.10 ansible_connection=local)
   v priečinku onboarding som mal všetky súbory s ktorými som pracoval tak napísanie playbooku 
   inštaloval som docker a docker compose, kopíroval som nginx.conf, docker-compose.yml, a štartoval kontajner. (zistil som že docker compose a docker-compose sú 2 rozdielne veci)
   pôvodne teda bol deploy cez shell doker compose. Neskôr som zistil že existuje takzvaý indepotentný ansible modul. (dosť important thing čo vykonáva akciu iba ak je akcia potrebná (napr že docker už je nainštalovaný alebo servre bežia))
   
   bash skript < community.docker.docker_compose_v2 


4. Vagrant
   as usual - reading manual
   bol som nadšený pretože o existencii tohoto softu som nevedel.
   zobral som si default script pre Vagrantfile, tweakol som specs a ako provisioning som pripojil ansible (čo bude spúšťať svoj playbook atď)


   Ďalší debbuging bol kvôli nesprávnemu setovaniu hostov, najskôr som mal localhosta, zmenil som na myhosts ako v inventory.ini.
   Verzia Ubuntu bola deprecated. 

   posledná aktualizácia playbooku bola celá inštalácia dockera. na to som zobral  command z https://docs.docker.com/engine/install/ubuntu/ a prepísal ho do yaml.
5. Spustenie a deployment 

1. Clone z tohoto githubu 
2. run:
   ```bash
   vagrant up
   ```
3. wikina by mala bežať na `http://<ip>:8080`
