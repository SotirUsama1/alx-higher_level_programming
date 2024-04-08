#!/bin/bash
echo 'file name: '
read x
touch ${PWD}/$x
# echo -e "#!/bin/bash\n" > ./$x
vi $x
chmod a+x $x