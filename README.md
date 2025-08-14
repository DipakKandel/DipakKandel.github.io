# Dipak Kandel - Portfolio Website (Django)

A modern, responsive portfolio website built with Django that allows easy content management through an admin panel.

## 🚀 Features

- **Django Backend**: Full-featured Django application with admin interface
- **Content Management**: Easy to update portfolio content through Django admin
- **Modern Design**: Clean, professional design with dark theme
- **Responsive Layout**: Fully responsive design that works on all devices
- **Dynamic Content**: All content is pulled from database models
- **Contact Form**: Functional contact form with database storage
- **Image Management**: Easy image uploads for projects and profile

## 🛠️ Technologies Used

- **Backend**: Django 5.2.5
- **Database**: SQLite (can be easily changed to PostgreSQL/MySQL)
- **Frontend**: HTML5, CSS3, JavaScript
- **Styling**: Custom CSS with modern design
- **Icons**: Font Awesome
- **Fonts**: Inter (Google Fonts)

## 📁 Project Structure

```
dipakKandel.github.io/
├── manage.py                 # Django management script
├── requirements.txt          # Python dependencies
├── portfolio/               # Main portfolio app
│   ├── models.py           # Database models
│   ├── views.py            # View functions
│   ├── admin.py            # Admin interface
│   └── urls.py             # URL patterns
├── portfolio_project/       # Django project settings
│   ├── settings.py         # Project configuration
│   └── urls.py             # Main URL configuration
├── templates/               # HTML templates
│   └── portfolio/
│       └── home.html       # Main portfolio page
├── static/                  # Static files
│   ├── css/
│   │   └── style.css       # Main stylesheet
│   ├── js/
│   │   └── main.js         # JavaScript functionality
│   └── images/             # Static images
├── media/                   # User uploaded content
│   ├── profile/            # Profile images
│   └── projects/           # Project images
└── venv/                   # Virtual environment
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8+
- pip

### Installation

1. **Clone the repository**

   ```bash
   git clone <repository-url>
   cd dipakKandel.github.io
   ```

2. **Create and activate virtual environment**

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**

   ```bash
   python manage.py makemigrations
   python manage.py migrate
   ```

5. **Create superuser**

   ```bash
   python manage.py createsuperuser
   ```

6. **Run the development server**

   ```bash
   python manage.py runserver
   ```

7. **Access the website**
   - Portfolio: http://127.0.0.1:8000/
   - Admin: http://127.0.0.1:8000/admin/

## 📊 Database Models

### PersonalInfo

- Name, title, description
- Contact information (email, phone, location)
- Social media links
- Profile image

### Skill

- Skill name and category
- Proficiency level (1-10)
- Ordering for display

### Experience

- Job title, company, location
- Start/end dates
- Description and achievements
- Technologies used

### Project

- Project title and description
- Image and links (GitHub, live)
- Associated technologies
- Featured flag for homepage

### Education

- Degree and institution
- Dates and location
- GPA and description

### Achievement

- Achievement title and description
- Year and organization
- Certificate links

### Contact

- Contact form submissions
- Read/unread status
- Timestamp

### SiteSettings

- Configurable site content
- Hero section text
- Section titles and descriptions

## 🎨 Customization

### Adding Content

1. Access Django admin at `/admin/`
2. Use the intuitive interface to add/edit content
3. All changes are immediately reflected on the website

### Styling

- Edit `static/css/style.css` for design changes
- Modify `templates/portfolio/home.html` for layout changes

### Adding New Sections

1. Create new models in `portfolio/models.py`
2. Add admin configuration in `portfolio/admin.py`
3. Update views in `portfolio/views.py`
4. Modify templates as needed

## 🔧 Configuration

### Environment Variables

Create a `.env` file for production settings:

```env
DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-database-url
EMAIL_HOST=your-email-host
EMAIL_PORT=587
EMAIL_HOST_USER=your-email
EMAIL_HOST_PASSWORD=your-password
```

### Email Configuration

Update email settings in `portfolio_project/settings.py`:

```python
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'your-smtp-host'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'your-email'
EMAIL_HOST_PASSWORD = 'your-password'
```

## 📱 Responsive Design

- **Desktop**: 1200px and above
- **Tablet**: 768px - 1199px
- **Mobile**: Below 768px

## 🚀 Deployment

### Production Checklist

1. Set `DEBUG = False`
2. Update `SECRET_KEY`
3. Configure production database
4. Set up static file serving
5. Configure email backend
6. Set `ALLOWED_HOSTS`

### Recommended Hosting

- **Heroku**: Easy deployment with PostgreSQL
- **DigitalOcean**: VPS with full control
- **AWS**: Scalable cloud hosting
- **Vercel**: Static hosting with Django API

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📞 Support

For questions or support:

- Email: dipak.itsme@gmail.com
- GitHub: [github.com/DipakKandel](https://github.com/DipakKandel)

## 📄 License

This project is licensed under the MIT License.

---

**Made with ❤️ in Sydney, Australia** - Dipak Kandel
