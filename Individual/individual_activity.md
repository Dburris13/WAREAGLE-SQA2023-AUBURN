
# Steps to get vault4paper.py running

  - Ran Ubuntu docker image from workshop2 since I couldn't manage to build a container from the Dockerfile include in KubeSec.zip
  - Start docker session in CLI mode
	  - `docker run --rm -it project-docker`
  - Inside docker image ran the following:
  	  - `apt update`
     - `apt upgrade`         
	  - `apt install curl`
    -  `apt install git`    	 
	  - `/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"`
	  - `brew tap hashicorp/tap`
	  - `brew install hashicorp/tap/vault`
  -  Connect another shell to same docker session
	  - `docker exec -it \<container_id\> bash`
	  - Start vault server
		  - `vault server -dev`
  - Back in first terminal:
	  - Changed  vault4papyer.py hvac_url to 'http://127.0.0.1:8200'
	  - Changed vault4papyer.py hvac_token to token given by `vault server -dev` 
	  - Ran vault4paper.py
	  - `python3 vault4paper.py`
  - Walked through all the Ansible and Puppet files and replaced anything with secret, password, or user in the field name. 

  
  
