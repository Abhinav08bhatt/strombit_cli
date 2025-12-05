# PLAN.md  
## stormbit Web v2.0 — Development Plan

stormbit v2.0 will be a minimal, modern web application that fetches weather information from the Visual Crossing API, displays it in a clean UI, and provides users with current, hourly, and weekly forecasts.

The goal is to deliver a fully functional, deployable, portfolio-ready weather website by 31 December.

---

# 1. Project Goals

- Build a modern frontend weather application using:
  - HTML
  - CSS
  - JavaScript (ES6, no framework for v2.0)
- Provide a clean, minimal UI with:
  - Current weather
  - Hourly forecast
  - 7-day forecast
- Search functionality for any city worldwide.
- Graceful handling of invalid inputs and API errors.
- Deploy on Vercel or Netlify.

---

# 2. Features

## 2.1 Core Features (v2.0)

### 1. Search
- User enters a city name.
- App fetches weather data from the API.
- Renders results dynamically.

### 2. Current Weather Section
Displays:
- Temperature (°C)
- Feels like
- Conditions (Clear, Rain, Cloudy…)
- Humidity
- Wind speed
- Local date and time

### 3. Hourly Forecast (Today)
For every hour:
- Time
- Temperature
- Condition
- Simple icon

### 4. Weekly Forecast (Next 7 Days)
For each day:
- Date (formatted)
- Max / Min temperature
- Conditions
- Small icon or emoji

### 5. Error Handling
- Invalid city message
- “No data available”
- Network error fallback

---

# 3. Tech Stack

### Frontend Only
- HTML5  
- CSS3  
- JavaScript (ES6 Modules)

### API
- Visual Crossing Weather API

### Deployment
- Vercel (recommended)
- Netlify (alternative)

---

# 4. Folder Structure

```
stormbit-web/
│
├── index.html
│
├── style/
│   └── main.css
│
├── js/
│   ├── app.js
│   ├── api.js
│   ├── render.js
│   └── utils.js
│
└── assets/
    └── icons/
```

---

# 5. Architecture Overview

### app.js
- Reads user input.
- Calls `getWeather(city)`.
- Triggers render functions:
  - `renderCurrentWeather(data)`
  - `renderHourly(data)`
  - `renderWeekly(data)`

### api.js
- Handles API requests.
- Fetches and returns JSON.
- Raises proper errors if needed.

### render.js
- Updates DOM elements.
- Generates UI blocks for:
  - Current weather
  - Hourly data
  - Weekly data

### utils.js
- Time formatting helpers.
- Date formatting helpers.
- Condition → icon mappings.

---

# 6. UI / Design Requirements

### Overall
- Minimal, clean, modern layout.
- Soft neutral background (light theme).
- Rounded cards with subtle shadows.
- Modern sans-serif font.
- Mobile-first responsive design.

### Sections
1. Search Bar
2. Current Weather Card
3. Hourly Forecast Strip (scrollable)
4. Weekly Forecast Grid

---

# 7. Milestones & Timeline

### Phase 1 — UI Layout (Dec 22 – Dec 24)
- Build static HTML structure.
- Style using CSS.
- Create responsive layout.
- Prepare empty sections for JS.

### Phase 2 — API Integration (Dec 25 – Dec 27)
- Implement fetch logic.
- Render current weather.
- Render hourly forecast.
- Render weekly forecast.
- Add loading and error states.

### Phase 3 — Polish & UX (Dec 28 – Dec 29)
- Improve spacing, typography, alignment.
- Add icons for weather.
- Add transitions.
- Improve mobile layouts.

### Phase 4 — Deployment (Dec 30 – Dec 31)
- Final cleanup.
- Write README.
- Deploy to Vercel / Netlify.
- Capture screenshots for portfolio.

---

# 8. Final Deliverables
By 31 December:
- Fully working live website.
- Clean modular codebase.
- README with screenshots.
- Deployment link.
- Version 2.0 release tag.

---

> Notes :
- stormbit v2.0 focuses on a frontend-only implementation to keep development simple and fast
- A backend (FastAPI / Flask) may be introduced in future versions if needed.
