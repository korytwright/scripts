#The purpose in obtaining this code is to completely understand the logic through reverse engineering 

!/usr/bin/env python
#
# Script Name:
# Description:
# Deploy To:
# Commit To:

import platform
import os
import re
import socket
import subprocess
import smtplib
import sys
from email.mime.text import MIMEText
from optparse import OptionParser

################################### GLOBALS ###################################

# Path to NRPE binary
CHECK_NRPE = '/usr/lib64/nagios/plugins/check_nrpe'


FLOW_CONFIG = {
    'VMSP-VAIL': {
        '10.71.248.32': {
            '172.24.19.77': (162,),
            '172.24.19.96': (22,),
            '172.24.19.97': (22,),
            '172.24.19.98': (22,),
            '172.24.19.99': (22,),
        },
        '10.71.248.33': {
            '172.24.19.77': (162,),
            '172.24.19.96': (22,),
            '172.24.19.97': (22,),
            '172.24.19.98': (22,),
            '172.24.19.99': (22,),
        },
        '10.71.248.34': {
            '172.24.19.77': (162,),
            '172.24.19.96': (22,),
            '172.24.19.97': (22,),
            '172.24.19.98': (22,),
            '172.24.19.99': (22,),
        },
        '10.71.248.66': {
            '172.24.19.64': (53,),
            '172.24.19.65': (123,),
            '172.24.19.77': (162,),
        },
        '10.71.248.82': {
            '172.24.19.64': (53,),
            '172.24.19.65': (123,),
            '172.24.19.77': (162,),
        },
        '10.71.248.69': {
  '172.24.19.64': (22,),
            '172.24.19.77': (162,),
        },
        '10.71.248.85': {
            '172.24.19.64': (22,),
            '172.24.19.77': (162,),
        },
        '10.71.248.8': {
            '172.24.19.71': (22,),
            '172.24.19.72': (22,),
            '172.24.19.73': (22,),
            '172.24.19.74': (22,),
            '172.24.19.77': (162,),
        },
        '10.71.248.9': {
            '172.24.19.71': (22,),
            '172.24.19.72': (22,),
            '172.24.19.73': (22,),
            '172.24.19.74': (22,),
            '172.24.19.77': (162,),
        },
        '10.71.248.72': {
            '172.24.19.75': (4730,),
            '172.24.19.77': (162,),
        },
        '10.71.248.73': {
            '172.24.19.77': (162,),
        },
        '10.71.248.88': {
            '172.24.19.75': (4730,),
            '172.24.19.77': (162,),
        },
        '10.71.248.68': {
            '172.24.19.77': (162,),
            '172.24.19.78': (1514,),
            '172.24.19.79': (1514,),
        },
        '10.71.248.84': {
            '172.24.19.77': (162,),
            '172.24.19.78': (1514,),
            '172.24.19.79': (1514,),
        },
        '10.71.248.67': {
            '172.24.19.77': (162,),
            '172.24.19.80': (6514,),
        },
        '10.71.248.83': {
            '172.24.19.77': (162,),
            '172.24.19.80': (6514,),
        },
        '10.71.248.70': {
            '172.24.19.77': (162,),
            '172.24.19.82': (443,),
        },
'10.71.248.86': {
            '172.24.19.77': (162,),
            '172.24.19.82': (443,),
        },
        '10.87.248.32': {
            '172.25.19.77': (162,),
            '172.25.19.96': (22,),
            '172.25.19.97': (22,),
            '172.25.19.98': (22,),
            '172.25.19.99': (22,),
        },
        '10.87.248.33': {
            '172.25.19.77': (162,),
            '172.25.19.96': (22,),
            '172.25.19.97': (22,),
            '172.25.19.98': (22,),
            '172.25.19.99': (22,),
        },
        '10.87.248.34': {
            '172.25.19.77': (162,),
            '172.25.19.96': (22,),
            '172.25.19.97': (22,),
            '172.25.19.98': (22,),
            '172.25.19.99': (22,),
        },
        '10.87.248.66': {
            '172.25.19.64': (53,),
            '172.25.19.65': (123,),
            '172.25.19.77': (162,),
        },
        '10.87.248.82': {
            '172.25.19.64': (53,),
            '172.25.19.65': (123,),
            '172.25.19.77': (162,),
        },
        '10.87.248.69': {
            '172.25.19.64': (22,),
            '172.25.19.77': (162,),
        },
        '10.87.248.85': {
            '172.25.19.64': (22,),
            '172.25.19.77': (162,),
        },
        '10.87.248.8': {
            '172.25.19.71': (22,),
            '172.25.19.72': (22,),
            '172.25.19.73': (22,),
            '172.25.19.74': (22,),
            '172.25.19.77': (162,),
        },
        '10.87.248.9': {
            '172.25.19.71': (22,),
 '172.25.19.72': (22,),
            '172.25.19.73': (22,),
            '172.25.19.74': (22,),
            '172.25.19.77': (162,),
        },
        '10.87.248.72': {
            '172.25.19.75': (4730,),
            '172.25.19.77': (162,),
        },
        '10.87.248.73': {
            '172.25.19.77': (162,),
        },
        '10.87.248.88': {
            '172.25.19.75': (4730,),
            '172.25.19.77': (162,),
        },
        '10.87.248.68': {
            '172.25.19.77': (162,),
            '172.25.19.78': (1514,),
            '172.25.19.79': (1514,),
        },
        '10.87.248.84': {
            '172.25.19.77': (162,),
            '172.25.19.78': (1514,),
            '172.25.19.79': (1514,),
        },
        '10.87.248.67': {
            '172.25.19.77': (162,),
            '172.25.19.80': (6514,),
        },
        '10.87.248.83': {
            '172.25.19.77': (162,),
            '172.25.19.80': (6514,),
        },
        '10.87.248.70': {
            '172.25.19.77': (162,),
            '172.25.19.82': (443,),
        },
        '10.87.248.86': {
            '172.25.19.77': (162,),
            '172.25.19.82': (443,),
        },
    },
    'DALLAS-VAIL': {
        '10.71.248.32': {
            '172.24.19.77': (162,),
            '172.24.19.94': (8834,),
            '172.24.19.96': (22,),
            '172.24.19.97': (22,),
            '172.24.19.98': (22,),
            '172.24.19.99': (22,),
        },
        '10.71.248.33': {
            '172.24.19.77': (162,),
'172.24.19.94': (8834,),
            '172.24.19.96': (22,),
            '172.24.19.97': (22,),
            '172.24.19.98': (22,),
            '172.24.19.99': (22,),
        },
        '10.71.248.34': {
            '172.24.19.77': (162,),
            '172.24.19.94': (8834,),
            '172.24.19.96': (22,),
            '172.24.19.97': (22,),
            '172.24.19.98': (22,),
            '172.24.19.99': (22,),
        },
        '10.71.248.66': {
            '172.24.19.64': (53,),
            '172.24.19.65': (123,),
            '172.24.19.77': (162,),
            '172.24.19.94': (8834,),
        },
        '10.71.248.82': {
            '172.24.19.64': (53,),
            '172.24.19.65': (123,),
            '172.24.19.77': (162,),
            '172.24.19.94': (8834,),
        },
        '10.71.248.69': {
            '172.24.19.64': (22,),
            '172.24.19.77': (162,),
            '172.24.19.94': (8834,),
        },
        '10.71.248.85': {
            '172.24.19.64': (22,),
            '172.24.19.77': (162,),
            '172.24.19.94': (8834,),
        },
        '10.71.248.8': {
            '172.24.19.71': (22,),
            '172.24.19.72': (22,),
            '172.24.19.73': (22,),
            '172.24.19.74': (22,),
            '172.24.19.77': (162,),
            '172.24.19.94': (8834,),
        },
        '10.71.248.9': {
            '172.24.19.71': (22,),
            '172.24.19.72': (22,),
            '172.24.19.73': (22,),
            '172.24.19.74': (22,),
            '172.24.19.77': (162,),
            '172.24.19.94': (8834,),
        },
        '10.71.248.72': {
            '172.24.19.75': (4730,),

 '172.24.19.77': (162,),
            '172.24.19.94': (8834,),
        },
        '10.71.248.73': {
            '172.24.19.77': (162,),
            '172.24.19.94': (8834,),
        },
        '10.71.248.88': {
            '172.24.19.75': (4730,),
            '172.24.19.77': (162,),
            '172.24.19.94': (8834,),
        },
        '10.71.248.68': {
            '172.24.19.77': (162,),
            '172.24.19.78': (1514,),
            '172.24.19.79': (1514,),
            '172.24.19.94': (8834,),
        },
        '10.71.248.84': {
            '172.24.19.77': (162,),
            '172.24.19.78': (1514,),
            '172.24.19.79': (1514,),
            '172.24.19.94': (8834,),
        },
        '10.71.248.67': {
            '172.24.19.77': (162,),
            '172.24.19.80': (6514,),
            '172.24.19.94': (8834,),
        },
        '10.71.248.83': {
            '172.24.19.77': (162,),
            '172.24.19.80': (6514,),
            '172.24.19.94': (8834,),
        },
        '10.71.248.70': {
            '172.24.19.77': (162,),
            '172.24.19.82': (443,),
            '172.24.19.94': (8834,),
        },
        '10.71.248.86': {
            '172.24.19.77': (162,),
            '172.24.19.82': (443,),
            '172.24.19.94': (8834,),
        },
    },
    'PHOENIX-VAIL': {
        '10.87.248.32': {
            '172.25.19.77': (162,),
            '172.25.19.94': (8834,),
            '172.25.19.96': (22,),
            '172.25.19.97': (22,),
            '172.25.19.98': (22,),
            '172.25.19.99': (22,),
        },
 '10.87.248.33': {
            '172.25.19.77': (162,),
            '172.25.19.94': (8834,),
            '172.25.19.96': (22,),
            '172.25.19.97': (22,),
            '172.25.19.98': (22,),
            '172.25.19.99': (22,),
        },
        '10.87.248.34': {
            '172.25.19.77': (162,),
            '172.25.19.94': (8834,),
            '172.25.19.96': (22,),
            '172.25.19.97': (22,),
            '172.25.19.98': (22,),
            '172.25.19.99': (22,),
        },
        '10.87.248.66': {
            '172.25.19.64': (53,),
            '172.25.19.65': (123,),
            '172.25.19.77': (162,),
            '172.25.19.94': (8834,),
        },
        '10.87.248.82': {
            '172.25.19.64': (53,),
            '172.25.19.65': (123,),
            '172.25.19.77': (162,),
            '172.25.19.94': (8834,),
        },
        '10.87.248.69': {
            '172.25.19.64': (22,),
            '172.25.19.77': (162,),
            '172.25.19.94': (8834,),
        },
        '10.87.248.85': {
            '172.25.19.64': (22,),
            '172.25.19.77': (162,),
            '172.25.19.94': (8834,),
        },
        '10.87.248.8': {
            '172.25.19.71': (22,),
            '172.25.19.72': (22,),
            '172.25.19.73': (22,),
            '172.25.19.74': (22,),
            '172.25.19.77': (162,),
            '172.25.19.94': (8834,),
        },
        '10.87.248.9': {
            '172.25.19.71': (22,),
            '172.25.19.72': (22,),
            '172.25.19.73': (22,),
            '172.25.19.74': (22,),
            '172.25.19.77': (162,),
            '172.25.19.94': (8834,),
        },
 '10.87.248.72': {
            '172.25.19.75': (4730,),
            '172.25.19.77': (162,),
            '172.25.19.94': (8834,),
        },
        '10.87.248.73': {
            '172.25.19.77': (162,),
            '172.25.19.94': (8834,),
        },
        '10.87.248.88': {
            '172.25.19.75': (4730,),
            '172.25.19.77': (162,),
            '172.25.19.94': (8834,),
        },
        '10.87.248.68': {
            '172.25.19.77': (162,),
            '172.25.19.78': (1514,),
            '172.25.19.79': (1514,),
            '172.25.19.94': (8834,),
        },
        '10.87.248.84': {
            '172.25.19.77': (162,),
            '172.25.19.78': (1514,),
            '172.25.19.79': (1514,),
            '172.25.19.94': (8834,),
        },
        '10.87.248.67': {
            '172.25.19.77': (162,),
            '172.25.19.80': (6514,),
            '172.25.19.94': (8834,),
        },
        '10.87.248.83': {
            '172.25.19.77': (162,),
            '172.25.19.80': (6514,),
            '172.25.19.94': (8834,),
        },
        '10.87.248.70': {
            '172.25.19.77': (162,),
            '172.25.19.82': (443,),
            '172.25.19.94': (8834,),
        },
        '10.87.248.86': {
            '172.25.19.77': (162,),
            '172.25.19.82': (443,),
            '172.25.19.94': (8834,),
        },
    },
}
########################## PARSE COMMAND-LINE INPUT ###########################

usage = '%prog'
desc = '''Tests various traffic flows.'''

parser = OptionParser(usage=usage, description=desc)
parser.add_option('-d', '--debug', action="store_true",
                  dest='debug', default=False,
                  help='Print out debug info without running any actual tests')
parser.add_option('-f', '--flow', dest='flow',
                  help='Name of flow to test')
parser.add_option('-l', '--list', action="store_true",
                  dest='list', default=False,
                  help='Print out list of flows')
parser.add_option('-t', '--timeout', dest='timeout',
                  type=int, default=1,
                  help='Set timeout for connections')

OPTS, ARGS = parser.parse_args()

################################# SUB ROUTINES ################################

def print_config(flow_config):
    '''
    Print out list of all possible traffic flows

    Args: flow_config - Config with agailable flows

    Return: formatted text of all flows
    '''

    # Flow str
    flows = ''

    # Compile sites and groups strings
    for flow in FLOW_CONFIG:
        flows = '{0}{1}\n'.format(flows, flow)

    return flows[:-1]


def check_params (params, flow_config):
    '''
    Checks command line parameters for validity

    Args: params - Dictionary of command line parameters 
          flow_config - Config with agailable flows

    Return: err_msg - error message
    '''

    # Initialize error message
    err_msg = ''

# Run checks on params
    if not params.flow:
        err_msg = 'Flow - Must supply a flow'
    elif params.flow and (params.flow not in flow_config):
        err_msg = 'Flow {0} is not a valid flow'.format(params.flow)

    return err_msg


def run_tests (flow_config, flow, debug, timeout):
    '''
    Runs flow tests and compiles dictionary of results
    
    Args: flow_config - Config with agailable flows
          flow - Name of flow to run
          debug - Check variable for debug mode
          timeout - Timeout for check_nrpe command

    Return: test_results - a dictionary containing output results for
                           all connections within connections dict
            Dict format: {'flow_name': {'host': {results}}}
    '''

    def test_connect (host, remote_ip, port, timeout):
        '''
        Create socket and test connection to specified host and port

        Args: host - Host to ssh into and test traffic flow from
              remote_ip - IP of remote server to test traffic flow to from host
              port - Port of remote service to test traffic flow on

        Return: results - a dictionary containing output results from nrpe command
                Dict format: {'output': []}
        '''

        # Results dictionary containing both output and errors
        results = {
            'host': host,
            'output': [],
        }

        # Run tests and compile result
        # Build nrpe command
        nrpe_command = '{check_nrpe} -H {host} -c check_traffic_flow -a {remote_ip} {port} {timeout}'.format(
                                                      check_nrpe=CHECK_NRPE,
                                                      host=host,
                                                      remote_ip=remote_ip,
                                                      port=port,
                                                      timeout=timeout)

        # Check for debug mode
        if not debug:
            try:
                # Run nrpe command to get connection results
 subproc = subprocess.Popen(nrpe_command.split(' '), stdout=subprocess.PIPE,
                                                                    stderr=subprocess.PIPE)
                out, err = subproc.communicate()
            except Exception as e:
                print 'Could not issue nrpe command {0} - {1}'.format(nrpe_command, e)
            else:
                # Add standard output to results
                if out:
                    # Only append non empty lines
                    results['output'] = results['output'] + [x for x in out.split(
                                                                           '\n') if x]
                if err:
                    print 'Could not issue nrpe command {0} - {1}'.format(nrpe_command, err)
        else:
            results['output'].append(nrpe_command)

        return results


    # Dictionary holding all results
    test_results = []

    # Run tests
    for source in flow_config[flow]:
        for destination in flow_config[flow][source]:
            for port in flow_config[flow][source][destination]:
                test_results.append(test_connect(
                                    host=source,
                                    remote_ip=destination,
                                    port=port,
                                    timeout=timeout))


    return test_results


def compile_report (test_results, flow, debug):
    '''
    Compiles report of test results
    
    Args: test_results - dictionary results from flow tests
          debug - Check variable for debug mode
          flow - Name of flow 

    Return: report - formatted report of test results
    '''

    # Report string
    report = '{hf}\n{flow}\n{hf}\n'.format(flow=flow,
                                         hf='-'*(len(flow)+3))

    # Run through results and compile report
    for test in test_results:
        host = test['host']

   # Construct pas/fail output for host
        for output in test['output']:
            report = '{0}{1}: {2}\n'.format(report,host,output)

    return report


################################# MAIN ROUTINE ################################

# Print out all possible flows and exit if list param given
if OPTS.list:
    print print_config(FLOW_CONFIG)
    sys.exit(1)

# Check if nrpe binary exists and is executable by user
if not os.access(CHECK_NRPE, os.R_OK):
    print 'Cannot read CHECK_NRPE binary: {0}'.format(CHECK_NRPE)
    sys.exit(1)

# Check for command line parameter errors
err_msg = check_params(OPTS, FLOW_CONFIG)

if err_msg:
    print err_msg
    sys.exit(1)

# Run tests and compile results
test_results = run_tests(FLOW_CONFIG, OPTS.flow, OPTS.debug, OPTS.timeout)

# Compile report of test results
report = compile_report(test_results, OPTS.flow, OPTS.debug)

# Print out report
print report

sys.exit(0)


