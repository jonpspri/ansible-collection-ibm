#!/usr/bin/python
# -*- coding: utf-8 -*-

ANSIBLE_METADATA = {'metadata_version': '1.1',
                    'status': ['preview'],
                    'supported_by': 'community'}

DOCUMENTATION = '''
---
module: ibm_cis_rate_limit
short_description: Configure IBM Cloud 'ibm_cis_rate_limit' resource

version_added: "2.8"

description:
    - Create, update or destroy an IBM Cloud 'ibm_cis_rate_limit' resource

requirements:
    - IBM-Cloud terraform-provider-ibm v1.7.1
    - Terraform v0.12.20

options:
    threshold:
        description:
            - (Required for new resource) Rate Limiting Threshold
        required: False
        type: int
    disabled:
        description:
            - Whether this rate limiting rule is currently disabled.
        required: False
        type: bool
        default: False
    description:
        description:
            - A note that you can use to describe the reason for a rate limiting rule.
        required: False
        type: str
    bypass:
        description:
            - Bypass URL
        required: False
        type: list
        elements: dict
    period:
        description:
            - (Required for new resource) Rate Limiting Period
        required: False
        type: int
    correlate:
        description:
            - Ratelimiting Correlate
        required: False
        type: list
        elements: dict
    action:
        description:
            - (Required for new resource) Rate Limiting Action
        required: False
        type: list
        elements: dict
    cis_id:
        description:
            - (Required for new resource) CIS Intance CRN
        required: False
        type: str
    domain_id:
        description:
            - (Required for new resource) CIS Domain ID
        required: False
        type: str
    match:
        description:
            - Rate Limiting Match
        required: False
        type: list
        elements: dict
    rule_id:
        description:
            - Rate Limit rule Id
        required: False
        type: str
    id:
        description:
            - (Required when updating or destroying existing resource) IBM Cloud Resource ID.
        required: False
        type: str
    state:
        description:
            - State of resource
        choices:
            - available
            - absent
        default: available
        required: False
    iaas_classic_username:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure (SoftLayer) user name. This can also be provided
              via the environment variable 'IAAS_CLASSIC_USERNAME'.
        required: False
    iaas_classic_api_key:
        description:
            - (Required when generation = 1) The IBM Cloud Classic
              Infrastructure API key. This can also be provided via the
              environment variable 'IAAS_CLASSIC_API_KEY'.
        required: False
    region:
        description:
            - The IBM Cloud region where you want to create your
              resources. If this value is not specified, us-south is
              used by default. This can also be provided via the
              environment variable 'IC_REGION'.
        default: us-south
        required: False
    ibmcloud_api_key:
        description:
            - The IBM Cloud API key to authenticate with the IBM Cloud
              platform. This can also be provided via the environment
              variable 'IC_API_KEY'.
        required: True

author:
    - Jay Carman (@jaywcarman)
'''

# Top level parameter keys required by Terraform module
TL_REQUIRED_PARAMETERS = [
    ('threshold', 'int'),
    ('period', 'int'),
    ('action', 'list'),
    ('cis_id', 'str'),
    ('domain_id', 'str'),
]

# All top level parameter keys supported by Terraform module
TL_ALL_PARAMETERS = [
    'threshold',
    'disabled',
    'description',
    'bypass',
    'period',
    'correlate',
    'action',
    'cis_id',
    'domain_id',
    'match',
    'rule_id',
]

# define available arguments/parameters a user can pass to the module
from ansible_collections.ibmcloud.ibmcollection.plugins.module_utils.ibmcloud import Terraform, ibmcloud_terraform
from ansible.module_utils.basic import env_fallback
module_args = dict(
    threshold=dict(
        required=False,
        type='int'),
    disabled=dict(
        default=False,
        type='bool'),
    description=dict(
        required=False,
        type='str'),
    bypass=dict(
        required=False,
        elements='',
        type='list'),
    period=dict(
        required=False,
        type='int'),
    correlate=dict(
        required=False,
        elements='',
        type='list'),
    action=dict(
        required=False,
        elements='',
        type='list'),
    cis_id=dict(
        required=False,
        type='str'),
    domain_id=dict(
        required=False,
        type='str'),
    match=dict(
        required=False,
        elements='',
        type='list'),
    rule_id=dict(
        required=False,
        type='str'),
    id=dict(
        required=False,
        type='str'),
    state=dict(
        type='str',
        required=False,
        default='available',
        choices=(['available', 'absent'])),
    iaas_classic_username=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_USERNAME']),
        required=False),
    iaas_classic_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IAAS_CLASSIC_API_KEY']),
        required=False),
    region=dict(
        type='str',
        fallback=(env_fallback, ['IC_REGION']),
        default='us-south'),
    ibmcloud_api_key=dict(
        type='str',
        no_log=True,
        fallback=(env_fallback, ['IC_API_KEY']),
        required=True)
)


def run_module():
    from ansible.module_utils.basic import AnsibleModule

    module = AnsibleModule(
        argument_spec=module_args,
        supports_check_mode=False
    )

    # New resource required arguments checks
    missing_args = []
    if module.params['id'] is None:
        for arg, _ in TL_REQUIRED_PARAMETERS:
            if module.params[arg] is None:
                missing_args.append(arg)
        if missing_args:
            module.fail_json(msg=(
                "missing required arguments: " + ", ".join(missing_args)))

    result = ibmcloud_terraform(
        resource_type='ibm_cis_rate_limit',
        tf_type='resource',
        parameters=module.params,
        ibm_provider_version='1.7.1',
        tl_required_params=TL_REQUIRED_PARAMETERS,
        tl_all_params=TL_ALL_PARAMETERS)

    if result['rc'] > 0:
        module.fail_json(
            msg=Terraform.parse_stderr(result['stderr']), **result)

    module.exit_json(**result)


def main():
    run_module()


if __name__ == '__main__':
    main()
