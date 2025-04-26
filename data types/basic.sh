# this is a practice file.

#!/usr/bin/bash

mkdir my_project
cd my_project
mkdir content
mkdir -p my_dir/src

ls -a -lh 
pwd
rm -r content
ls -a
touch content.txt
echo "hello world!" > content1.txt
cat content1.txt

cp content1.txt content.txt
mv content1.txt content.txt

ln -s content.txt softlink_adit
ln content.txt hardlink_adit

mv content.txt ./my_dir/
