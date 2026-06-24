# 💒 Wedding Invitation Website

A beautiful, animated wedding invitation website built with Flask + HTML/CSS/JS.

## 📁 Project Structure

```
wedding/
├── app.py                  ← Flask backend (RSVP endpoints)
├── requirements.txt        ← Python dependencies
├── wedding_data.json       ← All wedding details (edit this!)
├── rsvp_responses.json     ← Stored RSVP submissions
├── setup_assets.py         ← Downloads placeholder images
├── templates/
│   └── index.html          ← Main wedding page (Jinja2 template)
├── static/
│   ├── images/             ← Wedding photos
│   │   ├── hero.jpg        ← Hero background
│   │   ├── bride1-3.jpg    ← Gallery photos
│   │   ├── venue.jpg       ← Venue image
│   │   └── parents1-4.jpg  ← Parents gallery
│   └── music/
│       └── wedding-song.mp3 ← Background music
└── .gitignore
```

## 🚀 How to Run Locally

### Step 1: Open Terminal and navigate to the project

```bash
cd /Users/knayak1/PycharmProjects/wedding
```

### Step 2: (Optional) Create a virtual environment

```bash
python3 -m venv venv
source venv/bin/activate
```

### Step 3: Install dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Download placeholder images (first time only)

```bash
python3 setup_assets.py
```

### Step 5: Run the app

```bash
python3 app.py
```

### Step 6: Open in browser

Go to: **http://127.0.0.1:5000**

---

## ✨ Features

| Feature | Status |
|---------|--------|
| Countdown timer to wedding date | ✅ |
| Photo gallery with horizontal scroll | ✅ |
| Scratch card to reveal wedding date | ✅ |
| Events timeline (Haldi, Mehendi, Wedding, Reception) | ✅ |
| Venue with Google Maps link | ✅ |
| Background music player | ✅ |
| Family blessings section | ✅ |
| Parents gallery | ✅ |
| RSVP form (saves to JSON) | ✅ |
| WhatsApp share button | ✅ |
| Scroll animations | ✅ |
| Mobile responsive | ✅ |
| Admin endpoint to view RSVPs | ✅ |

## 🔗 Endpoints

| URL | Method | Description |
|-----|--------|-------------|
| `/` | GET | Main wedding page |
| `/rsvp` | POST | Submit RSVP form |
| `/rsvp/list` | GET | View all RSVPs (admin) |

## 🛠️ Customization

### Change wedding details:
Edit `wedding_data.json` — update names, dates, venue, events, etc.

### Replace images:
Drop your real photos into `static/images/` with the same filenames.

### Add real music:
Replace `static/music/wedding-song.mp3` with an actual .mp3 file.

---

## 📝 Future Improvements

- [ ] Add database (SQLite/PostgreSQL) for RSVP storage
- [ ] Add admin dashboard with password protection
- [ ] Add email/SMS notifications on RSVP
- [ ] Add photo upload from guests
- [ ] Deploy to Vercel/Railway/Render
- [ ] Add guest count selector in RSVP
- [ ] Add multi-language support

