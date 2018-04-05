#!/bin/bash
svn_rev=$(GIT_EXEC_PATH=/usr/lib/git-core/ /usr/bin/git describe --match svn-r)
/bin/sed -e 's/\$Revision\$/$Revision: '$svn_rev'$/g' -
