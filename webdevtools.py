#!/usr/bin/python3
"""
 __        __   _       ____               _____           _
 \ \      / /__| |__   |  _ \  _____   __ |_   _|__   ___ | |___
  \ \ /\ / / _ \ '_ \  | | | |/ _ \ \ / /   | |/ _ \ / _ \| / __|
   \ V  V /  __/ |_) | | |_| |  __/\ V /    | | (_) | (_) | \__ \\
    \_/\_/ \___|_.__/  |____/ \___| \_/     |_|\___/ \___/|_|___/

  Power by: PHILIPPE ASSIS
  Oficial repository: https://github.com/PhilippeAssis/webdevtools
  Version: 1.0

 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
 $$                                                              $$
 $$ LICENSE                                                      $$
 $$                                                              $$
 $$ Copyright 2015 PHILIPPE ASSIS                                $$
 $$ Licensed under the Apache License,                           $$
 $$ Version 2.0 (the “License”);                                 $$
 $$ you may not use this file except in compliance with the      $$
 $$ License. You may obtain a copy of the License at             $$
 $$ http://www.apache.org/licenses/LICENSE-2.0                   $$
 $$                                                              $$
 $$ Unless required by applicable law or agreed to in writing,   $$
 $$ software distributed under the License is distributed on an  $$
 $$ “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, $$
 $$ either express or implied. See the License for the specific  $$
 $$ language governing permissions and limitations under the     $$
 $$ License.                                                     $$
 $$                                                              $$
 $$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$
"""
from optparse import OptionParser, os

parser = OptionParser()

parser.add_option("-r",help="Site: Remove site |Host: Removes the specified host",
                  default=False, action="store_true")
parser.add_option("-p", help="Port (Default 80)", default='80')
parser.add_option("-f", help="Forces the creation of directories if the specified path does not "
                                                 "exist", default=False, action="store_true")
parser.add_option("-i" ,help="IP for which the URL address should be directed to when the host is locally generated (Default 127.0.0.1)", default='127.0.0.1')
parser.add_option("-l", help="By declaring -l, will be created an entry in /etc/hosts to the current site",
                  default=False, action="store_true")

(options, args) = parser.parse_args()

params = ''

if args:
    for i,arg in enumerate(args):
        if i == 0:
            params = 'dev'+arg+' '
        else:
            params += arg+' '

print(options.values())
exit(0)

if options:
    for (key,item) in options.values():
        print(key)


print(params)
# os.system(params)

exit(0)