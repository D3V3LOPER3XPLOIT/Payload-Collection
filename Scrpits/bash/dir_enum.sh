#!/bin/bash
while read line; do
  curl -s -o /dev/null -w "%{http_code} -> %{url_effective}\n" http://$1/$line
done < wordlist.txt
