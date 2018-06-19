import requests
import json
import os
import logging
from . import url_processing as up

def get_github_token(github_token):
    try:
        if github_token == '':
            return os.environ["GIT_TOKEN"]
        return github_token
    except KeyError:
        logging.critical("Unable to find Github token either as a parameter or the in environment variable 'GIT_TOKEN'")
        exit()

def get_files_from_json(response_object):
    files = {}
    try:
        for item in response_object:
            files.update({ item.get("name"): item.get("type") })
        return files
    except AttributeError as e:
        logging.critical("Unable to retrieve list of files from response.\n Exception: " + str(e) + "\n Response: " + str(response_object))
        exit()

def get_list_of_files_in_path(repo_url, base_path, github_token, reference):
    github_token = get_github_token(github_token)
    logging.info("Retrieving a list of files for directory: " + base_path)
    response = download_git_file_content(repo_url, base_path, github_token, reference)
    response_object = json.loads(response.decode('utf-8'))
    return get_files_from_json(response_object)

def process_request(http_url, github_token):
    try:
        request = requests.get(http_url,
            headers= {
                "Authorization": "token " + github_token,
                "Accept": "application/vnd.github.v3.raw"
            })
        return request.content
    except requests.exceptions.RequestException as e:
        logging.error("Error requesting file. RequestException: " + str(e))

def download_git_file_content(repo_url, file_name, github_token, reference):
    github_token = get_github_token(github_token)
    (domain_name, repo_name) = up.get_url_components(repo_url)
    http_url = up.generate_repo_api_url(domain_name, repo_name, file_name, reference, 'contents')
    logging.info("Requesting file: " + file_name + " at url: " + http_url)
    return process_request(http_url, github_token)

def download_git_repo_info(repo_url, github_token, info_type):
    github_token = get_github_token(github_token)
    (domain_name, repo_name) = up.get_url_components(repo_url)
    http_url = up.generate_repo_api_url(domain_name, repo_name, '', '', info_type)
    logging.info("Requesting repository " + info_type + " at url: " + http_url)
    return process_request(http_url, github_token)