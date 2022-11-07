# This is UFW, Firewall Configuration

<p>
   <img src="V1HjQ1Y.png">
</p>

1. Block all incoming traffic but

[Firewal configuration commands](0-block_all_incoming_traffic_but)

Let’s install the ufw firewall and setup a few rules on web-01.

Requirements:

1. The requirements below must be applied to web-01 (feel free to do it on lb-01 and web-02, but it won’t be checked)
2. Configure ufw so that it blocks all incoming traffic, except the following TCP ports:
* 22 (SSH)
* 443 (HTTPS SSL)
* 80 (HTTP)
3. Share the ufw commands that you used in your answer file