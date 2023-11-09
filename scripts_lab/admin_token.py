from openstack_sdk import password_authentication_with_scoped_authorization

# ACCESS NODE
GATEWAY_IP = '10.20.12.226' # ------------------------------------------------------------------------------------------------------ COMPLETE THIS
# ENDPOINTS
KEYSTONE_ENDPOINT = 'http://' + GATEWAY_IP + ':5000/v3'
# CREDENTIALS
ADMIN_USER_PASSWORD = 'c60bbeea2aa5ed9dbef7c007137f871a' # --------------------------------------------------------------------------------------------- COMPLETE THIS
ADMIN_USER_USERNAME = 'admmin' # --------------------------------------------------------------------------------------------- COMPLETE THIS
ADMIN_USER_DOMAIN_NAME = 'Default' # ------------------------------------------------------------------------------------------ COMPLETE THIS
DOMAIN_ID = 'default' # ------------------------------------------------------------------------------------------------------- COMPLETE THIS
ADMIN_PROJECT_NAME = 'admin' # ---------------------------------------------------------------------------------------------- COMPLETE THIS

def main():
    # ===================================================== TOKEN FOR ADMIN USER =====================================================
    resp1 = password_authentication_with_scoped_authorization(KEYSTONE_ENDPOINT, ADMIN_USER_DOMAIN_NAME, ADMIN_USER_USERNAME, ADMIN_USER_PASSWORD, DOMAIN_ID, ADMIN_PROJECT_NAME)
    if resp1.status_code == 201:
        print('SUCCESSFUL ADMIN AUTHENTICATION')
        admin_token = resp1.headers['X-Subject-Token']
        print(admin_token)
    else:
        print('FAILED ADMIN AUTHENTICATION')
        return

if __name__ == "__main__":
    main()