from diagrams import Cluster, Diagram
from diagrams.generic.network import VPN
from diagrams.generic.storage import Storage
from diagrams.onprem.compute import Server
from diagrams.onprem.container import Docker
from diagrams.onprem.iac import Ansible
from diagrams.onprem.network import Caddy
from diagrams.onprem.proxmox import Pve

with Diagram("Overview", filename="diagrams/overview", show=False, direction="TB"):
    source = Pve("pve")
    with Cluster("VMs"):
        storage = Storage("storage")
        docker = Docker("docker")
        ansible = Ansible("ansible")

    with Cluster("Containers"):
        containers = [
            VPN("wireguard"),
            Server("qbittorrent"),
            Server("plex"),
            Server("immich"),
            Server("firefox"),
            Caddy("caddy")
        ]
    source - storage
    source - docker
    source - ansible
    docker - containers