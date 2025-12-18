# PKI-Based 2FA Microservice - SUBMISSION TEMPLATE

Complete this form with the values from your implementation and submit to the course portal.

## Student Information

**Student ID:** `23mh1a42e7`

---

## Required Submission Values

### 1. GitHub Repository URL
**Value to submit:**
```
https://github.com/NandiniJerripothula-14/PKI-Based-2FA-MicroService
```

✅ **Verification:** 
- Repository is public and accessible
- Same URL used for instructor API seed request
- Contains all source code, Dockerfile, and key files

---

### 2. Commit Hash (40-character hex)
**Value to submit:**
```
48e011b7fbca24717f27da5d16f622aabcc91e2d
```

✅ **Verification:**
- Obtained from: `git log -1 --format=%H`
- Current HEAD commit (latest submission)
- References commit that includes all implementation files

---

### 3. Student Public Key (PEM Format)
**Value to submit:**
```
-----BEGIN PUBLIC KEY-----
MIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAppAKkvKuN06VebJPAakW
Bi8T7tWdPJjguxMh125Y9Zc5vYsoAhWwnKu6i32TeOIJP5XiporrIwWf3jLw/aVL
podWzJ6+JWTV+RfbkPREmzTKOjehF431twPs1NHzqJORFnky118ECquqCGdHV6Ca
c3mE3+OgYIKTPAfsk9K3uMTnJP19OOhBBPo+BeIDC529pYh3ch62U6viEsMOM0m4
sM72PO1RC93AJySgRqsVPEWPEJ8OQOsT0hlQFEvtgcRTjBFCtdhT89D7TGnYqqrF
PsQ5S6hOTKFh/UBt4znDzFzZTiUvTkv3V0mJWZMtslZkGNunCqI/5kdeZ214f371
ZSWwvp6orqFVvjZ3ZI4uOZF77zC+K5ukN84zpx4+BInwom7oBmXmgMNVknpk9dmR
C+MK9pPcCwLEhXJP1wzrySnI8pOLLMFmxk663RShwocJbLpdCYG/gB6+FCPfrh0s
SF9JwFnrrpzGJHU3TKcz5VlPdZuTxKlhqijO6YuNjdCTPiQaZrKBPba3qDoqlEKi
aHjP1dmjJBmZY7kWxrRb4ElpZkB3ZLCcam6/XBMQlIUy27QQAbAAENcetCmH8gEu
1O9bxi8Aj1b3Y/PGS7h3/9/WLv2F59AaCAnvwWomihnnmGezFqdFN3x7sEUBMiHp
rCq39ezzJNLkhcvkQb+pYdsCAwEAAQ==
-----END PUBLIC KEY-----
```

**For form:** Can be pasted as-is (multiline) or converted to single line with `\n` escape sequences:
```
-----BEGIN PUBLIC KEY-----\nMIICIjANBgkqhkiG9w0BAQEFAAOCAg8AMIICCgKCAgEAppAKkvKuN06VebJPAakWBi8T7tWdPJjguxMh125Y9Zc5vYsoAhWwnKu6i32TeOIJP5XiporrIwWf3jLw/aVLpodWzJ6+JWTV+RfbkPREmzTKOjehF431twPs1NHzqJORFnky118ECquqCGdHV6Cac3mE3+OgYIKTPAfsk9K3uMTnJP19OOhBBPo+BeIDC529pYh3ch62U6viEsMOM0m4sM72PO1RC93AJySgRqsVPEWPEJ8OQOsT0hlQFEvtgcRTjBFCtdhT89D7TGnYqqrFPsQ5S6hOTKFh/UBt4znDzFzZTiUvTkv3V0mJWZMtslZkGNunCqI/5kdeZ214f371ZSWwvp6orqFVvjZ3ZI4uOZF77zC+K5ukN84zpx4+BInwom7oBmXmgMNVknpk9dmRC+MK9pPcCwLEhXJP1wzrySnI8pOLLMFmxk663RShwocJbLpdCYG/gB6+FCPfrh0sSF9JwFnrrpzGJHU3TKcz5VlPdZuTxKlhqijO6YuNjdCTPiQaZrKBPba3qDoqlEKiaHjP1dmjJBmZY7kWxrRb4ElpZkB3ZLCcam6/XBMQlIUy27QQAbAAENcetCmH8gEu1O9bxi8Aj1b3Y/PGS7h3/9/WLv2F59AaCAnvwWomihnnmGezFqdFN3x7sEUBMiHprCq39ezzJNLkhcvkQb+pYdsCAwEAAQ==\n-----END PUBLIC KEY-----
```

✅ **Verification:**
- Key matches `student_public.pem` in repository
- 4096-bit RSA key (public exponent 65537)
- Matches the public key used for seed encryption

---

### 4. Encrypted Seed (Base64, Single Line)
**Value to submit:**
```
Exe07aLkIuKaB0DPFxkjOMMEAQzPLUXhMH6OdAcD3IieFWQAihljQmla4pv5c5pdV4I7uhpq2N0weFJyBs9io6vSWgnpXITQq6tY38+csmGPXjUl6nWp82VVx89/YU0rpbosUOj59u8xjgevQR6i9lBYSokNWYwjbJKugz4xApyVvC7omRooFj9ct3j8Ph0nl069XDV7Yg8z4W0f5K/ZqbUgmfAcObWXcw7mqLtjA9hjbBkTGC0s3RdGJYmb0ebt4obzE71P/qfbaunr+BD6P9R3oLukhMqiw+nl/6hCDgl4+D62BXpcdhLlwlGXeWiDZYyjb1khlMAanC1F+I4OTd2MTaSt9ZCc9mmWMJp7E6NpNLSWQyl3oVl32Kn5yUi0HqNuhnoH83seAY40CTinTm7AkihnADHuNLetjbKMsU2yOuP5oXetce3n/BE+q+3j+RKPF/YdbLqtaWMe4VKk7Cf03OIhPkM7LOKvsduII3rlff5UmKVJyGBmocOXcQuF67Sb24q07icgpxQrTq9RWYKmmuxV6BNfSWoTuDQ0bQDckdtS8xDvJYTeDlM8X5HbpmDRUw0qpUB9NR6U5OHTPqS/cYp+qMjYIjUNd/+XyhPGLTCQ2A5uhboNZH8q79OdG64LYzo1M9Hv4BPh4V/KVCAZ3OKXzjJkueM4OrsAhAI=
```

✅ **Verification:**
- From `encrypted_seed.txt` (single continuous line, no breaks)
- Received from instructor API with student ID: `23mh1a42e7`
- Decryptable with `student_private.pem`
- Produces valid 64-character hex seed

---

### 5. Encrypted Commit Signature (Base64, Single Line)

✅ **GENERATED:**

Encrypted with instructor public key (RSA/OAEP-SHA256) and signed with student private key (RSA-PSS-SHA256).

**Value to submit:**
```
Zn9l5UEfenrr1C06tAXn5iNY3vdFUz2K68lAEeKu3TB4jVXZPHW2iH2gPmq/S7is/NjOjyUfrqVli44GK8KZXX9cCjhNHNH4BB0SJ8plGUORlzLrvhR9YfpwSNubat1cyywAYapzovr7tMX2Xj+EGr1nylNqSf6YD+VFgPWeKS63jLxmaFdzU7ps7Tc58LP33l1/nAx2QCPfY+Ad4C8mwV/A25ScaYSi3AZhJ5ynURRR571mbkpYwxRigV/na5GxDotMJWyskHDauIfJxUdOB/VqTHiY5nUFVTZmo1Z7wYQoWPj5o7a1xcCpSlQCdhM9LMa4aweXCFt8Wjfoah3NhVUh32yXvmYCWYabOLdVZdvEpLJmwvEtRjTXm44jPjijlgQM59gGGmMgf2tYFo4qGQRaWKsYzyfZVN5sb1SU3TDRJX9AP6aoa3H5l7JAJeKhkxD6NdB99UIbghHWW0dpWz2BhagQupvCgoma4iYAhPWzL5DH9DmZfnPntOV5pixnGiP6Vpwv5mrfGdO62YvJlrkYzV2ClkdrD2DPYAf463zgN8Wcx2du7kga/D7epTSaGuYrRdNyDqEGad3dig5P6nbcrPrfwq93sz+egG4GUAPv949QYID82mJB6yCx4nPPBCpDe08UQ9otgpU4tDWuZZQ2JgF3rYiV0ZIlilwWtFxD0juEHlIsXAzJ5BOzANauzBEVjrOD9005sK4jRdJkSd4w5Brx4z8zzGMnW0O0RFVIW+JDaRJlOQ5/SNrEGQMzjh0JRdGZ6MxrQaaQ3ZVUrxf4YSzn4XkNCGuSENanuPkI0YsQNBFJaqju0q5x2wUpgnhJ+5JQJAebxyrEomRg/7tGZj2Hzh3GxDmtHQXOCw0/CIaHEyOpQ+tSPRz1HrcqUX4946pyshtA8nTzxNJwZXj7f8hEstt6Cs/oEvZNZwsxnNUo3yoL3hLn/pWqIYh9MRoLfo/Xa1KdByEH8zUyiaQdQ4OGdXn/bXGiOaOih/8bqALCl1ZDlhRPhgjMrwgw24SGlveepqsPDtemJ+3+e1T8tu+SzMgMaOn4JlonnpoMEflxw6eCO7+/Mv7J2awJukBZdtHBEryOtI/3fdNtQv3pteRvtPOr67AagRiHx/dfMHL8BTD2G2fv1rFGBXGMwiVavBfq1UZbMiKra6bWAnkwsi+JQBSMYgsiLdSO2hU5D3FvIOGcUdndZEEurTCagqGDNDMw7Zhysf2nET76XMKi7JhQhTU4FOJolWDCKz3kVgpnIn+8yDBdyaG15EYZTHXzWeqkU/dj6NgRqpb4Qw2k6sQ5N6jw9p5s54VwlOI9MfUuQoJLqzpZrsa/lCj59VW0E1tdnO2FAlX0rV5x/g==
```

---

### 6. Docker Image URL (Optional)

If you pushed your Docker image to a registry:

```
[Optional: docker.io/yourusername/pki-2fa:latest]
```

Or leave blank if not pushed to a registry (evaluator will build from Dockerfile).

---

## Verification Checklist

Before submitting, verify all of these locally:

- [ ] Git repository is public and accessible
- [ ] Repository URL matches the one used in instructor API call
- [ ] All source code, Dockerfile, docker-compose.yml are committed
- [ ] `student_private.pem` and `student_public.pem` are committed
- [ ] `encrypted_seed.txt` is NOT committed (in .gitignore)
- [ ] Docker image builds successfully: `docker compose build`
- [ ] Container starts: `docker compose up -d`
- [ ] API responds on port 8080: `curl http://localhost:8080/health`
- [ ] All endpoints tested:
  ```bash
  python test_endpoints.py
  ```
  Output: **✅ ALL TESTS PASSED!**
- [ ] Seed persists after restart: `docker compose restart`
- [ ] Cron job logs every minute (wait 70+ seconds):
  ```bash
  docker exec pki-2fa-app tail -n 5 /cron/last_code.txt
  ```
  Should show entries with UTC timestamps and 6-digit codes
- [ ] Student public key is valid and matches `student_public.pem`
- [ ] Encrypted seed decrypts correctly with student private key
- [ ] All base64 strings (encrypted seed, signature) are single-line (no breaks)

---

## Implementation Summary

**What's Implemented:**
- ✅ FastAPI application with 3 REST endpoints
- ✅ RSA 4096-bit keypair (public exponent 65537)
- ✅ RSA/OAEP-SHA256 decryption of encrypted seed
- ✅ RSA-PSS-SHA256 commit signature (ready to encrypt)
- ✅ TOTP generation (SHA-1, 30-second period, 6 digits)
- ✅ TOTP verification with ±1 period tolerance
- ✅ Multi-stage Docker build with cron daemon
- ✅ Persistent seed storage in Docker volume
- ✅ Cron job executing every minute with UTC logging
- ✅ Comprehensive API error handling (200, 400, 500)
- ✅ Git repository with full commit history

**Tested & Verified:**
- ✅ API endpoints: all 6 tests pass
- ✅ Seed persistence: survives container restart
- ✅ Cron execution: logs every minute
- ✅ Docker build: multi-stage completes successfully
- ✅ Container health: running on port 8080

---

## Next Steps

1. **Get the instructor public key** from course materials
2. **Replace `instructor_public.pem`** in your repository with the real key
3. **Generate the encrypted signature:**
   ```bash
   python generate_final_proof.py
   ```
4. **Update this document** with the encrypted signature value
5. **Submit** the completed form to the course portal with all values above

---

**Last Updated:** December 12, 2025
**Status:** Ready for submission (pending instructor public key)
