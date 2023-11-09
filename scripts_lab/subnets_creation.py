from openstack_sdk import create_subnet
import json

# ACCESS NODE
GATEWAY_IP = '' # ------------------------------------------------------------------------------------------------------ COMPLETE THIS
# ENDPOINTS
NEUTRON_ENDPOINT = 'http://' + GATEWAY_IP + ':9696/v2.0'
# CREDENTIALS
DOMAIN_ID = '' # ------------------------------------------------------------------------------------------------------- COMPLETE THIS
# DATA
token_for_project = '' # ----------------------------------------------------------------------------------------------- COMPLETE THIS
network_id = '' # ------------------------------------------------------------------------------------------------------ COMPLETE THIS
subnet_name = '' # ----------------------------------------------------------------------------------------------------- COMPLETE THIS
ip_version = '' # ------------------------------------------------------------------------------------------------------ COMPLETE THIS
cidr = '' # ------------------------------------------------------------------------------------------------------------ COMPLETE THIS

def main():
    resp = create_subnet(NEUTRON_ENDPOINT, token_for_project, network_id, subnet_name, ip_version, cidr)
    if resp.status_code == 201:
        print('SUBNET CREATED SUCCESSFULLY')
        subnet_created = resp.json()
        print(json.dumps(subnet_created))
    else:
        print('FAILED SUBNET CREATION')
        return

if __name__ == "__main__":
    main()