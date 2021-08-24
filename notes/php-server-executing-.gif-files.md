# php server executing .gif files

this is a rare scenario which I've encountered in a box which executes `php` in a `.gif` file due to a bad configuration in the Apache `httpd` configuration. in this case it executed `cmd.php.gif` which has the following content in it.

```text
<?php echo "123"; ?>
```

So, you have a web server on `httpd`, and the config file looks like this - `/etc/httpd/conf.d/php.conf`

```text
AddHandler php5-script .php
AddType text/html .php
```

it is due to this above config in the `php.conf` file, which is basically telling `apache2` to handle any file with a `.php` in its name as a `php` script. it should actually be something like

```text
<FilesMatch ".php$">
    AddHandler php5-script .php
    AddType text/html .php
</FilesMatch>
```

so that it specifies the match as **ending** with `.php`

