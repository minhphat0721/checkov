import unittest

from checkov.terraform.models.enums import CheckResult
from checkov.terraform.checks.resource.aws.S3AccessLogs import check


class TestS3AccessLogs(unittest.TestCase):

    def test_failure_s3_accesslogs(self):
        resource_conf = {"region": ["us-west-2"],
                         "bucket": ["my_bucket"],
                         "acl": ["public-read"],
                         "force_destroy": [True],
                         "tags": [{"Name": "my-bucket"}]}
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.FAILURE, scan_result)

    def test_success_s3_accesslogs(self):

        resource_conf = {"region": ["us-west-2"],
                         "bucket": ["my_bucket"],
                         "acl": ["public-read"],
                         "force_destroy": [True],
                         "tags": [{"Name": "my-bucket"}],
                         "logging": [{"target_bucket": "logging-bucket",
                                      "target_prefix": "log/"
                                      }]}
        scan_result = check.scan_resource_conf(conf=resource_conf)
        self.assertEqual(CheckResult.SUCCESS, scan_result)


if __name__ == '__main__':
    unittest.main()
