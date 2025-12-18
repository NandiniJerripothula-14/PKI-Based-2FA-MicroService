import requests
import json

BASE = 'http://localhost:8080'

print('1) Health ->', end=' ')
r = requests.get(BASE + '/health', timeout=5)
print(r.status_code, r.json())

# Post encrypted seed to /decrypt-seed
print('\n2) POST /decrypt-seed ->', end=' ')
with open('encrypted_seed.txt', 'r') as f:
    enc = f.read().strip()
resp = requests.post(BASE + '/decrypt-seed', json={'encrypted_seed': enc}, timeout=10)
print(resp.status_code, resp.text)

# Generate 2FA
print('\n3) GET /generate-2fa ->', end=' ')
r = requests.get(BASE + '/generate-2fa', timeout=5)
print(r.status_code, r.json())
code = r.json().get('code')

# Verify valid code
print('\n4) POST /verify-2fa (valid) ->', end=' ')
r_valid = requests.post(BASE + '/verify-2fa', json={'code': code}, timeout=5)
print(r_valid.status_code, r_valid.json())

# Verify invalid code
print('\n5) POST /verify-2fa (invalid) ->', end=' ')
r_inv = requests.post(BASE + '/verify-2fa', json={'code': '000000'}, timeout=5)
print(r_inv.status_code, r_inv.json())

# Verify missing code
print('\n6) POST /verify-2fa (missing) ->', end=' ')
r_miss = requests.post(BASE + '/verify-2fa', json={}, timeout=5)
print(r_miss.status_code, r_miss.text)
