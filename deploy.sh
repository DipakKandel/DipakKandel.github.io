#!/bin/bash

echo "🚀 Starting Django Portfolio Deployment..."

# Activate virtual environment
echo "📦 Activating virtual environment..."
source venv/bin/activate

# Install/update dependencies
echo "📥 Installing dependencies..."
pip install -r requirements.txt

# Collect static files
echo "📁 Collecting static files..."
python manage.py collectstatic --noinput

# Make migrations
echo "🗄️ Creating database migrations..."
python manage.py makemigrations

# Apply migrations
echo "🔄 Applying migrations..."
python manage.py migrate

# Create superuser if it doesn't exist
echo "👤 Checking superuser..."
python manage.py shell -c "
from django.contrib.auth.models import User
if not User.objects.filter(username='admin').exists():
    User.objects.create_superuser('admin', 'dipak.itsme@gmail.com', 'admin123')
    print('Superuser created: admin/admin123')
else:
    print('Superuser already exists')
"

echo "✅ Local deployment preparation complete!"
echo ""
echo "🌐 Next steps:"
echo "1. Go to https://railway.app"
echo "2. Sign in with GitHub"
echo "3. Create new project from GitHub repo"
echo "4. Select your repository: dipakKandel/dipakKandel.github.io"
echo "5. Railway will automatically deploy your Django app"
echo ""
echo "📖 See DEPLOYMENT.md for detailed instructions"
echo ""
echo "🎯 Your portfolio will be live at: https://your-domain.railway.app/"
echo "🔒 Privacy Policy: https://your-domain.railway.app/privacy-policy/"
echo "⚙️ Admin Panel: https://your-domain.railway.app/admin/"
