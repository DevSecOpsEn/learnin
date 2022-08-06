import json
import yaml
import sys

in_file = sys.argv[1]
out_file = sys.argv[2]

with open(in_file, 'r') as json_in, open(out_file, 'w') as yaml_out:
    json_text = json.load(json_in)
    yaml_out.write("---\n"+yaml.dump(json_text, sort_keys=False)+"...")
