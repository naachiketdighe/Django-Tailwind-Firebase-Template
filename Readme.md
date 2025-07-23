# Firebase Setup Instructions

This project integrates with Firebase for authentication and/or backend services. Follow these steps to configure Firebase.

## 1️⃣ Create a Firebase Project

1. Visit [Firebase Console](https://console.firebase.google.com)  
2. Click **“Add Project”** and follow the setup wizard  
3. After setup, you’ll be redirected to your project dashboard  

## 2️⃣ Register a Web App

1. In the Firebase dashboard, click the **⚙️ Project settings** icon  
2. Scroll to **Your apps** and click the **</> (Web)** icon  
3. Enter an app nickname (e.g., `MyApp`) and click **Register app**  

## 3️⃣ Download Firebase Admin SDK Config

1. In **Project settings**, go to the **Service accounts** tab  
2. Click **Generate new private key**  
3. A file named `firebase-adminsdk-xxxxx.json` will download  

**Save this file as:**  
`firebase-config.json`

> **Security:** Never commit this file to version control. Add it to `.gitignore`.

# Firebase Web API Key Setup

This README explains how to locate and configure the Firebase Web API Key for client‑side usage.

## 1️⃣ Navigate to Firebase Console
1. Visit https://console.firebase.google.com  
2. Select your Firebase project from the list.

## 2️⃣ Open Project Settings
1. Click the ⚙️ **Project settings** icon next to “Project Overview.”  
2. Ensure you are on the **General** tab.

## 3️⃣ Locate Your Web API Key
1. Scroll to the **Your apps** section.  
2. Select your **Web app** (</> icon) if not already selected.  
3. Under **Firebase SDK snippet**, find the **apiKey** field.  
4. Copy the value of **apiKey** — this is your Web API Key.

## 4️⃣ Store the API Key Securely
Add the key to your environment variables instead of hardcoding it:

```bash
# .env.local (for local development)
FIREBASE_API_KEY=YOUR_API_KEY_HERE
