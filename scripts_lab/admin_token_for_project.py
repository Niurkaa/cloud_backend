from openstack_sdk import token_authentication_with_scoped_authorization

# ACCESS NODE
GATEWAY_IP = '' # ------------------------------------------------------------------------------------------------------ COMPLETE THIS
# ENDPOINTS
KEYSTONE_ENDPOINT = 'http://' + GATEWAY_IP + ':5000/v3'
# CREDENTIALS
DOMAIN_ID = '' # ------------------------------------------------------------------------------------------------------- COMPLETE THIS
# DATA
admin_token = '' # ----------------------------------------------------------------------------------------------------- COMPLETE THIS
project_name = '' # ---------------------------------------------------------------------------------------------------- COMPLETE THIS

def main():
    # ===================================================== TOKEN FOR PROJECT =====================================================
    resp = token_authentication_with_scoped_authorization(KEYSTONE_ENDPOINT, admin_token, DOMAIN_ID, project_name)
    if resp.status_code == 201:
        print('SUCCESSFUL AUTHENTICATION FOR PROJECT ' + project_name)
        token_for_project = resp.headers['X-Subject-Token']
        print(token_for_project)
    else:
        print('FAILED AUTHENTICATION FOR PROJECT ' + project_name)
        return

if __name__ == "__main__":
    main()