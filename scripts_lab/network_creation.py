from openstack_sdk import create_network
import json

# ACCESS NODE
GATEWAY_IP = '' # ------------------------------------------------------------------------------------------------------ COMPLETE THIS
# ENDPOINTS
NEUTRON_ENDPOINT = 'http://' + GATEWAY_IP + ':9696/v2.0'
# CREDENTIALS
DOMAIN_ID = '' # ------------------------------------------------------------------------------------------------------- COMPLETE THIS
# DATA
token_for_project = '' # ----------------------------------------------------------------------------------------------- COMPLETE THIS
network_name = '' # ---------------------------------------------------------------------------------------------------- COMPLETE THIS

def main():
    resp3 = create_network(NEUTRON_ENDPOINT, token_for_project, network_name)
    if resp3.status_code == 201:
        print('NETWORK CREATED SUCCESSFULLY')
        network_created = resp3.json()
        print(json.dumps(network_created))
    else:
        print('FAILED NETWORK CREATION')
        return

if __name__ == "__main__":
    main()