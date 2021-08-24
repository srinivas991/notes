<?php
$var = '1234;ping 10.10.14.19';
$output = exec("python3 /home/kali/notes/htb/previse/test.py {$var}");
echo $output;
?>
