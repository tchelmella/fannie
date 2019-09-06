import subprocess

# if the script don't need output.
subprocess.call("php /var/www/cgi-bin/fsearch.php")

# if you want output
proc = subprocess.Popen("php /var/www/cgi-bin/fsearch2.py", shell=True, stdout=subprocess.PIPE)
script_response = proc.stdout.read()
