/*
 * Copyright 2019-present Open Networking Foundation
 *
 * Licensed under the Apache License, Version 2.0 (the "License");
 * you may not use this file except in compliance with the License.
 * You may obtain a copy of the License at
 *
 *     http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS,
 * WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 * See the License for the specific language governing permissions and
 * limitations under the License.
 */

#include <core.p4>
#include <v1model.p4>

#include "include/header.p4"
#include "include/parser.p4"
#include "include/checksum.p4"

#define CPU_CLONE_SESSION_ID 99
#define USID_BLOCK_MASK     (0xffffffff << 96)


control IngressPipeImpl (inout parsed_headers_t hdr,
                         inout local_metadata_t local_metadata,
                         inout standard_metadata_t standard_metadata) {

    action drop() {
        mark_to_drop();
    }

    action set_output_port(port_num_t port_num) {
        standard_metadata.egress_spec = port_num;
    }

    direct_counter(CounterType.packets_and_bytes) unicast_counter; 
    table unicast {
        key = {
            hdr.ethernet.dst_addr: exact; 
        }
        actions = {
            set_output_port;
            drop;
            NoAction;
        }
        counters = unicast_counter;
        default_action = NoAction();
    }

    direct_counter(CounterType.packets_and_bytes) l2_firewall_counter;
    table l2_firewall {
	    key = {
	        hdr.ethernet.dst_addr: exact;
	    }
	    actions = {
	        NoAction;
	    }
    	counters = l2_firewall_counter;
    }

    action set_next_hop(mac_addr_t next_hop) {
	    hdr.ethernet.src_addr = hdr.ethernet.dst_addr;
	    hdr.ethernet.dst_addr = next_hop;
	    hdr.ipv6.hop_limit = hdr.ipv6.hop_limit - 1;
    }

    direct_counter(CounterType.packets_and_bytes) routing_v6_counter;
    table routing_v6 {
	    key = {
	        hdr.ipv6.dst_addr: lpm;
	    }
        actions = {
	        set_next_hop;
        }
        counters = routing_v6_counter;
    }

    action end_action() {
        // set destination IP address to next segment
        hdr.ipv6.dst_addr = local_metadata.next_srv6_sid;
    }

    action end_action_usid() {
        hdr.ipv6.dst_addr = (hdr.ipv6.dst_addr & USID_BLOCK_MASK) | ((hdr.ipv6.dst_addr << 16) & ~((bit<128>)USID_BLOCK_MASK));
    }

    direct_counter(CounterType.packets_and_bytes) my_sid_table_counter;
    table my_sid_table {
        key = {
            hdr.ipv6.dst_addr: lpm;
        }
        actions = {
            end_action;
            end_action_usid;
            NoAction;
        }
        default_action = NoAction;
        counters = my_sid_table_counter;
    }

    apply {
	    if (hdr.ipv6.hop_limit == 0) {
	        drop();
	    }

	    if (l2_firewall.apply().hit) {
            switch(my_sid_table.apply().action_run) {
                end_action: {
                    // support for reduced SRH
                    if (hdr.srv6h.segment_left > 0) {
                        // decrement segments left
                        hdr.srv6h.segment_left = hdr.srv6h.segment_left - 1;
                    } 
                }
            }

            
	        routing_v6.apply();
	    }
        
        unicast.apply();
    }
}

control EgressPipeImpl (inout parsed_headers_t hdr,
                        inout local_metadata_t local_metadata,
                        inout standard_metadata_t standard_metadata) {
    apply { }
}

V1Switch(
    ParserImpl(),
    VerifyChecksumImpl(),
    IngressPipeImpl(),
    EgressPipeImpl(),
    ComputeChecksumImpl(),
    DeparserImpl()
) main;
