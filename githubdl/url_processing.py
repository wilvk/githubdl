import logging
from . import url_helpers as uh

def generate_repo_api_url(domain_name, repo_name, file_name, reference, api_path):
    if domain_name.lower() == "github.com":
        return generate_github_api_url(repo_name, file_name, reference, api_path)
    return generate_private_repo_api_url(domain_name, repo_name, file_name, reference, api_path)

def get_components_for_url_protocol(is_ssh, is_http, repo_url):
    if is_ssh:
        domain_name = uh.get_domain_name_from_ssh_url(repo_url)
        repo_name = uh.get_repo_name_from_ssh_url(repo_url)
    elif is_http:
        domain_name = uh.get_domain_name_from_http_url(repo_url)
        repo_name = uh.get_repo_name_from_http_url(repo_url)
    return (domain_name, repo_name)

def get_url_components(repo_url):
    (is_ssh, is_http) = uh.check_url_protocol(repo_url)
    return get_components_for_url_protocol(is_ssh, is_http, repo_url)

def generate_ref_string(reference):
    if not reference:
        return reference
    return "?ref=" + reference

def generate_request_string(file_name, reference):
    reference = generate_ref_string(reference)
    if file_name != '' or reference != '':
        return '/' + file_name + reference
    return ''

def generate_github_api_url(repo_name, file_name, reference, api_path='contents'):
    request_string = generate_request_string(file_name, reference)
    logging.info("repo_name: " + repo_name + " api_path: " + api_path + " request_string: " + request_string)
    return "https://api.github.com/repos/" + repo_name + "/" + api_path + request_string

def generate_private_repo_api_url(domain_name, repo_name, file_name, reference, api_path='contents'):
    request_string = generate_request_string(file_name, reference)
    return "https://" + domain_name + "/api/v3/repos/" + repo_name + "/" + api_path + request_string
