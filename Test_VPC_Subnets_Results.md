# Output of my VPC's

- Run the script in the terminal
```sh
python list_vpc.py 
```
- Output of the vpc from aws-region=eu-central-1
```sh
[$] <git:(main)> python list_vpc.py
2022-10-07 13:14:48,985: INFO: Found credentials in shared credentials file: ~/.aws/credentials
2022-10-07 13:14:49,471: INFO: VPC Details: 
2022-10-07 13:14:49,471: INFO: {
    "CidrBlock": "192.168.0.0/16",
    "DhcpOptionsId": "dopt-08d1973c06e0c3f031",
    "State": "available",
    "VpcId": "vpc-0d2022c4752b36f73",
    "OwnerId": "123456789012",
    "InstanceTenancy": "default",
    "CidrBlockAssociationSet": [
        {
            "AssociationId": "vpc-cidr-assoc-044f12081937ca833",
            "CidrBlock": "192.168.0.0/16",
            "CidrBlockState": {
                "State": "associated"
            }
        }
    ],
    "IsDefault": false,
    "Tags": [
        {
            "Key": "Name",
            "Value": "ta-labs-vpc"
        }
    ]
}
```
# Output of my subnets

- Run the script in the terminal:
```sh
python list_vpc.py 
```
- Output of the subnets from aws-region=eu-central-1

```sh
2022-10-07 14:40:15,957: INFO: Found credentials in shared credentials file: ~/.aws/credentials
2022-10-07 14:40:16,330: INFO: Subnet Details: 
2022-10-07 14:40:16,330: INFO: {
    "AvailabilityZone": "eu-central-1b",
    "AvailabilityZoneId": "euc1-az3",
    "AvailableIpAddressCount": 251,
    "CidrBlock": "192.168.2.0/24",
    "DefaultForAz": false,
    "MapPublicIpOnLaunch": false,
    "MapCustomerOwnedIpOnLaunch": false,
    "State": "available",
    "SubnetId": "subnet-0f7e3be0bbf061973",
    "VpcId": "vpc-0d2022c4752b36f73",
    "OwnerId": "123456789012",
    "AssignIpv6AddressOnCreation": false,
    "Ipv6CidrBlockAssociationSet": [],
    "Tags": [
        {
            "Key": "Name",
            "Value": "ta-subnet-public2-1b"
        }
    ],
    "SubnetArn": "arn:aws:ec2:eu-central-1:123456789012:subnet/subnet-0f7e3be0bbf061973",
    "EnableDns64": false,
    "Ipv6Native": false,
    "PrivateDnsNameOptionsOnLaunch": {
        "HostnameType": "ip-name",
        "EnableResourceNameDnsARecord": false,
        "EnableResourceNameDnsAAAARecord": false
    }
}

2022-10-07 14:40:16,331: INFO: {
    "AvailabilityZone": "eu-central-1b",
    "AvailabilityZoneId": "euc1-az3",
    "AvailableIpAddressCount": 251,
    "CidrBlock": "192.168.12.0/24",
    "DefaultForAz": false,
    "MapPublicIpOnLaunch": false,
    "MapCustomerOwnedIpOnLaunch": false,
    "State": "available",
    "SubnetId": "subnet-0170204db387fd0e9",
    "VpcId": "vpc-0d2022c4752b36f73",
    "OwnerId": "123456789012",
    "AssignIpv6AddressOnCreation": false,
    "Ipv6CidrBlockAssociationSet": [],
    "Tags": [
        {
            "Key": "Name",
            "Value": "ta-subnet-private2-1b"
        }
    ],
    "SubnetArn": "arn:aws:ec2:eu-central-1:123456789012:subnet/subnet-0170204db387fd0e9",
    "EnableDns64": false,
    "Ipv6Native": false,
    "PrivateDnsNameOptionsOnLaunch": {
        "HostnameType": "ip-name",
        "EnableResourceNameDnsARecord": false,
        "EnableResourceNameDnsAAAARecord": false
    }
}

2022-10-07 14:40:16,331: INFO: {
    "AvailabilityZone": "eu-central-1c",
    "AvailabilityZoneId": "euc1-az1",
    "AvailableIpAddressCount": 251,
    "CidrBlock": "192.168.13.0/24",
    "DefaultForAz": false,
    "MapPublicIpOnLaunch": false,
    "MapCustomerOwnedIpOnLaunch": false,
    "State": "available",
    "SubnetId": "subnet-0844d251c575a8cdc",
    "VpcId": "vpc-0d2022c4752b36f73",
    "OwnerId": "123456789012",
    "AssignIpv6AddressOnCreation": false,
    "Ipv6CidrBlockAssociationSet": [],
    "Tags": [
        {
            "Key": "Name",
            "Value": "ta-subnet-private3-1c"
        }
    ],
    "SubnetArn": "arn:aws:ec2:eu-central-1:123456789012:subnet/subnet-0844d251c575a8cdc",
    "EnableDns64": false,
    "Ipv6Native": false,
    "PrivateDnsNameOptionsOnLaunch": {
        "HostnameType": "ip-name",
        "EnableResourceNameDnsARecord": false,
        "EnableResourceNameDnsAAAARecord": false
    }
}

2022-10-07 14:40:16,331: INFO: {
    "AvailabilityZone": "eu-central-1a",
    "AvailabilityZoneId": "euc1-az2",
    "AvailableIpAddressCount": 251,
    "CidrBlock": "192.168.11.0/24",
    "DefaultForAz": false,
    "MapPublicIpOnLaunch": false,
    "MapCustomerOwnedIpOnLaunch": false,
    "State": "available",
    "SubnetId": "subnet-0d23a0b7cdfb3c3f4",
    "VpcId": "vpc-0d2022c4752b36f73",
    "OwnerId": "123456789012",
    "AssignIpv6AddressOnCreation": false,
    "Ipv6CidrBlockAssociationSet": [],
    "Tags": [
        {
            "Key": "Name",
            "Value": "ta-subnet-private1-1a"
        }
    ],
    "SubnetArn": "arn:aws:ec2:eu-central-1:123456789012:subnet/subnet-0d23a0b7cdfb3c3f4",
    "EnableDns64": false,
    "Ipv6Native": false,
    "PrivateDnsNameOptionsOnLaunch": {
        "HostnameType": "ip-name",
        "EnableResourceNameDnsARecord": false,
        "EnableResourceNameDnsAAAARecord": false
    }
}

2022-10-07 14:40:16,331: INFO: {
    "AvailabilityZone": "eu-central-1c",
    "AvailabilityZoneId": "euc1-az1",
    "AvailableIpAddressCount": 251,
    "CidrBlock": "192.168.3.0/24",
    "DefaultForAz": false,
    "MapPublicIpOnLaunch": false,
    "MapCustomerOwnedIpOnLaunch": false,
    "State": "available",
    "SubnetId": "subnet-00297bdd6ba96d480",
    "VpcId": "vpc-0d2022c4752b36f73",
    "OwnerId": "123456789012",
    "AssignIpv6AddressOnCreation": false,
    "Ipv6CidrBlockAssociationSet": [],
    "Tags": [
        {
            "Key": "Name",
            "Value": "ta-subnet-public3-1c"
        }
    ],
    "SubnetArn": "arn:aws:ec2:eu-central-1:123456789012:subnet/subnet-00297bdd6ba96d480",
    "EnableDns64": false,
    "Ipv6Native": false,
    "PrivateDnsNameOptionsOnLaunch": {
        "HostnameType": "ip-name",
        "EnableResourceNameDnsARecord": false,
        "EnableResourceNameDnsAAAARecord": false
    }
}

2022-10-07 14:40:16,331: INFO: {
    "AvailabilityZone": "eu-central-1a",
    "AvailabilityZoneId": "euc1-az2",
    "AvailableIpAddressCount": 250,
    "CidrBlock": "192.168.1.0/24",
    "DefaultForAz": false,
    "MapPublicIpOnLaunch": false,
    "MapCustomerOwnedIpOnLaunch": false,
    "State": "available",
    "SubnetId": "subnet-08b345c4cd76aac6b",
    "VpcId": "vpc-0d2022c4752b36f73",
    "OwnerId": "123456789012",
    "AssignIpv6AddressOnCreation": false,
    "Ipv6CidrBlockAssociationSet": [],
    "Tags": [
        {
            "Key": "Name",
            "Value": "ta-subnet-public1-1a"
        }
    ],
    "SubnetArn": "arn:aws:ec2:eu-central-1:123456789012:subnet/subnet-08b345c4cd76aac6b",
    "EnableDns64": false,
    "Ipv6Native": false,
    "PrivateDnsNameOptionsOnLaunch": {
        "HostnameType": "ip-name",
        "EnableResourceNameDnsARecord": false,
        "EnableResourceNameDnsAAAARecord": false
    }
}
```
