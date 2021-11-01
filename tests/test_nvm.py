def test_nvm_installed(host):
    assert host.package("nvm").is_installed
