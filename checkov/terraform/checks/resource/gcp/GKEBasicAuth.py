from checkov.terraform.checks.resource.base_resource_check import BaseResourceCheck
from checkov.common.models.enums import CheckResult, CheckCategories


class GKEBasicAuth(BaseResourceCheck):
    def __init__(self):
        name = "Ensure GKE basic auth is disabled"
        id = "CKV_GCP_19"
        supported_resources = ['google_container_cluster']
        categories = [CheckCategories.GENERAL_SECURITY]
        super().__init__(name=name, id=id, categories=categories, supported_resources=supported_resources)

    def scan_resource_conf(self, conf):
        """
            Looks for password configuration at azure_instance:
            https://www.terraform.io/docs/providers/google/r/compute_ssl_policy.html
        :param conf: google_compute_ssl_policy configuration
        :return: <CheckResult>
        """
        if 'master_auth' in conf.keys():
            if 'username' in conf['master_auth'][0].keys() and 'password' in conf['master_auth'][0].keys():
                return CheckResult.FAILED
        return CheckResult.PASSED


check = GKEBasicAuth()
