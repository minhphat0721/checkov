import unittest

from checkov.terraform.models.enums import CheckResult
from checkov.terraform.checks.resource.gcp.GoogleComputeMinTLSVersion import check


class TestGoogleComputeMinTLSVersion(unittest.TestCase):

    def test_failure(self):
        resource_conf =  {'name': ['nonprod-ssl-policy'], 'profile': ['MODERN']
                          }

        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILURE, scan_result)

    def test_success(self):
        resource_conf = {'name': ['nonprod-ssl-policy'], 'profile': ['MODERN'], 'min_tls_version': ['TLS_1_2']}
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.SUCCESS, scan_result)


if __name__ == '__main__':
    unittest.main()
