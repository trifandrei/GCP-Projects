Load Balancing

HTTP(S) Load Balancing is a proxy-based  load balancer that enables you to run and scale your services behind a single external IP address. External HTTP(S) Load Balancing distributes HTTP and HTTPS traffic to backends hosted on a variety of Google Cloud platforms (such as Compute Engine, Google Kubernetes Engine (GKE), Cloud Storage), as well as external backends connected over the internet or via hybrid connectivity.

You can configure external HTTP(S) Load Balancing in the following modes:

External HTTP(S) load balancer. This is the external HTTP(S) load balancer that is regional in Standard Tier and global in Premium Tier. The external HTTP(S) load balancer is implemented on Google Front Ends (GFEs). GFEs are distributed globally and operate together using Google's global network and control plane.
Regional external HTTP(S) load balancer. This is a regional load balancer that is implemented as a managed service on the open-source Envoy proxy. It includes advanced traffic management capabilities such as traffic mirroring, weight-based traffic splitting, request/response-based header transformations.

DNS

The Domain Name System (DNS) is the phonebook of the Internet. Humans access information online through domain names, like nytimes.com or espn.com. Web browsers interact through Internet Protocol (IP) addresses. DNS translates domain names to IP addresses so browsers can load Internet resources.
Each device connected to the Internet has a unique IP address which other machines use to find the device. DNS servers eliminate the need for humans to memorize IP addresses.
The process of DNS resolution involves converting a hostname (www.example.com) into a computer-friendly IP address (192.168.1.1). An IP address is given to each device on the Internet, and that address is necessary to find the appropriate Internet device - like a street address is used to find a particular home. When a user wants to load a webpage, a translation must occur between what a user types into their web browser (example.com) and the machine-friendly address necessary to locate the example.com webpage.
