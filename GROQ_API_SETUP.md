# 🔐 Groq API Setup - HackForce AI API

## ✅ Groq API Key Configured

Your Groq API key has been added to the local `.env` file and is ready to use.

---

## 🚀 For Vercel Deployment

When deploying to Vercel, you need to add the Groq API key as an environment variable.

### Step-by-Step Instructions

1. **Go to Vercel Dashboard**
   - Visit: https://vercel.com/dashboard
   - Select your project: `hackforce-ai-api`

2. **Navigate to Environment Variables**
   - Click "Settings" tab
   - Click "Environment Variables" in the left sidebar

3. **Add Groq API Key**
   - Click "Add New"
   - Enter the following:
     ```
     Name: GROQ_API_KEY
     Value: [Your Groq API key from local .env file]
     ```
   - Select environments: ✅ Production ✅ Preview ✅ Development
   - Click "Save"

4. **Redeploy**
   - Go to "Deployments" tab
   - Click "Redeploy" on the latest deployment
   - Or push a new commit to trigger deployment

---

## 📋 Where to Find Your Groq API Key

### Option 1: From Local .env File
Your Groq API key is already in: `backend/.env`

Open the file and copy the value after `GROQ_API_KEY=`

### Option 2: From Groq Dashboard
1. Go to: https://console.groq.com
2. Sign in to your account
3. Navigate to API Keys section
4. Copy your API key

---

## 🔒 Security Best Practices

### ✅ DO:
- Keep API keys in environment variables
- Use different keys for development and production
- Rotate keys periodically
- Monitor API usage

### ❌ DON'T:
- Commit API keys to Git (already protected by .gitignore)
- Share API keys publicly
- Hardcode keys in source code
- Use production keys in development

---

## 🧪 Testing Groq API

### Local Testing
```bash
cd backend
source venv/bin/activate  # Windows: venv\Scripts\activate
python -c "import os; from dotenv import load_dotenv; load_dotenv(); print('Groq API Key configured:', 'Yes' if os.getenv('GROQ_API_KEY') else 'No')"
```

### Production Testing
After deployment, check:
- Vercel function logs for any API errors
- Test endpoints that use Groq API
- Monitor API usage in Groq dashboard

---

## 📊 Groq API Features

Your HackForce AI API can use Groq for:
- 🤖 Advanced bug classification
- 📝 Natural language processing
- 🔍 Bug report analysis
- 💡 Smart developer assignment
- 📊 Sentiment analysis

---

## 🎯 Next Steps

1. ✅ Groq API key is in local `.env`
2. 🔄 Add to Vercel environment variables (when deploying)
3. 🚀 Deploy your application
4. ✅ Test Groq-powered features

---

## 💡 Groq API Limits

### Free Tier
- Check your limits at: https://console.groq.com
- Monitor usage to avoid rate limits
- Upgrade if needed for production

### Rate Limiting
- Implement rate limiting in your API
- Cache responses when possible
- Handle errors gracefully

---

## 🆘 Troubleshooting

### Issue: "Groq API key not found"
**Solution:**
1. Verify key is in `.env` file
2. Check environment variable name is correct: `GROQ_API_KEY`
3. Restart backend server after adding key

### Issue: "Groq API authentication failed"
**Solution:**
1. Verify API key is correct
2. Check key hasn't expired
3. Ensure no extra spaces in key value

### Issue: "Rate limit exceeded"
**Solution:**
1. Check usage in Groq dashboard
2. Implement caching
3. Consider upgrading plan

---

## 📚 Resources

- **Groq Console:** https://console.groq.com
- **Groq Documentation:** https://console.groq.com/docs
- **API Reference:** https://console.groq.com/docs/api-reference

---

**Your Groq API is configured and ready to power HackForce AI API! 🚀**

---

*Last Updated: January 29, 2026*  
*Security: Protected* 🔐
