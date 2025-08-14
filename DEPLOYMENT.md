# 🚀 Deployment Guide - Django Portfolio to Railway

This guide will help you deploy your Django portfolio to Railway for free hosting.

## 📋 Prerequisites

1. **GitHub Account** - Your code is already here
2. **Railway Account** - Sign up at [railway.app](https://railway.app)
3. **Python 3.11+** - For local development

## 🔧 Step 1: Prepare Your Project

### Install Production Dependencies

```bash
pip install -r requirements.txt
```

### Collect Static Files

```bash
python manage.py collectstatic --noinput
```

### Create Database Migrations

```bash
python manage.py makemigrations
python manage.py migrate
```

### Create Superuser

```bash
python manage.py createsuperuser
```

## 🌐 Step 2: Deploy to Railway

### Option A: Deploy via Railway Dashboard

1. **Go to [Railway.app](https://railway.app)**
2. **Sign in with GitHub**
3. **Click "New Project"**
4. **Select "Deploy from GitHub repo"**
5. **Choose your repository**: `dipakKandel/dipakKandel.github.io`
6. **Select the main branch**

### Option B: Deploy via Railway CLI

1. **Install Railway CLI**

   ```bash
   npm install -g @railway/cli
   ```

2. **Login to Railway**

   ```bash
   railway login
   ```

3. **Initialize Railway in your project**

   ```bash
   railway init
   ```

4. **Deploy**
   ```bash
   railway up
   ```

## ⚙️ Step 3: Configure Environment Variables

In Railway dashboard, add these environment variables:

```
SECRET_KEY=your-super-secret-key-here
DEBUG=False
ALLOWED_HOSTS=your-railway-domain.railway.app
DATABASE_URL=sqlite:///db.sqlite3
```

## 🔐 Step 4: Generate Secret Key

Generate a new secret key:

```bash
python -c "from django.core.management.utils import get_random_secret_key; print(get_random_secret_key())"
```

## 📊 Step 5: Populate Your Data

After deployment, you'll need to add your content:

1. **Access Admin Panel**: `https://your-domain.railway.app/admin/`
2. **Login with your superuser credentials**
3. **Add your personal information, projects, skills, etc.**

## 🌍 Step 6: Access Your Live Portfolio

Your portfolio will be available at:

- **Main Site**: `https://your-domain.railway.app/`
- **Privacy Policy**: `https://your-domain.railway.app/privacy-policy/`
- **Admin Panel**: `https://your-domain.railway.app/admin/`

## 🔄 Step 7: Automatic Deployments

Railway will automatically redeploy when you push to GitHub:

```bash
git add .
git commit -m "Update portfolio content"
git push origin main
```

## 🛠️ Troubleshooting

### Common Issues:

1. **Static Files Not Loading**

   - Run `python manage.py collectstatic` locally
   - Check `STATIC_ROOT` in settings

2. **Database Issues**

   - Ensure migrations are applied
   - Check `DATABASE_URL` environment variable

3. **Environment Variables**
   - Verify all required variables are set in Railway
   - Check for typos in variable names

## 📱 Custom Domain (Optional)

1. **In Railway dashboard, go to your project**
2. **Click "Settings" → "Domains"**
3. **Add your custom domain**
4. **Update DNS records as instructed**

## 💰 Cost

- **Railway Free Tier**: $5/month credit
- **Django Portfolio**: ~$2-3/month
- **Remaining Credit**: $2-3/month for other projects

## 🎯 Next Steps

After deployment:

1. **Test all functionality**
2. **Update your resume with the live URL**
3. **Share your portfolio with potential employers**
4. **Monitor Railway dashboard for usage**

## 📞 Support

If you encounter issues:

- **Railway Docs**: [docs.railway.app](https://docs.railway.app)
- **Django Docs**: [docs.djangoproject.com](https://docs.djangoproject.com)
- **Your Email**: dipak.itsme@gmail.com

---

**Happy Deploying! 🚀**
