Steps to get vault4paper.py running

Running on Ubunutu docker image from workshop2


Start docker session in CLI mode
	docker run --rm -it project-docker
	
Connect another shell to same docker session
	docker exec -it 94a4cbac79cf bash

	apt-get install curl
	/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	brew tap hashicorp/tap
	brew install hashicorp/tap/vault

Start vault server
	vault server -dev
	
In vault4papyer.py changed hvac_url to 'http://127.0.0.1:8200'
In vault4papyer.py changed hvac_token to 'hvs.v6MgsXtppeoTusv75gsigVO4'

	python3 vault4paper.py



main.yaml
	Replaced the following elements in main.yml:
	kie_admin_user:
	kie_admin_password:
	nexus_admin_user:
	nexus_admin_password:
	bcentral_app_secret:
	kserver_app_secret:
	kieserver_controller_user:
	kieserver_controller_password:
	kieserver_user:
	kieserver_password:
	kie_maven_user:
	kie_maven_password:

user_secerets.yaml	
	Replaced ALL elements in user_secrets.yml

vm.yaml
	Replaced all phrases of the word "secret" with the same vault lookup value since it's all the same password
	Replaced the following secrets:
	'very-long-long-long-long-long-secret'
	'NA'
	'Y3nS5p0bKLI8bR/thxo0CFS3uItJXifjfRymRGOGJhRgij48ttTjPR33ZdAhobHrXd5MJNz4X69wYKvsUMlIfg=='
	Did not replace the private keys in vm.yaml

all.pp, cloudcontroller.pp, 
	Replaced all "password" with the same vault lookup
	Replaced "12345" with same vault lookup
	Replaced admin_email with lookup
	
magnum.pp
	Replaced the following secrets:
	'an_even_bigger_secret'
	'magnum'
	'oh_my_no_secret'
	'a_big_secret'

nova.pp
	Replaced 'an_even_bigger_secret' and 'a_big_secret" with same links from magnum.pp	
	Replaced the following secrets with new links:
	'nova'
	'openstack'
	'7200aea0-2ddd-4a32-aa2a-d49f66ab554c'
	'AQD7kyJQQGoOBhAAqrPAqSopSwPrrfMMomzVdw=='

site.pp
	Replaced the following secrets:
	'keystone'
	'ChangeMe'
	'test@puppetlabs.com'
	'glance_password'
	'glance'
	'glance_pass'


