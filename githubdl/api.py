'''
    api.py module - exposed methods for the githubdl library
'''
import os
import logging
import sys
import re
from . import request_processing as rp
from . import file_processing as fp
from . import url_processing as up

def set_default_if_empty(variable_to_check, default_value):
    if not variable_to_check:
        return default_value
    return variable_to_check

def set_logging(log_level):
    log_level = set_default_if_empty(log_level, logging.INFO)
    logging.basicConfig(stream=sys.stdout, level=log_level, format='%(asctime)s - %(name)-12s - %(levelname)-8s - %(message)s')

def save_file_to_path(repo_url, download_filename, target_path, github_token, reference):
    download_file = rp.download_git_file_content(repo_url, download_filename, github_token, reference)
    full_file_name = fp.get_target_full_filename(download_filename, target_path)
    full_dir_name, base_name = os.path.split(full_file_name)
    fp.create_directory(full_dir_name)
    fp.write_file(full_file_name, download_file)

def dl_info(repo_url, github_token, log_level, info_type):
    set_logging(log_level)
    tags = rp.download_git_repo_info(repo_url, github_token, info_type)
    return tags.decode("utf-8")

'''
Exposed api methods below:
'''
def dl_file(repo_url, file_name, target_filename='', github_token='', log_level='', reference=''):
    set_logging(log_level)
    target_filename = set_default_if_empty(target_filename, file_name)
    file_data = rp.download_git_file_content(repo_url, file_name, github_token, reference)
    fp.write_file(target_filename, file_data)

def dl_dir(repo_url, base_path, target_path='', github_token='', log_level='', reference='', submodules=''):
    set_logging(log_level)
    target_path = set_default_if_empty(target_path, base_path)
    files = rp.get_list_of_files_in_path(repo_url, base_path, github_token, reference)
    for file_item, file_type in files.items():
        if file_type == "dir":
            recurse_dir = os.path.join(base_path, file_item)
            dl_dir(repo_url, recurse_dir, target_path, github_token)
        else:
            download_filename = os.path.join(base_path, file_item)
            save_file_to_path(repo_url, download_filename, target_path, github_token, reference)
            if file_item.lower().endswith('.gitmodules') and submodules:
                full_filename = fp.get_target_full_filename(download_filename, target_path)
                process_gitmodule(github_token, base_path, file_item, target_path, full_filename)

def process_gitmodule(github_token, base_path, file_item, target_path, full_filename):
    with open(full_filename) as f:
        content = f.readlines()
    content = [x.strip() for x in content]
    path = None
    url = None
    path_pred = re.compile(r'^\s*path\s*=\s*(.*)$')
    url_pred = re.compile(r'^\s*url\s*=\s*(.*)$')
    for line in content:
        if not path:
            path = path_pred.search(line)
        if not url:
            url = url_pred.search(line)
        if path and url:
            tmp_path = os.path.join(target_path, path.group(1))
            tmp_url = url.group(1)
            path = url = None
            fp.create_directory(tmp_path)
            dl_dir(repo_url=tmp_url, base_path="/", target_path=tmp_path, github_token=github_token, submodules=True)

def dl_tags(repo_url, github_token='', log_level=''):
    return dl_info(repo_url, github_token, log_level, 'tags')

def dl_branches(repo_url, github_token='', log_level=''):
    return dl_info(repo_url, github_token, log_level, 'branches')

def get_repo_name_from_url(repo_url):
    (domain_name, repo_name) = up.get_url_components(repo_url)
    return repo_name

def get_domain_name_from_url(repo_url):
    (domain_name, repo_name) = up.get_url_components(repo_url)
    return domain_name
