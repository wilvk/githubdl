#!/usr/local/bin/python

import os
import sys
import inspect
import shutil
from pathlib import Path
from nose import with_setup
import githubdl

class TestGithubPathDl:

    @classmethod
    def setup_class(self):
        self.single_file_name = "README.md"
        self.single_dir_name = "support"
        self.test_repo_url_http = "https://github.com/wilvk/pbec"
        self.test_repo_url_ssh = "git@github.com:wilvk/pbec.git"

    def is_single_file_present(self):
        single_file = Path(self.single_file_name)
        return single_file.is_file()

    def is_single_file_nonzero(self):
        file_info = os.stat(self.single_file_name)
        return file_info.st_size > 0

    def is_single_dir_present(self):
        single_dir = Path(self.single_dir_name)
        return single_dir.is_dir()

    def cleanup(self):
        if self.is_single_file_present():
           os.remove(self.single_file_name)
        if self.is_single_dir_present():
            shutil.rmtree(self.single_dir_name)

    def teardown(self):
        self.cleanup()

    def setup(self):
        self.cleanup()

    def test_can_download_file_http_fille_present(self):
        githubdl.dl_file(self.test_repo_url_http, self.single_file_name)
        assert self.is_single_file_present() == True

    def test_can_download_file_http_file_size_non_zero(self):
        githubdl.dl_file(self.test_repo_url_http, self.single_file_name)
        assert self.is_single_file_nonzero() == True

    def test_can_download_file_http_by_sha_reference_file_present(self):
        githubdl.dl_file(self.test_repo_url_http, self.single_file_name, reference="bfef53")
        assert self.is_single_file_present() == True

    def test_can_download_file_http_by_tag_reference_file_present(self):
        githubdl.dl_file(self.test_repo_url_http, self.single_file_name, reference="read_working")
        assert self.is_single_file_present() == True

    def test_can_download_file_http_by_sha_reference_file_size_non_zero(self):
        githubdl.dl_file(self.test_repo_url_http, self.single_file_name, reference="bfef53")
        assert self.is_single_file_nonzero() == True

    def test_can_download_file_http_by_tag_reference_file_size_non_zero(self):
        githubdl.dl_file(self.test_repo_url_http, self.single_file_name, reference="read_working")
        assert self.is_single_file_nonzero() == True

    def test_can_download_single_directory_http(self):
        githubdl.dl_dir(self.test_repo_url_http, self.single_dir_name)
        assert self.is_single_dir_present() == True

    def test_can_download_file_ssh(self):
        githubdl.dl_file(self.test_repo_url_ssh, self.single_file_name)
        assert self.is_single_file_present() == True

    def test_can_download_single_directory_ssh(self):
        githubdl.dl_dir(self.test_repo_url_ssh, self.single_dir_name)
        assert self.is_single_dir_present() == True

