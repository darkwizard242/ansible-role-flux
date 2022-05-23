import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


PACKAGE_BINARY = '/usr/local/bin/flux'


def test_flux_binary_exists(host):
    """
    Tests if flux binary exists.
    """
    assert host.file(PACKAGE_BINARY).exists


def test_flux_binary_file(host):
    """
    Tests if flux binary is a file type.
    """
    assert host.file(PACKAGE_BINARY).is_file


def test_flux_binary_which(host):
    """
    Tests the output to confirm flux's binary location.
    """
    assert host.check_output('which flux') == PACKAGE_BINARY
