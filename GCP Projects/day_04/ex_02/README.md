Cloud CDN (Content Delivery Network) uses Google's global edge network to serve content closer to users, which accelerates your websites and applications.
Cloud CDN works with external HTTP(S) Load Balancing to deliver content to your users. The external HTTP(S) load balancer provides the frontend IP addresses and ports that receive requests and the backends that respond to the requests.
When a user requests content from an external HTTP(S) load balancer, the request arrives at a Google Front End (GFE), which is at the edge of Google network as close as possible to the user.
If the load balancer URL map routes traffic to a backend service or backend bucket that has Cloud CDN configured, the GFE uses Cloud CDN.

Features:

With edge caches peered with nearly every major end-user ISP globally, Cloud CDN offers connectivity to more users everywhere. Thanks to anycast architecture, A site gets a single global IP address, combining consistent performance worldwide with easy management.

Cloud CDN enables customers to deliver content hosted on-premises or in another cloud over Google’s high-performance distributed edge caching infrastructure.

Serve responses from  globally distributed caches, even when you need requests to be authorized on a per-user basis.
