#!/bin/bash

iptables -t nat -A PREROUTING \
   -p udp --dport 67 -j DNAT --to-destination :9067
iptables -t nat -A PREROUTING \
   -p udp --dport 69 -j DNAT --to-destination :9069
iptables -t nat -A POSTROUTING \
   -p udp --sport 9067 -j MASQUERADE --to-ports 67
iptables -t nat -A POSTROUTING \
   -p udp --sport 9069 -j MASQUERADE --to-ports 69
