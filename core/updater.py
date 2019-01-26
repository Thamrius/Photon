import re
import os
from core.requester import requester
from core.colors import run, que, good, green, end, info

def updater():
    """Update the current installation.

    git clones the latest version and merges it with the current directory.
    """
    print('%s Checking for updates' % run)
    # Changes must be separated by ;
    changes = "cloning (mirroring) feature;fixed sitemap.xml parsing;reuse tcp connection to boost speed;handle redirect loops;csv export support;other minor bug fixes"
    latest_commit = requester('https://raw.githubusercontent.com/s0md3v/Photon/master/photon.py', host='github.com').text
    # Just a hack to see if a new version is available
    if changes not in latest_commit:
        changelog = re.search(r"changes = '''(.*?)'''", latest_commit)
        # Splitting the changes to form a list
        changelog = changelog.group(1).split(';')
        print('%s A new version of Photon is available.' % good)
        print('%s Changes:' % info)
        for change in changelog: # print changes
            print('%s>%s %s' % (green, end, change))

        current_path = os.getcwd().split('/') # if you know it, you know it
        folder = current_path[-1] # current directory name
        path = '/'.join(current_path) # current directory path
        choice = input('%s Would you like to update? [Y/n] ' % que).lower()

        if choice != 'n':
            print('%s Updating Photon' % run)
            os.system('git clone --quiet https://github.com/s0md3v/Photon %s'
                      % (folder))
            os.system('cp -r %s/%s/* %s && rm -r %s/%s/ 2>/dev/null'
                      % (path, folder, path, path, folder))
            print('%s Update successful!' % good)
    else:
        print('%s Photon is up to date!' % good)
