
ibm_pi_key -- Configure IBM Cloud 'ibm_pi_key' resource
=======================================================

.. contents::
   :local:
   :depth: 1


Synopsis
--------

Create, update or destroy an IBM Cloud 'ibm_pi_key' resource



Requirements
------------
The below requirements are needed on the host that executes this module.

- IBM-Cloud terraform-provider-ibm v1.7.1
- Terraform v0.12.20



Parameters
----------

  pi_creation_date (False, str, None)
    Date info


  pi_cloud_instance_id (False, str, None)
    (Required for new resource) PI cloud instance ID


  key_id (False, str, None)
    Key ID in the PI instance


  pi_key_name (False, str, None)
    (Required for new resource) Key name in the PI instance


  pi_ssh_key (False, str, None)
    (Required for new resource) PI instance key info


  id (False, str, None)
    (Required when updating or destroying existing resource) IBM Cloud Resource ID.


  state (False, any, available)
    State of resource


  zone (False, str, None)
    Denotes which IBM Cloud zone to connect to in multizone environment. This can also be provided via the environment variable 'IC_ZONE'.


  region (False, str, us-south)
    The IBM Cloud region where you want to create your resources. If this value is not specified, us-south is used by default. This can also be provided via the environment variable 'IC_REGION'.


  ibmcloud_api_key (True, any, None)
    The IBM Cloud API key to authenticate with the IBM Cloud platform. This can also be provided via the environment variable 'IC_API_KEY'.













Authors
~~~~~~~

- Jay Carman (@jaywcarman)

