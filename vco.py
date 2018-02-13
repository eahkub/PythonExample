#!/usr/bin/env python

##-----------------------------------------------------------------------------
##  Copyright (c) 2016 VeloCloud Networks, Inc.
##  All rights reserved.
##-----------------------------------------------------------------------------

import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__))+"/api/sdk/python")
#print os.path.dirname(os.path.abspath(__file__))+"/api/sdk/python"

import vco_client
from vco_client.rest import ApiException
import urllib3
## warnings should only be disabled if you disable ssl verification
urllib3.disable_warnings()

#TODO: edit to make example work
username = user
password = pw
operator = True
VCO = "https://(ip)/portal/rest/"

class ApiWrapper(object):
  """
  Stripped down version of the Api Wrapper used by the CLI
  """

  def __init__(self, default_url="https://localhost/portal/rest"):
    #If using dev server, the following may be helpful:
    vco_client.configuration.verify_ssl = False
    # By default, the vco_client checks for a cert file (ca-certificates.crt 
    # or ca-bundle.crt) in both
    # /etc/ssl/certs/ and /etc/pki/tls/certs/
    # if using a different file, uncomment and change the line below:
    # vco_client.configuration.ssl_ca_cert = "/etc/ssl/certs/ca-certificates.crt"
    
    self.default_url = default_url
    # initialize sdk classes
    self.client = vco_client.ApiClient(self.default_url)
    self.api = vco_client.AllApi(self.client)
    # cookie for storing login status
    self.auth_cookie = None

  def authenticate(self, username, password, operator):
    """
    Because cookie authentication isn't supported
    in the Swagger/OpenAPI spec yet, we need to 
    tell the Client to save our login cookie
    after a successful login
    """
    auth_method = self.api.login_enterprise_login
    if 'operator' in locals() and operator == True:
      auth_method = self.api.login_operator_login
    #one way to set param: use provided model class
    o = vco_client.AuthObject()
    o.username=username
    o.password=password
    try:
      auth_method(o)
    except ApiException as e:
      print "Login Error "
      sys.exit()
    if not hasattr(self.client,'last_response'):
      print "Error: No server response"
      sys.exit()
    returned_headers = self.client.last_response.getheaders()
    try:
      session_index = returned_headers['Set-Cookie'].find("velocloud.session")
      session_end = returned_headers['Set-Cookie'].find(";",session_index)
      self.client.default_headers['Cookie'] = returned_headers['Set-Cookie'][session_index:session_end]
      self.auth_cookie = returned_headers['Set-Cookie'][session_index:session_end]
    except Exception:
      print "Error retrieving authorization cookie."
      sys.exit()
    return True

print "Make sure to look at the sample.py source!"
if username == None or password == None:
  print "In order to run example, edit source - no login info supplied"
  sys.exit()
apiWrap = ApiWrapper(VCO)
apiWrap.authenticate(username,password,operator)


method = apiWrap.api.monitoring_get_enterprise_edge_link_status
print method({})

'''

# When running as operator, this will only work if edge 1 is under ent. 1. 
# Enterprise users don't need to specify an enterpriseId
# May need to change numbers for your vco.
print "Get Edge #1"
method = apiWrap.api.edge_get_edge
#Note that the key "edge_get_edge" is the same as the operationId
#and is derived from the path: /edge/getEdge => edge_get_edge
args = {"edge_get_edge":{"id":1,"enterpriseId":1}}
print method(**args)
print "\n"

"""
Most methods have logical param names.
If unsure, look at the source files in vco_client/apis/
to find method and param names
"""

"""
# all parameter names and schema specs can be found:
# via the "meta" command in the cli
# in the docs folder you received with this library (index.html)
# or in the swagger.json file itself

# to get a method via apiWrap.xxxxx(): replace x's with operationId field
#   in swagger operation object

# as mentioned above, param names come from name field in swagger parameter object
"""

# Using Models
###################################################
"""
A word of caution:
The next example uses the parameter models from vco_client/models
While these can be convienent, be aware that they mangle parameter names.
The swagger devs have decided that all params in these classes cannot
contain uppercase letters. The VCO, however, uses camelCase for all API
methods & params. The swagger code will transform the model class names into
the correct camelCase names when the method is called, but you need to
pass in the params using_the_underscore_format. Look at
the model source for more info.
"""
#Insert an enterprise user
# second way to pass in parameters:
# use supplied model objects from vco_client/models/
model = vco_client.EnterpriseObject()
#only the following three fields are required:
model.name = "Test Inc."
model.network_id = 1
model.configuration_id = 1

#but there are many optional params:
# print model.to_dict()

#as before, we pass the model to the api method
method = apiWrap.api.enterprise_insert_enterprise
print "/enterprise/insertEnterprise"
print method(model)


'''
