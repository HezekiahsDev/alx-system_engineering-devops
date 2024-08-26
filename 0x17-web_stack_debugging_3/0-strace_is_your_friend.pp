# Fix file extension error (*.phpp) in file `wp-settings.php`.

exec { 'fix-filename':
  command => 'sed -i s/phpp/php/g /var/www/html/wp-settings.php',
  path    => '/usr/local/bin/:/bin/'
}
