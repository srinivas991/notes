# stuff to try

try webdav scan if its IIS - `davtest`

and if it doesn't allow uploading aspx or php (depends), try uploading shell.html and `move` the files from html to php / aspx

when you find interesting filenames in an SMB share, try `allinfo` on the file, you may find alternate data streams. `get "file.txt:ALTERNAMEDATASTREAMNAME"`
