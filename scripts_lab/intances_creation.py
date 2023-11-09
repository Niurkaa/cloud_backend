from openstack_sdk import create_instance
import json

# ACCESS NODE
GATEWAY_IP = '' # ------------------------------------------------------------------------------------------------------ COMPLETE THIS
# ENDPOINTS
NOVA_ENDPOINT = 'http://' + GATEWAY_IP + ':8774/v2.1'
# CREDENTIALS
DOMAIN_ID = '' # ------------------------------------------------------------------------------------------------------- COMPLETE THIS
# DATA
token_for_project = '' # ----------------------------------------------------------------------------------------------- COMPLETE THIS
# INSTANCE 1 DATA
instance_1_name = '' # ------------------------------------------------------------------------------------------------- COMPLETE THIS
instance_1_flavor_id = '' # -------------------------------------------------------------------------------------------- COMPLETE THIS
instance_1_image_id = '' # --------------------------------------------------------------------------------------------- COMPLETE THIS
instance_1_networks = [{"port": ""}] # --------------------------------------------------------------------------------- COMPLETE THIS

# INSTANCE 2 DATA
instance_2_name = '' # ------------------------------------------------------------------------------------------------- COMPLETE THIS
instance_2_flavor_id = '' # -------------------------------------------------------------------------------------------- COMPLETE THIS
instance_2_image_id = '' # --------------------------------------------------------------------------------------------- COMPLETE THIS
instance_2_networks = [{"port": ""}] # --------------------------------------------------------------------------------- COMPLETE THIS

def main():  
    resp1 = create_instance(NOVA_ENDPOINT, token_for_project, instance_1_name, instance_1_flavor_id, instance_1_image_id, instance_1_networks)
    print(resp1.status_code)
    if resp1.status_code == 202:
        print('INSTANCE CREATED SUCCESSFULLY')
        instance_created = resp1.json()
        print(json.dumps(instance_created))
    else:
        print('FAILED INSTANCE CREATION')
        return
    
    resp2 = create_instance(NOVA_ENDPOINT, token_for_project, instance_2_name, instance_2_flavor_id, instance_2_image_id, instance_2_networks)
    print(resp2.status_code)
    if resp2.status_code == 202:
        print('INSTANCE CREATED SUCCESSFULLY')
        instance_created = resp2.json()
        print(json.dumps(instance_created))
    else:
        print('FAILED INSTANCE CREATION')
        return

if __name__ == "__main__":
    main()