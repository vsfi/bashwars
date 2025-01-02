import csv
import random

headers = [
    "Name",
    "PowerState",
    "FolderPath",
    "Host",
    "Datacenter",
    "VMXPath",
    "CPUCores",
    "MemGB",
    "UsedSpaceGB",
    "DatastoreList",
    "NetworkAdapterCount",
    "IPAddressCount",
]
vms_prefixes = [
    "patroni-prod-",
    "patroni-dev-",
    "patroni-test-",
    "Workstation-",
    "test-esxi-70-",
    "test-esxi-80-",
    "test-esxi-67-",
    "bastion-",
    "Windows-2019-server",
    "Windows-10-",
    "Windows-server",
    "Nfs-share-",
    "ceph-reef-osd-node-",
    "ceph-quincy-osd-node-",
    "ceph-reef-mon-node-",
    "ceph-quincy-mon-node-",
    "ceph-reef-mgmt-node-",
    "ceph-quincy-mgmt-node-",
    "Mikrotick-CHR-",
    "pfSense-",
    "Ubuntu-",
    "New Virtual Machine-",
]
datastores = [
    "ceph-isci-ssh",
    "ceph-icsi-hdd",
    "lenovo-raid-10",
    "iscsi-hdd",
    "iscsi-ssd",
    "nfs-test-datastore",
    "local-ssd",
    "local-hdd",
]


datacenters = [
    "e-Style0Telecom",
    "Oxygen",
    "Mirea",
    "dataline",
    "Digital-Media-House",
    "Colocat",
    "M1",
    "DataPlanet",
]
possible_memory = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024]
possible_cpu = [1, 2, 4, 8, 16, 32]
big_vm_position = 2600 + random.randint(0, 9)
data = []
for i in range(1, 10000):
    datacenter = random.choice(datacenters)
    datastore = random.choice(datastores)
    vm_name = f"{random.choice(vms_prefixes)}{i}"
    power_state = random.choice(["PoweredOn", "PowerOff"])
    folder_path = f"/{datacenter}/virtual_machines"
    host = f"esxi-{random.randint(1,100)}-{datacenter}.vsfi.org"
    vmx_path = f"/vmfs/volumes/{datacenter}-{datastore}/{vm_name}/{vm_name}.vmx"

    cpu_cores = random.randint(1, 4)
    mem_gb = random.choice(possible_memory)
    used_space_gb = random.randint(10, 100)
    datastore_count = 1
    datastore_list = f"{datacenter}-{datastore}"
    network_adapter_count = random.randint(1, 4)
    ip_address_count = abs(network_adapter_count - 1)

    data.append(
        [
            vm_name,
            power_state,
            folder_path,
            host,
            datacenter,
            vmx_path,
            cpu_cores,
            mem_gb,
            used_space_gb,
            datastore_list,
            network_adapter_count,
            ip_address_count,
        ]
    )
    if i == 2600:  # right
        data.append(
            [
                "ceph-reef-osd-node-10",
                "PowerOn",
                "/Oxygen/virtual_machines",
                "esxi-40-Oxygen.vsfi.org",
                "Oxygen",
                "/vmfs/volumes/Oxygen-ceph-icsi-hdd/Nfs-share-7/Nfs-share-7.vmx",
                "64",
                "16",
                "96",
                "Oxygen-ceph-icsi-hdd",
                4,
                3,
            ]
        )
    if i == 1000:
        data.append(
            [
                "ceph-reef-osd-node-10",
                "PowerOn",
                "/dataline/virtual_machines",
                "esxi-20-dataline.vsfi.org",
                "dataline",
                "/vmfs/volumes/dataline-ceph-icsi-hdd/Nfs-share-7/Nfs-share-7.vmx",
                "64",
                "16",
                "96",
                "dataline-ceph-icsi-hdd",
                4,
                3,
            ]
        )
    if i == 400:
        data.append(
            [
                "ceph-reef-osd-node-10",
                "PowerOn",
                "/Colocat/virtual_machines",
                "esxi-71-Colocat.vsfi.org",
                "Colocat",
                "/vmfs/volumes/Colocat-ceph-icsi-hdd/Nfs-share-7/Nfs-share-7.vmx",
                "64",
                "16",
                "96",
                "Colocat-ceph-icsi-hdd",
                4,
                3,
            ]
        )
    if i == 2900:
        data.append(
            [
                "ceph-reef-osd-node-10",
                "PowerOn",
                "/M1/virtual_machines",
                "esxi-98-M1.vsfi.org",
                "M1",
                "/vmfs/volumes/M1-ceph-icsi-hdd/Nfs-share-7/Nfs-share-7.vmx",
                "64",
                "16",
                "96",
                "M1-ceph-icsi-hdd",
                4,
                3,
            ]
        )
with open("vms_export.csv", mode="w", newline="") as file:
    writer = csv.writer(file)
    writer.writerow(headers)
    writer.writerows(data)
