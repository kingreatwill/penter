#!/usr/bin/env python3
import argparse
import requests
import pingparsing
import itertools
import ipaddress
from concurrent.futures import ThreadPoolExecutor
import functools
import json

# pip install pingparsing -i https://mirrors.aliyun.com/pypi/simple
MAX_THREAD = None
MAX_HOST = None
TIMEOUT = None
pool = None


def ping_host(host: str):
    ping_parser = pingparsing.PingParsing()
    transmitter = pingparsing.PingTransmitter()
    transmitter.destination = host
    transmitter.count = 10
    transmitter.timeout = TIMEOUT
    result = transmitter.ping()
    rtt_avg = ping_parser.parse(result).as_dict()["rtt_avg"]
    return host, rtt_avg


def compare(x, y):
    rtt_x = x[1]
    rtt_y = y[1]
    if rtt_x is None:
        return 1
    elif rtt_y is None:
        return -1
    else:
        return rtt_x - rtt_y


def get_best_host(hosts):
    jobs = []
    i = 0
    for host in hosts:
        i = i + 1
        if i > MAX_HOST:
            break
        jobs.append(pool.submit(ping_host, host))
    host2rtt = []
    for job in jobs:
        host, rtt = job.result()
        host2rtt.append((host, rtt))
    if len(host2rtt) < 1:
        return None, None
    host2rtt = sorted(host2rtt, key=functools.cmp_to_key(compare))
    return host2rtt[0]


def get_hosts(address_str):
    address = ipaddress.ip_network(address_str)
    if address.num_addresses == 1:
        return [address.network_address]
    else:
        return address.hosts()


if __name__ == "__main__":
    parser = argparse.ArgumentParser("Fetch Github IP hosts with smallest rtt_avg")
    parser.add_argument("--max_host", type=int,
                        help="maxmimum number host for each url", default=256)
    parser.add_argument("--max_thread", type=int,
                        help="maxmimum number ping thread", default=128)
    parser.add_argument("--timeout", type=int,
                        help="timeout for each ping packet, unit:ms", default=500)
    # http proxy only
    parser.add_argument("--host", type=str, help="proxy host for get meta request")
    parser.add_argument("--port", type=str, help="proxy port for get meta request")

    args = parser.parse_args()
    host = args.host
    port = args.port
    proxy = None
    MAX_HOST = args.max_host
    MAX_THREAD = args.max_thread
    TIMEOUT = args.timeout
    pool = ThreadPoolExecutor(MAX_THREAD)
    if host is not None and port is not None:
        proxy = {
            "http": "http://{}:{}".format(host, port)
        }
        print("use proxy: '{}'".format(proxy["http"]))
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.105 Safari/537.36',
    }
    r = requests.get("https://api.github.com/meta", headers=headers, proxies=proxy)
    if r.status_code == requests.codes.ok:
        data = r.json()
        apis = {
            "hooks.github.com": data["hooks"],
            "web.github.com": data["web"],
            "api.github.com": data["api"],
            "pages.github.com": data["pages"],
            "importer.github.com": data["importer"],
        }
        print(json.dumps(apis, indent=2))
        url2hosts = {}
        for k, v in apis.items():
            hosts = itertools.chain.from_iterable([get_hosts(address) for address in v])
            hosts = [str(host) for host in list(hosts)]
            url2hosts[k] = hosts

        best_hosts = {}
        for url, hosts in url2hosts.items():
            best_host, rtt = get_best_host(hosts)
            if rtt is not None:
                best_hosts[url] = best_host
                print("url:{:<20} host:{:<20} rtt:{}".format(url, best_host, rtt))
            else:
                print("all ips for {} failed".format(url))

        print("=======following can be copied to /etc/hosts/=======")
        for url, host in best_hosts.items():
            print("{} {}".format(url, host))

    else:
        print("REQUESTS FAILED\n{}".format(r.content))
