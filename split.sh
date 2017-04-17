for f in `cat bitcoin.json | jq -r 'keys[]'` ; do
  cat bitcoin.json | jq ".$f" > $f.json
done
