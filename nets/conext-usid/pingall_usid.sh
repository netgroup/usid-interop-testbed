#!/bin/bash

passed=0
total=0
declare -a endpoints=(
        "fcbb:bbbb:0100::"
        "fcbb:bbbb:0200::"
        "fcbb:bbbb:0300::"
        "fcbb:bbbb:0400::"
        "fcbb:bbbb:0500::"
        "fcbb:bbbb:0600::"
        "fcbb:bbbb:0700::"
        "fcbb:bbbb:0800::"
)

for i in "${endpoints[@]}"; do
	ping -c 1 "${i}" &>/dev/null \
		&& { echo -e "${i}\treachable"; passed=$((passed+1)); } \
		|| { echo -e "${i}\tUNREACHABLE"; }
	total=$((total+1))
done

echo ""
printf "Test PASSED %d/%d\n" ${passed} ${total}
