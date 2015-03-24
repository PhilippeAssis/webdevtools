#Web Dev Tools

##License
###Copyright 2015 PHILIPPE ASSIS
Licensed under the Apache License, Version 2.0 (the “License”); you may not use this file except in compliance with the License. You may obtain a copy of the License at [http://www.apache.org/licenses/LICENSE-2.0](http://www.apache.org/licenses/LICENSE-2.0)

Unless required by applicable law or agreed to in writing, software distributed under the License is distributed on an “AS IS” BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the License for the specific language governing permissions and limitations under the License.
  
  
##Installation.
1 - Unzip the package to a location of your choice (I nominate /opt/webdevtools).
    To decompress using the terminal use:
    
    $ sudo unzip webdevtools.zip -d /opt/webdevtools     

2 - Access the unzipped directory from the command line.
    
    $ cd /opt/webdevtools

3 - Type the following command:

    $ ./install

Wait for the installation and enjoy!

##Requires:
    Ubuntu 14.04 or higher
    Apache 2.4

##How to use:
###SITES
#####Creating a new site in Apache 2.4:

To create a conf in your apache 2, create a new directory for your project with the site name and add it to your local host, use:

    $ sudo devsite <site.url> -l

####Removing Site
To remove a website and you host, simply assing a
 
    $ sudo devsite <site.url> -r -l

If you want to remove the project directory also, use:

    $ sudo devsite <site.url> -r -l --path

If you want to manually point the way of the project root directory, you must assign the path in the second argument, like this:

    $ sudo devsite <site.url> <path>
    
You can assign '-l' at any time in your devsite command. It will cause your order also works with the local host using the automativamente devhost command.

To prevent the application manipulate the website directories, preventing them to be created if there are no, or removed, you must set the --auto option to 0

    $ sudo devsite  


###Using devsite without creating or removing directories


###HOSTS
####Creating a host
To create or modify a host type

    $ sudo devhost <site.url> <ip>

####Removing a host
To remove a host type

    $ sudo devhost <site.url> <ip> -r

For details on the parameter settings for each program Use '-h'

###Important!
The use of the root (sudo) may not be necessary if your user has permission to edit the contents of the following directories:

    /etc/apache2/site-avaliable
    
    /etc/hosts

In these directories, directory paths chosen for the sites should also be allowed to access, read and edit.

###Information about the parameters

####devsite
    <Site Url>* <directory path>
    -h, --help            Show this help message and exit
    -p PORT, --port=PORT  Port (Default 80) 
    -f, --force           Forces the creation of directories if the specified path does not exist
    -i IP, --ip=IP        IP for which the URL address should be directed to when the host is locally generated (Default 127.0.0.1)
    -l, --local           By declaring -l, will be created an entry in /etc/hosts to the current site
    -r, --remove          Remove site
    
    *required

####devhost
    <Site Url>* <Ip>
    -h, --help    Show this help message and exit
    -r, --remove  Removes the specified host
    
    *required


**Good job!**