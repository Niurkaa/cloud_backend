from openstack_sdk import create_port
import json

# ACCESS NODE
GATEWAY_IP = '' # ------------------------------------------------------------------------------------------------------ COMPLETE THIS
# ENDPOINTS
NEUTRON_ENDPOINT = 'http://' + GATEWAY_IP + ':9696/v2.0'
# CREDENTIALS
DOMAIN_ID = '' # ------------------------------------------------------------------------------------------------------- COMPLETE THIS
# DATA
token_for_project = '' # ----------------------------------------------------------------------------------------------- COMPLETE THIS
port_name = '' # ------------------------------------------------------------------------------------------------------- COMPLETE THIS
network_id = '' # ------------------------------------------------------------------------------------------------------ COMPLETE THIS
project_id = '' # ------------------------------------------------------------------------------------------------------ COMPLETE THIS

def main():
    resp1 = create_port(NEUTRON_ENDPOINT, token_for_project, port_name, network_id, project_id)
    if resp1.status_code == 201:
        print('PORT CREATED SUCCESSFULLY')
        port_created = resp1.json()
        print(json.dumps(port_created))
    else:
        print('FAILED PORT CREATION')
        return

    resp2 = create_port(NEUTRON_ENDPOINT, token_for_project, port_name, network_id, project_id)
    if resp2.status_code == 201:
        print('PORT CREATED SUCCESSFULLY')
        port_created = resp2.json()
        print(json.dumps(port_created))
    else:
        print('FAILED PORT CREATION')
        return

if __name__ == "__main__":
    main()