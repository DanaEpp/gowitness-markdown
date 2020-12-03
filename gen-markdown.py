#!/bin/env python3

import sys
import os
import glob
import re
import datetime
import time

def parse_domain(img_name):
    # Pattern is http-somedomain.com.png. We want to strip to somedomain.com
    start_pos = img_name.find("-")
    end_pos = len(img_name) - len(".png")
    domain = img_name[start_pos+1:end_pos]
    return domain

screenshot_dir = ""

# Check if we have a path arg. If not, use current working directory
if len(sys.argv) > 1:
    arg_dir = sys.argv[1]
    if os.path.isdir(arg_dir):
        screenshot_dir = arg_dir
    else:
        print( "Invalid dir. Using current dir")

output_file = os.path.join(screenshot_dir, "hosts.md") 

# Check if output file already exists
if os.path.exists(output_file):
    overwrite = input( "hosts.md already exists. Overwrite? [y/N] ")
    if overwrite.lower() != "y":
        sys.exit( "Aborting. User does not wish to overwrite existing hosts.md file.")
    else:
        os.remove(output_file) 

now = datetime.datetime.now()
timestamp = now.strftime("%B %d, %Y at %H:%M:%S")

f = open(output_file, "wt")

f.write( "# HOSTS\n\n")
f.write( f"Generated: {timestamp} {time.tzname[time.daylight]}\n\n")
    
for file in os.listdir(screenshot_dir):
    if file.endswith(".png"):
        f.write( "## " + parse_domain(file) + "\n" )
        f.write( "![](" + file + ")\n\n" )

f.close()
