# -*- coding: utf-8 -*-
'''
    __init__.py
'''

from __future__ import print_function

import sys
import argparse
import logging

from .api import dl_file
from .api import dl_dir
from .api import dl_tags
from .api import dl_branches
from .api import get_repo_name_from_url
from .api import get_domain_name_from_url


def get_default_log_level(log_level):
    '''
        Defines the default log levels.
    '''
    if log_level == 'DEBUG':
        return logging.DEBUG
    if log_level == 'INFO':
        return logging.INFO
    if log_level == 'WARN':
        return logging.WARN
    if log_level == 'ERROR':
        return logging.ERROR
    if log_level == 'CRITICAL':
        return logging.CRITICAL
    print("Invalid log level specified. Defaulting to INFO")
    return logging.INFO


def set_log_level(args):
    '''
        Sets the log level based on the log_level arg
    '''
    if args['log_level'] != None:
        return get_default_log_level(args['log_level'])
    if args['tags'] or args['branches']:
        return logging.WARN
    return logging.INFO


def main():
    '''
       Main entrypoint for the cli application
    '''
    parser = argparse.ArgumentParser(
        description='Github Path Downloader. Download files and directories from Github easily. Works with Github and Github Enterprise.')
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument('-f', '--file', help='The name of the file to download.', required=False)
    group.add_argument('-d', '--dir', help='The name of the directory to download.', required=False)
    group.add_argument('-a', '--tags', help='A switch specifying that a list of tags is to be downloaded.', required=False, action='store_true')
    group.add_argument('-b', '--branches', help='A switch specifying that a list of branches is to be downloaded.', required=False, action='store_true')

    parser.add_argument('-u', '--url', help='The url of the repository to download.', required=True)
    parser.add_argument('-t', '--target', help='The name of the file or directory to save the data to. Defaults to file or directory name.', required=False)
    parser.add_argument('-g', '--git_token',
                        help='The value of the Github/Github Enterprise Token. Can also be specified in the environment variable `GIT_TOKEN`.', required=False)
    parser.add_argument('-l', '--log_level',
                        help='The level of logging to use for output. Valid options are: DEBUG, INFO, WARN, ERROR, CRITICAL. Defaults to INFO.', required=False)
    parser.add_argument('-r', '--reference', help='The name of the commit/branch/tag. Default: the repository’s default branch.', required=False)
    parser.add_argument('-s', '--submodules', help='A switch specifying that all submodules are to be downloaded.', required=False, action='store_true')

    args = vars(parser.parse_args())

    git_token = ''
    log_level = ''
    target = ''
    reference = ''

    if args['git_token'] != None:
        git_token = args['git_token']

    log_level = set_log_level(args)

    if args['target'] != None:
        target = args['target']

    if args['reference'] != None:
        reference = args['reference']

    if args['tags']:
        tags_json = dl_tags(repo_url=args['url'], github_token=git_token, log_level=log_level)
        sys.stdout.write(tags_json)
    elif args['branches']:
        branches_json = dl_branches(repo_url=args['url'], github_token=git_token, log_level=log_level)
        sys.stdout.write(branches_json)

    if args['file'] != None:
        dl_file(repo_url=args['url'], file_name=args['file'], target_filename=target, github_token=git_token, log_level=log_level, reference=reference)
    elif args['dir'] != None:
        dl_dir(repo_url=args['url'], base_path=args['dir'], target_path=target, github_token=git_token, log_level=log_level, reference=reference, submodules=args['submodules'])
