# SUBMISSION SUMMARY

## Student Information
- **Student ID:** 23mh1a42e7
- **Repository URL:** https://github.com/NandiniJerripothula-14/PKI-Based-2FA-MicroService
- **Latest Commit:** 787578c (Add helper scripts for key generation, seed request, testing, and proof generation)

## Required Submission Values

### 1. GitHub Repository URL
```
https://github.com/NandiniJerripothula-14/PKI-Based-2FA-MicroService
```

### 2. Commit Hash
```
787578c
```
*(or 6d8e277 from initial commit)*

### 3. Student Public Key
To retrieve:
```bash
cat student_public.pem
```
Include entire file with BEGIN/END markers.

### 4. Encrypted Seed (Base64)
Already saved locally:
```bash
cat encrypted_seed.txt
```
**IMPORTANT:** Copy as single line (no line breaks).

### 5. Encrypted Commit Signature
To generate (requires real instructor public key):

1. Replace `instructor_public.pem` with the actual public key from course materials
2. Run:
   ```bash
   python generate_final_proof.py
   ```
3. Copy the output under "Encrypted Signature (base64, single line)"
4. Include in submission (single line, no breaks)

## What's Implemented ✅

### API Endpoints (all working)
- `POST /decrypt-seed` - RSA/OAEP decryption, seed persistence
- `GET /generate-2fa` - TOTP generation (SHA-1, 30s, 6 digits)
- `POST /verify-2fa` - TOTP verification with ±1 period tolerance
- `GET /health` - Bonus health check

### Security Features
- RSA 4096-bit key pair (public exponent 65537)
- RSA/OAEP-SHA256 decryption
- RSA-PSS-SHA256 commit signature
- TOTP verification with time window
- Secure file permissions (seed: 0600)
- UTF timezone for API and cron

### Docker & Deployment
- Multi-stage Dockerfile (builder + runtime)
- Python 3.11-slim base image
- Cron daemon running every minute
- Persistent volumes for `/data` and `/cron`
- Port 8080 exposed and functional
- Container restart-safe storage

### Testing & Verification
- API endpoint tests: ✅ ALL PASS
- Seed decryption: ✅ VERIFIED
- TOTP generation: ✅ VERIFIED (6-digit codes match expected)
- Cron execution: ✅ VERIFIED (UTC timestamps, minute intervals)
- Persistence: ✅ VERIFIED (seed survives restart)
- Docker build: ✅ SUCCESSFUL

## Key Files in Repository

**Committed (required):**
- `student_private.pem` - Student RSA private key
- `student_public.pem` - Student RSA public key
- `instructor_public.pem` - Placeholder (⚠️ MUST be replaced)
- All source code, Dockerfile, docker-compose.yml
- Helper scripts for testing and proof generation

**NOT Committed (intentional):**
- `encrypted_seed.txt` - Sensitive, kept local only

## Docker Image Details
- Image name: `pki-based-2fa-microservice-app`
- Base: `python:3.11-slim`
- Exposed port: 8080
- Volumes: `/data` (seed), `/cron` (logs)
- Timezone: UTC
- Entrypoint: `/start.sh` (starts cron + uvicorn)

## Testing Commands

```bash
# Build and run
docker compose build
docker compose up -d

# Test API
python test_endpoints.py

# Check cron (after 70+ seconds)
docker exec pki-2fa-app tail -n 5 /cron/last_code.txt

# Test persistence
docker compose restart
docker exec pki-2fa-app cat /data/seed.txt
```

## Project Status: COMPLETE ✅

All core requirements implemented, tested, and verified.

**Waiting for:** Instructor public key to generate final encrypted signature.

Once you provide the real `instructor_public.pem`, run `python generate_final_proof.py` and submit the encrypted signature along with the other values above.
