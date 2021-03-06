# -*- coding: utf-8 -*-
"""(Re)create the RethinkDB configuration file conf/rethinkdb.conf.
Start with conf/rethinkdb.conf.template
then append additional configuration settings (lines).
"""

from __future__ import unicode_literals
import os
import os.path
import shutil
import argparse
from hostlist import public_dns_names

# Parse the command-line arguments
parser = argparse.ArgumentParser()
parser.add_argument("--bind-http-to-localhost",
                    help="should RethinkDB web interface be bound to localhost?",
                    required=True)
args = parser.parse_args()
bind_http_to_localhost = args.bind_http_to_localhost

print('bind_http_to_localhost = {}'.format(bind_http_to_localhost))

# cwd = current working directory
old_cwd = os.getcwd()
os.chdir('conf')
if os.path.isfile('rethinkdb.conf'):
    os.remove('rethinkdb.conf')

# Create the initial rethinkdb.conf using rethinkdb.conf.template
shutil.copy2('rethinkdb.conf.template', 'rethinkdb.conf')

# Append additional lines to rethinkdb.conf
with open('rethinkdb.conf', 'a') as f:
    f.write('## The host:port of a node that RethinkDB will connect to\n')
    for public_dns_name in public_dns_names:
        f.write('join=' + public_dns_name + ':29015\n')
    if bind_http_to_localhost:
        f.write('## Bind the web interface port to localhost\n')
        # 127.0.0.1 is the usual IP address for localhost
        f.write('bind-http=127.0.0.1\n')

os.chdir(old_cwd)

# Note: The original code by Andreas wrote a file with lines of the form
#       join=public_dns_name_0:29015
#       join=public_dns_name_1:29015
#       but it stopped about halfway through the list of public_dns_names
#       (publist). In principle, it's only strictly necessary to
#       have one join= line.
#       Maybe Andreas thought that more is better, but all is too much?
#       Below is Andreas' original code. -Troy
# lfile = open('add2dbconf', 'w')
# before = 'join='
# after = ':29015'
# lfile.write('## The host:port of a node that rethinkdb will connect to\n')
# for entry in range(0,int(len(publist)/2)):
#     lfile.write(before + publist[entry] + after + '\n')
