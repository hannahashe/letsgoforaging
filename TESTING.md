# Testing

This document records manual testing for the Let’s Go Foraging Django MVP.

## Navigation

| Test | Expected result | Status |
|---|---|---|
| Click site logo | User is taken to the homepage | Pass |
| Click Walks nav link | User is taken to `/walks/` | Pass |
| Click Field Notes nav link | User is taken to `/field-notes/` | Pass |
| Click Gallery nav link | User is taken to `/gallery/` | Pass |
| Click About nav link | User is taken to `/about/` | Pass |
| Click Contact nav link | User is taken to `/contact/` | Pass |
| Active nav state appears on section pages | Current section is visually highlighted | Pass |

## Events / Walks

| Test | Expected result | Status |
|---|---|---|
| Published future event appears on Walks page | Event is visible on `/walks/` | Pass |
| Unpublished event does not appear on Walks page | Event is hidden from public page | Pass |
| Past event does not appear on Walks page | Event is hidden from upcoming events | Pass |
| Past published event appears in archive | Event appears on `/walks/archive/` | Pass |
| Event title/detail link opens detail page | User is taken to the event detail page | Pass |
| Event detail page displays event date, time, location and description | Correct event information is shown | Pass |
| External ticket link opens in a new tab | Booking site opens separately | Pass |

## Blog / Field Notes

| Test | Expected result | Status |
|---|---|---|
| Published blog post appears on Field Notes page | Post is visible on `/field-notes/` | Pass |
| Unpublished blog post does not appear publicly | Post is hidden from public pages | Pass |
| Blog post title/detail link opens detail page | User is taken to the blog detail page | Pass |
| Blog detail page displays excerpt and body text | Correct post information is shown | Pass |

## Gallery

| Test | Expected result | Status |
|---|---|---|
| Published gallery image appears on Gallery page | Image is visible on `/gallery/` | Pass |
| Unpublished gallery image does not appear publicly | Image is hidden from public page | Pass |
| Gallery image displays alt text in template | Image includes alt attribute | Pass |
| Featured gallery image appears on homepage | Featured image appears in homepage preview | Pass |

## Reviews

| Test | Expected result | Status |
|---|---|---|
| Published featured review appears on homepage | Review is visible in What People Say section | Pass |
| Unpublished review does not appear publicly | Review is hidden from homepage | Pass |
| Review displays reviewer name, quote, rating and source | Correct review information is shown | Pass |

## Homepage

| Test | Expected result | Status |
|---|---|---|
| Featured future event appears on homepage | Featured walk is shown | Pass |
| Past featured event does not appear on homepage | Past event is hidden | Pass |
| Featured blog post appears on homepage | Featured Field Note is shown | Pass |
| Featured gallery images appear on homepage | Gallery preview is shown | Pass |
| Featured reviews appear on homepage | Reviews are shown | Pass |
| CTA button links to Walks page | User is taken to `/walks/` | Pass |

## Static and error pages

| Test | Expected result | Status |
|---|---|---|
| CSS loads in development | Site is styled correctly | Pass |
| `collectstatic` runs successfully | Static files collect into `staticfiles/` | Pass |
| Custom 404 page appears with `DEBUG=False` | Branded 404 page is shown | Pass |

## Admin

| Test | Expected result | Status |
|---|---|---|
| Admin user can log in | Django admin dashboard is accessible | Pass |
| Admin can create and edit events | Event saves successfully | Pass |
| Admin can create and edit blog posts | Blog post saves successfully | Pass |
| Admin can create and edit gallery images | Gallery image saves successfully | Pass |
| Admin can create and edit reviews | Review saves successfully | Pass |
| Admin forms are grouped into readable sections | Fieldsets display correctly | Pass |

## Environment settings

| Test | Expected result | Status |
|---|---|---|
| `SECRET_KEY` loads from `env.py` locally | Project runs without hardcoded secret in settings | Pass |
| `DEBUG` loads from `env.py` locally | Development mode works | Pass |
| `ALLOWED_HOSTS` loads from `env.py` locally | `127.0.0.1` and `localhost` work | Pass |
| `CSRF_TRUSTED_ORIGINS` loads from `env.py` locally | Admin forms save correctly | Pass |
| `env.py` is ignored by Git | File is not shown in `git status` | Pass |