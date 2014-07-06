Filterbuster
============

Egress filter mapping application with additional functionality.
Expanded from: https://www.trustedsec.com/files/egressbuster.zip

  [-] Prerequisites: ...

  It is required to utilize additional modules outside the standard library as follows. You can use
  `easy_install` if you so desire or download and install from source. Your choice.

  The application will perform some basic checks to help elimate issues later in the application

    """ required for graphing """
    Please install numpy with: `easy_install numpy`

    """ import configparser for user supplied configuration file """
    Please install ConfigParser with: `easy_install configparser`

    """ required for covert testing """
    Please install python DNS module with: `easy_install dnspython`

  Currently the application relies on iptables for port redirection to the servers listening port
  other solutions, utilize scapy to handle all packet manipulation

  [-] Commandline Usage: ...
  
    {Client}  term:$ python ./filterbuster.py client ( config.file ) ( no / yes )
    {Server}  term:$ python ./filterbuster.py server ( tcp/udp ) ( port ) ( no / yes )

  [-] Understanding the client: ....

  The client is configured via a ini file specified on the commandline. This file is parsed 
  and used within the applications logic to configure the scanning engine and load additional
  modules into the framework.
  
  [-] Client Configuration file: ...

  Below is a sample configuration file used by the application. As modules are introduced, this
  configuration file will obviously need expanding as required. The examples below expect some
  modification from the end user -

      [SectionOne]

        diagnostics: ( boolean )
        target: ( 127.0.0.1 / hostname / subdomain.domain.tla )
        types: ( connect )
        spoof: ( boolean )
        range: ( portlist.txt / 0-65535 )
        random: ( boolean )
        protocol: ( tcp / udp / icmp / etc / etc )
        consultant: ( your name )
        location: ( your location )
      
      [SectionTwo]
      
        sleep: ( static / random )
        nappy: ( number )
        dwell: ( number )
      
      [SectionThree]
      
        suppress: ( boolean )
        logging: ( boolean )
        logtype: ( txt / xml / csv / json )
        covert: ( boolean )

  [-] Understanding the server: ....
  
  The server is threaded, bound to a single port and listens on all interfaces meaning all attempted 
  communications on the IP stack will be redirected to the server and it will answer the attempted 
  communication if specific criteria are meet. If these conditions are not fulfilled the server will 
  append any received data to a Contaminated file which can be used as an Honeypot of sorts.

  The Contaminated files contents are constructed as follows:

      {"127.0.0.1": {
        "TCP":{
          "80":{
            "hexdump":"\x00\x01\x02",
            "binarydump":"000000000000000100000010",
            "ASCIIdump":"somedata",
            "rawdump":"somedata",
            "Count":"25"
          },
          "443":{
            "hexdump":"\xFF\xFF\xFF",
            "binarydump":"111111111111111111111111",
            "ASCIIdump":"somedata",
            "rawdump":"somedata",
            "Count":"100"              
          }
        }    
      }}
      
  There really is no actual configuration to the server other than commandline options. As the applications
  functionality expands this could change.
  
  [-] TODO list: ....

      MORE SCAPY
      Make "both" TCP/UDP scan module have 2 seperate list so TCP and UDP ports tested
        are not the same when using in random choice
      Gather PII sample data (images): [
          passports,
          social security cards,
          drivers license,
          license plates,
          birth certificates
      ]
      Server side logging ? very quesitonable
            Encrypt data at rest if this is to be offered
      Take IP/Hostname list (iterate list for targeting)
      IPv6 Support
      More protocol testing - smtp, etc etc
      More Covert / backchannel testing
        Modes:[
            SSH over HTTPTunnel,
            IP packet fileds,
            GRE
        ]
      Better Request handling
      FwKnop for remote administration
      IDS/IPS testing (sending known signatures)
        Modes:[
            silent,
            quiet,
            loud,
            OBVIOUS,
            OBNOXIOUS
        ]
        Send known shellcodes signatures
        Send known malware signatures
        Send known virus signatures
        Send known botnet signatures
        Send known buffer overflow signatures
        Send clear text Personal Identifiable Information (PII) signatures
          Modes:[
              clear text,
              rot13,
              md5,
              sha1-512,
              Web safe encoding,
              PSK
              SSL/TLS
          ]
        Send Clear text Payment Card Industry (PCI) signatures
          Modes:[
              clear text,
              rot13,
              md5,
              sha1-512,
              PSK,
              SSL/TLS
          ]
      Spoofing traffic to confuse investigators (Red Herring)
        Mode:[
            spoof live machine (DoS / race conditions),
            produce ficticious traffic (smokescreen),
            capture and replay (cause RST floods)
        ]
      Monitor and report activity on wire to identify other vectors of attack
      Covert tunnel proxy options (turn client into a socks proxy)
      Lockout watchdog (monitor for preconfigured port knock sequence)
        Functionality:[
            Flush iptables,
            Wait for 5 min for ssh connection,
            reconfigure iptables port redirection
        ]
      GUI interface for both server/ client
        Interface:[
            Its perfect the way it is ? (highly doubtful),
            QT GUI (kinda played around with it) ,
            Web Driven (im interested),
            Maybe all sounds good
        ]
      Bogus Data Generator module - Diagnostics and log generation testing
      Traceroute from inside out - w/ SVG image generation for reports ( scapy )
      Get NG FW or access to an environement with one ( physical or virtual )
      Learn more on the topic of:[
            HL7 iso v2.x and v3 specifications
      ]
      Implement specific test based on PCI
      Implement specific test based on HIPAA
      Log and encrypt data w/ email alerting:[
        send encrypted attachment via email server,
        log on disk and encrypt no smtp,
        silent - no logging (current configuration)
            except for Contamination logged data
      ]
      Stop myself from coding between ( 23:45 / 04:40 ) or at least dont commit
      
