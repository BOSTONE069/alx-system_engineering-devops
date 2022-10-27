**HTTPS SSL**

<p align="center">
 <img src="https://s3.amazonaws.com/intranet-projects-files/holbertonschool-sysadmin_devops/276/FlhGPEK.png">
</p>


* **World wide web**

[0-world_wide_web](0-world_wide_web)

Configure your domain zone so that the subdomain www points to your load-balancer IP (lb-01). Let’s also add other subdomains to make our life easier, and write a Bash script that will display information about subdomains.

Requirements:

* Add the subdomain www to your domain, point it to your lb-01 IP (your domain name might be configured with default subdomains, feel free to remove them)
* Add the subdomain lb-01 to your domain, point it to your lb-01 IP
* Add the subdomain web-01 to your domain, point it to your web-01 IP
* Add the subdomain web-02 to your domain, point it to your web-02 IP

* Your Bash script must accept 2 arguments:
1. domain:
* type: string
* what: domain name to audit
* mandatory: yes
2. subdomain:
* type: string
* what: specific subdomain to audit
* mandatory: no
* Output: The subdomain [SUB_DOMAIN] is a [RECORD_TYPE] record and points to [DESTINATION]
* When only the parameter domain is provided, display information for its subdomains www, lb-01, web-01 and web-02 - in this specific order
* When passing domain and subdomain parameters, display information for the specified subdomain
* Ignore shellcheck case SC2086
* Must use:
* awk
* at least one Bash function
* You do not need to handle edge cases such as:
* Empty parameters
* Nonexistent domain names
* Nonexistent subdomains
