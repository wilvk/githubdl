#!/usr/local/bin/python

import os
import sys
import inspect
from nose import with_setup
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
includedir = os.path.join(parentdir, "githubdl")
sys.path.insert(0, includedir)
import url_helpers as uh

class TestUrlHelpers:

    def test_check_url_is_http_http(self):
        result = uh.check_url_is_http("http://test.com")
        assert result == True

    def test_check_url_is_http_https(self):
        result = uh.check_url_is_http("https://test.com")
        assert result == True

    def test_check_url_is_not_http_1(self):
        result = uh.check_url_is_http("httpxx://test.com")
        assert result == False

    def test_check_url_is_not_http_2(self):
        result = uh.check_url_is_http("htp://test.com")
        assert result == False

    def test_check_url_is_ssh(self):
        result = uh.check_url_is_ssh("git@github.com:pypa/sampleproject.git")
        assert result == True

    def test_check_url_is_not_ssh_invalid_user(self):
        result = uh.check_url_is_ssh("giti_@github.com:pypa/sampleproject.git")
        assert result == False

    def test_check_url_is_not_ssh_slash(self):
        result = uh.check_url_is_ssh("git@test.com/test.git")
        assert result == True

    def test_check_url_is_not_ssh_http(self):
        result = uh.check_url_is_ssh("htp://test.com")
        assert result == False

    def test_get_domain_name_from_http(self):
        result = uh.get_domain_name_from_http_url("https://github.com/pypa/sampleproject.git")
        assert result == "github.com"

    def test_get_repo_name_from_http_url(self):
        result = uh.get_repo_name_from_http_url("https://github.com/pypa/sampleproject.git")
        assert result == "pypa/sampleproject"

    def test_get_domain_name_from_ssh_url(self):
        result = uh.get_domain_name_from_ssh_url("git@github.com:pypa/sampleproject.git")
        assert result == "github.com"

    def test_get_repo_name_from_ssh_url(self):
        result = uh.get_repo_name_from_ssh_url("git@github.com:pypa/sampleproject.git")
        assert result == "pypa/sampleproject"

