
ibm_network_vlan -- Configure IBM Cloud 'ibm_network_vlan' resource
===================================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_network_vlan' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.7.1
- Terraform v0.12.20



Parameters
----------

  tags (False, list, None)
    List of tags


  resource_name (False, str, None)
    The name of the resource


  type (False, str, None)
    (Required for new resource) VLAN type


  name (False, str, None)
    VLAN name


  router_hostname (False, str, None)
    router host name


  vlan_number (False, int, None)
    VLAN number


  softlayer_managed (False, bool, None)
    Zzset to true if VLAN is managed by softlayer


  subnets (False, list, None)
    None


  datacenter (False, str, None)
    (Required for new resource) Datacenter name


  child_resource_count (False, int, None)
    Child resource count


  resource_controller_url (False, str, None)
    The URL of the IBM Cloud dashboard that can be used to explore and view details about this instance


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  iaas_classic_username (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure (SoftLayer) user name. This can also be provided via the environment variable 'IAAS_CLASSIC_USERNAME'.


  iaas_classic_api_key (False, any, None)
    (Required when generation = 1) The IBM Cloud Classic Infrastructure API key. This can also be provided via the environment variable 'IAAS_CLASSIC_API_KEY'.


  region (False, any, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

