import re
from urllib.parse import urlparse
import logging

def check_url_is_http(repo_url):
    predicate = re.compile('^https?://.*$')
    match = predicate.search(repo_url)
    return False if match is None else True

def check_url_is_ssh(repo_url):
    predicate = re.compile(r'^git\@.*\.git$')
    match = predicate.search(repo_url)
    return False if match is None else True

def get_domain_name_from_http_url(repo_url):
    site_object = urlparse(repo_url)
    return site_object.netloc

def get_repo_name_from_http_url(repo_url):
    site_object = urlparse(repo_url)
    parsed_string = re.sub(r'\.git$', '', site_object.path)
    if parsed_string[0] == '/':
        return parsed_string[1:]
    return parsed_string

def get_repo_name_from_ssh_url(repo_url):
    predicate = re.compile(r'(?<=\:)(.*)(?=\.)')
    match = predicate.search(repo_url)
    return match.group()

def get_domain_name_from_ssh_url(repo_url):
    predicate = re.compile(r'(?<=\@)(.*)(?=\:)')
    match = predicate.search(repo_url)
    return match.group()

def validate_protocol_exists(is_ssh, is_http):
    if not is_ssh and not is_http:
        err_message = "Error: repository url provided is not http(s) or ssh"
        logging.critical(err_message)
        raise RuntimeError(err_message)

def check_url_protocol(repo_url):
    is_ssh = check_url_is_ssh(repo_url)
    is_http = check_url_is_http(repo_url)
    validate_protocol_exists(is_ssh, is_http)
    return (is_ssh, is_http)
