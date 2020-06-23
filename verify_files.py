# Validates `manifest.json`
# Checks all files appear in `voices` field exist in the directory
# Checks a keyword only appears once
import os
import json

os.chdir('src')

def has_file(fname, contents):
    return fname in contents

def validate_config(config, contents):
    ret = 0
    kwset = set()
    if 'contributes' in config:
        for entry in config['contributes']:
            if ret:
                return ret
            if 'voices' not in entry:
                print(f'Panic on: {entry}\nEntry does not have `voices` field')
                ret = 1
                continue
            if 'keywords' not in entry:
                print(f'Panic on: {entry}\nEntry does not have `keywords` field')
                ret = 1
                continue
            for kw in entry['keywords']:
                if kw in kwset:
                    print(f'Panic on: {entry}\nUsing f{kw} twice')
                    ret = 1
            for fname in entry['voices']:
                if not has_file(fname, contents):
                    print(f'{fname} is not found but referred')
                    ret = 1
                    break
            
        return ret
    else:
        error('manifest.json is not well-formed')
        return 1

def main():
    contents = list(filter(lambda x: x.endswith('wav') or x.endswith('mp3'), os.listdir()))
    with open('manifest.json', 'r') as fp:
        config = json.load(fp)
        return validate_config(config, contents)

if __name__ == '__main__':
    exit(main())