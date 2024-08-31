# import sys
# def process_input(input):
#         print("Siu "+input)

# for line in sys.stdin:
#         process_input(line.strip())
# process_dict.py

import json
import sys

def process_dictionary(data):
    # Example function to process the dictionary
    print("Received dictionary:")
    print(json.dumps(data, indent=4))

if __name__ == "__main__":
    if len(sys.argv) > 1:
        # Assuming the first argument is a JSON string representing the dictionary
        dict_str = sys.argv[1]
        data = json.loads(dict_str)
    else:
        print("No dictionary provided.")
