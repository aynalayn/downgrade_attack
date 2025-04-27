# downgrade_attack



# **TLS Downgrade Attack CTF Challenge**  
**Objective**: Extract the flag by bypassing modern TLS protections using legacy tools.

## 📦 Required Tools (Included in `/tools`)
1. **Legacy OpenSSL 1.1.1**  
   Location: `tools\OpenSSL-1.1.1\bin\openssl.exe`  
   (For TLS 1.0 connections)

2. **Python 3.8**  
   Location: `tools\Python38\python.exe`  
   (For running the vulnerable server)

## 🚀 Step-by-Step Guide

### 1. Start the Server
```cmd
cd C:\downgrade_ctf\server
..\tools\Python38\python.exe server.py
```

### 2. Attack Sequence

#### Test with Modern OpenSSL (Will Fail)
```cmd
cd C:\downgrade_ctf
openssl s_client -connect localhost:4433 -tls1
```
*Expected error: `no protocols available`*

#### Get Flag with Legacy OpenSSL
```cmd
cd C:\downgrade_ctf
tools\OpenSSL-1.1.1\bin\openssl.exe s_client -connect localhost:4433 -tls1 -no_verify
```
*Flag format: `FLAG:{TLS_DOWNGRADE_MASTER_1337}`*

## 📂 File Structure
```
downgrade_ctf/
├── tools/
│   ├── OpenSSL-1.1.1/  # Legacy OpenSSL
│   └── Python38/       # Python 3.8
├── server/             # Server code
└── client/             # Attack instructions
```

## 💡 Key Points
- Modern systems block TLS 1.0 (CVE-2011-3389)
- Legacy tools bypass these protections
- All executables run from local `tools` folder

## ⚠️ Troubleshooting
If commands fail:
1. Verify all files are in the correct locations
2. Check server is running (`netstat -ano | findstr 4433`)
3. Disable firewall temporarily during testing

---

This version:
1. Uses direct relative paths (`tools\Python38\python.exe`)
2. Requires no system PATH changes
3. Maintains clear folder structure
4. Provides exact command sequences

Participants will:
1. Navigate to the project folder
2. Run commands exactly as shown
3. Never need to modify system settings

Here's a comprehensive **README.md** in English for your TLS Downgrade Attack CTF challenge:

---

# **TLS Downgrade Attack CTF Challenge**  
**Difficulty**: Intermediate  
**Category**: Cryptography/Network Security  
**Flag**: `FLAG:{TLS_DOWNGRADE_MASTER_1337}`  

## 📝 Challenge Description  
This lab demonstrates a real-world TLS downgrade attack where modern systems block deprecated TLS 1.0, but legacy clients can still exploit servers supporting old protocols.  

**Learning Objectives**:  
- Understand TLS protocol differences  
- Experience modern security restrictions  
- Perform a manual downgrade attack  

## 🛠️ Prerequisites  
- Windows 10/11  
- Python 3.8 (for server)  
- Two OpenSSL versions:  
  - **Modern** (v3.x): Blocks TLS 1.0 (`C:\Program Files\OpenSSL-Win64\bin\openssl.exe`)  
  - **Legacy** (v1.1.1): Allows TLS 1.0 (`C:\OpenSSL-1.1.1\bin\openssl.exe`)  

## 🚀 Setup Instructions  

### 1. Start the Server  
```cmd
cd C:\downgrade_ctf\server
"C:\Python38\python.exe" server.py
```
*Server runs on `localhost:4433` supporting TLS 1.0/1.3*  

### 2. Generate Certificates (First-Time Setup)  
```cmd
"C:\OpenSSL-1.1.1\bin\openssl.exe" req -x509 -newkey rsa:2048 -keyout server.key -out server.crt -days 365 -nodes -subj "/CN=localhost"
```

## 🔍 Attack Walkthrough  

### Step 1: Modern Client Test (TLS 1.3)  
```cmd
"C:\Program Files\OpenSSL-Win64\bin\openssl.exe" s_client -connect localhost:4433 -tls1_3 -no_verify
```
**Expected Output**:  
`Server requires TLS 1.0 connection to get the flag`  

### Step 2: Attempt TLS 1.0 (Blocked)  
```cmd
"C:\Program Files\OpenSSL-Win64\bin\openssl.exe" s_client -connect localhost:4433 -tls1 -no_verify
```
**Expected Error**:  
`no protocols available` (Modern OpenSSL blocks TLS 1.0)  

### Step 3: Successful Attack (Legacy Client)  
```cmd
"C:\OpenSSL-1.1.1\bin\openssl.exe" s_client -connect localhost:4433 -tls1 -no_verify
```
**Flag**:  
`Success! Your flag: FLAG:{TLS_DOWNGRADE_MASTER_1337}`  

## 🧠 Explanation  
- **Why TLS 1.0 is dangerous**: Vulnerable to BEAST, POODLE attacks  
- **Modern protections**: OpenSSL 3.x+ actively blocks deprecated protocols  
- **Real-world impact**: Legacy systems (IoT, old servers) remain vulnerable  

## ⚠️ Troubleshooting  
| Issue | Solution |
|-------|----------|
| Connection refused | Check `netstat -ano \| findstr 4433` |
| Certificate errors | Use `-no_verify` flag in all commands |
| Git problems | Upload files manually via GitHub UI |

## 📚 Resources  
- [OpenSSL Docs](https://www.openssl.org/docs/)  
- [TLS Downgrade Attacks (OWASP)](https://owasp.org/www-community/attacks/SSL_Downgrade)  
